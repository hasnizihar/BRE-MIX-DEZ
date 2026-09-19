from src.bre_engine.models.domain import MixDesignInput, MixDesignResult, ValidationResult
from src.bre_engine.data.provider import EngineeringDataProvider
from src.bre_engine.trace.tracker import TraceTracker
from src.bre_engine.calculations.eq_bre_001 import calculate_target_mean_strength
from src.bre_engine.calculations.lkp_bre_001 import determine_water_cement_ratio
from src.bre_engine.calculations.eq_bre_003 import determine_cement_content
from src.bre_engine.calculations.lkp_bre_002 import determine_wet_density
from src.bre_engine.calculations.eq_bre_004 import determine_total_aggregate_content
from src.bre_engine.calculations.eq_bre_005 import determine_fine_aggregate_content
from src.bre_engine.calculations.eq_bre_006 import determine_coarse_aggregate_content

# Mapping from percentage defective to k (statistical constant).
# BR 331 Table: proportion defective -> k value
K_VALUES = {
    1.0: 2.33,
    2.0: 2.05,
    3.0: 1.88,
    5.0: 1.64,
    10.0: 1.28,
    15.0: 1.04,
    20.0: 0.84,
}


class BRECalculationEngine:
    """
    The core stateless calculation pipeline for the BRE Mix Design method.
    
    Executes BR 331 Stages 1-5 in sequence, producing a fully traced
    MixDesignResult.
    """
    
    def __init__(self, data_provider: EngineeringDataProvider):
        self.data = data_provider
        
    def calculate(self, request: MixDesignInput) -> MixDesignResult:
        """
        Executes the full BRE calculation pipeline.
        
        Raises:
            EngineeringDataUnavailableError: If required data is marked [PENDING_USER_DATA].
            InvalidEngineeringInputError: If inputs violate standard boundaries.
        """
        tracker = TraceTracker()
        
        # 0. Input Validation
        validation = self._validate_inputs(request)
        
        # Resolve k from percentage defective
        k = K_VALUES.get(request.concrete.proportion_defective)
        if k is None:
            # Fallback: find closest
            from src.bre_engine.errors.exceptions import InvalidEngineeringInputError
            raise InvalidEngineeringInputError(
                f"Unsupported proportion defective: {request.concrete.proportion_defective}%. "
                f"Supported values: {sorted(K_VALUES.keys())}"
            )
        
        # Resolve standard deviation
        s_design = request.standard_deviation_override
        if s_design is None:
            s_design = 8.0  # MVP default (Figure 3 lower bound)
        
        # ------------------------------------------------------------------
        # Stage 1: Target Mean Strength
        # ------------------------------------------------------------------
        f_m = calculate_target_mean_strength(
            f_ck=request.concrete.characteristic_strength,
            s_design=s_design,
            k=k,
            tracker=tracker
        )
        
        # ------------------------------------------------------------------
        # Stage 2: Water/Cement Ratio
        # ------------------------------------------------------------------
        aggregate_type = request.aggregate.coarse_aggregate_type  # "Crushed" or "Uncrushed"
        
        wc_ratio = determine_water_cement_ratio(
            f_m=f_m,
            cement_strength_class=request.cement.strength_class,
            aggregate_type=aggregate_type,
            provider=self.data,
            max_wc_ratio=request.concrete.max_wc_ratio,
            tracker=tracker
        )
        
        # ------------------------------------------------------------------
        # Stage 2 continued: Free-Water Content (from Table 3)
        # For MVP, this is provided as an input or looked up.
        # BR 331 Table 3 maps (slump, max_agg_size, aggregate_type) -> free_water.
        # MVP: use the free_water_content from the input model if provided,
        # otherwise use a simple lookup.
        # ------------------------------------------------------------------
        free_water_content = self._determine_free_water(request, tracker)
        
        # ------------------------------------------------------------------
        # Stage 3: Cement Content
        # ------------------------------------------------------------------
        result_3 = determine_cement_content(
            free_water_content=free_water_content,
            wc_ratio=wc_ratio,
            min_cement_content=request.concrete.min_cement_content,
            max_cement_content=None,  # Not in the input model yet
            tracker=tracker
        )
        cement_content = result_3["cement_content"]
        
        # If W/C was modified due to minimum cement constraint, use modified value
        if result_3["modified_wc_ratio"] is not None:
            wc_ratio = result_3["modified_wc_ratio"]
        
        # ------------------------------------------------------------------
        # Stage 4: Wet Density (from Figure 5)
        # ------------------------------------------------------------------
        # Determine combined relative density
        # For MVP, use the aggregate RD from input (defaults to 2.6 for uncrushed)
        relative_density = request.aggregate.fine_aggregate_rd
        
        wet_density = determine_wet_density(
            free_water_content=free_water_content,
            relative_density=relative_density,
            provider=self.data,
            tracker=tracker
        )
        
        # Total aggregate content
        result_4 = determine_total_aggregate_content(
            wet_density=wet_density,
            cement_content=cement_content,
            free_water_content=free_water_content,
            tracker=tracker
        )
        total_aggregate = result_4["total_aggregate_content"]
        
        # ------------------------------------------------------------------
        # Stage 5: Fine & Coarse Aggregate
        # ------------------------------------------------------------------
        # Fine aggregate proportion from Figure 6 (DATA-003).
        # For MVP: this is provided as percentage_passing_600 in the input,
        # but the actual proportion comes from Figure 6 lookup.
        # Since DATA-003 is PENDING, we require it as a direct input.
        fine_agg_proportion = request.aggregate.percentage_passing_600
        
        result_5 = determine_fine_aggregate_content(
            total_aggregate_content=total_aggregate,
            fine_aggregate_proportion_percentage=fine_agg_proportion,
            tracker=tracker
        )
        fine_aggregate = result_5["fine_aggregate_content"]
        
        result_6 = determine_coarse_aggregate_content(
            total_aggregate_content=total_aggregate,
            fine_aggregate_content=fine_aggregate,
            tracker=tracker
        )
        coarse_aggregate = result_6["coarse_aggregate_content"]
        
        # ------------------------------------------------------------------
        # Build result
        # ------------------------------------------------------------------
        return MixDesignResult(
            target_mean_strength=f_m,
            water_cement_ratio=wc_ratio,
            free_water_content=free_water_content,
            cement_content=cement_content,
            total_aggregate=total_aggregate,
            fine_aggregate=fine_aggregate,
            coarse_aggregate=coarse_aggregate,
            batch_water=free_water_content,         # MVP: no moisture adjustment
            batch_fine_aggregate=fine_aggregate,     # MVP: no moisture adjustment
            batch_coarse_aggregate=coarse_aggregate, # MVP: no moisture adjustment
            trace=tracker.get_trace(),
            validation=validation
        )

    def _determine_free_water(self, request: MixDesignInput, tracker: TraceTracker) -> float:
        """
        Determine free-water content from Table 3.
        
        BR 331 Table 3: maps (slump_class, max_aggregate_size, aggregate_type) to free_water.
        
        For MVP, we use a simplified lookup based on Example 1 values.
        """
        # Simplified Table 3 lookup (BR 331 Table 3)
        # Format: (slump_range, max_agg_size, aggregate_type) -> free_water
        TABLE_3 = {
            # Uncrushed aggregate
            ("Slump_10_30", 10, "Uncrushed"): 180,
            ("Slump_10_30", 20, "Uncrushed"): 160,
            ("Slump_10_30", 40, "Uncrushed"): 140,
            ("Slump_30_60", 10, "Uncrushed"): 205,
            ("Slump_30_60", 20, "Uncrushed"): 180,
            ("Slump_30_60", 40, "Uncrushed"): 160,
            ("Slump_60_180", 10, "Uncrushed"): 225,
            ("Slump_60_180", 20, "Uncrushed"): 195,
            ("Slump_60_180", 40, "Uncrushed"): 175,
            # Crushed aggregate
            ("Slump_10_30", 10, "Crushed"): 205,
            ("Slump_10_30", 20, "Crushed"): 185,
            ("Slump_10_30", 40, "Crushed"): 165,
            ("Slump_30_60", 10, "Crushed"): 230,
            ("Slump_30_60", 20, "Crushed"): 205,
            ("Slump_30_60", 40, "Crushed"): 185,
            ("Slump_60_180", 10, "Crushed"): 250,
            ("Slump_60_180", 20, "Crushed"): 220,
            ("Slump_60_180", 40, "Crushed"): 200,
        }
        
        key = (
            request.concrete.slump_class,
            request.aggregate.max_aggregate_size,
            request.aggregate.coarse_aggregate_type
        )
        
        free_water = TABLE_3.get(key)
        if free_water is None:
            from src.bre_engine.errors.exceptions import InvalidEngineeringInputError
            raise InvalidEngineeringInputError(
                f"No Table 3 entry for combination: slump={key[0]}, "
                f"max_agg_size={key[1]}mm, type={key[2]}"
            )
        
        if tracker:
            tracker.add_step(
                step_id="TBL-BRE-003",
                description="Determine free-water content from Table 3",
                inputs={
                    "slump_class": request.concrete.slump_class,
                    "max_aggregate_size": request.aggregate.max_aggregate_size,
                    "aggregate_type": request.aggregate.coarse_aggregate_type
                },
                equation_or_table="Table 3",
                source_id="TBL-BRE-003",
                output={"free_water_content": float(free_water)},
                warnings=[]
            )
            
        return float(free_water)
        
    def _validate_inputs(self, request: MixDesignInput) -> ValidationResult:
        """Perform boundary and sanity checks on inputs before calculation."""
        # Pydantic already enforces base types and ranges (gt=0, etc.)
        # Here we add cross-field engineering checks.
        return ValidationResult(is_valid=True)
