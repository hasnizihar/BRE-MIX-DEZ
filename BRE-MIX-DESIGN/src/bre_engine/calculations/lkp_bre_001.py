from typing import Optional
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError, EngineeringDataUnavailableError
from src.bre_engine.data.provider import EngineeringDataProvider

def determine_water_cement_ratio(
    f_m: float, 
    cement_strength_class: str, 
    aggregate_type: str, 
    provider: EngineeringDataProvider,
    max_wc_ratio: Optional[float] = None,
    tracker: 'TraceTracker' = None
) -> float:
    """
    LKP-BRE-001: Determine the target water/cement ratio (W/C).
    
    Source: BRE BR 331, Stage 2 (Figure 4) (SRC-BRE-001)
    
    Args:
        f_m (float): Target mean strength (N/mm²)
        cement_strength_class (str): Cement strength class (e.g. "42.5")
        aggregate_type (str): Aggregate type ("Crushed" or "Uncrushed")
        provider (EngineeringDataProvider): Interface to fetch Figure 4 data.
        max_wc_ratio (float, optional): Maximum allowed W/C ratio from durability constraints.
        tracker (TraceTracker, optional): Tracker to log the calculation step.
        
    Returns:
        float: Target water/cement ratio
        
    Raises:
        InvalidEngineeringInputError: If inputs violate valid ranges.
        EngineeringDataUnavailableError: If Figure 4 data (DATA-001) is missing.
    """
    if f_m <= 0:
        raise InvalidEngineeringInputError(f"Target mean strength f_m must be > 0. Got: {f_m}")
        
    # 1. Obtain datum strength at W/C = 0.5 from Table 2
    f_datum = provider.get_table_value(
        table_id="TBL-BRE-002",
        cement_strength_class=cement_strength_class,
        aggregate_type=aggregate_type,
        age=28
    )
    
    # 2. Obtain the Figure 4 mathematical curve family dataset
    curves_data = provider.get_figure_4_data()
    
    # 3. Perform 2D curve family interpolation
    from src.bre_engine.interpolation.curve_family import CurveFamilyInterpolator
    interpolator = CurveFamilyInterpolator(curves_data)
    wc_ratio = interpolator.find_x_for_y(target_y=f_m, datum_y=f_datum)
    
    # 4. Apply maximum W/C ratio cap if specified
    if max_wc_ratio is not None:
        if wc_ratio > max_wc_ratio:
            wc_ratio = max_wc_ratio
    
    if tracker:
        tracker.add_step(
            step_id="LKP-BRE-001",
            description="Determine target water/cement ratio via Figure 4 Curve Family Interpolation",
            inputs={
                "f_m": f_m, 
                "f_datum": f_datum,
                "max_wc_ratio": max_wc_ratio,
                "cement_strength_class": cement_strength_class,
                "aggregate_type": aggregate_type
            },
            equation_or_table="Figure 4 (Curve Family Interpolation)",
            source_id="DATA-001",
            output=wc_ratio,
            warnings=["Extrapolation is not permitted."]
        )
        
    return wc_ratio
