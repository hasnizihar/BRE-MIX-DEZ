from typing import Dict, Any, Optional
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError

def determine_fine_aggregate_content(
    total_aggregate_content: float,
    fine_aggregate_proportion_percentage: float,
    tracker: 'TraceTracker' = None
) -> Dict[str, Any]:
    """
    EQ-BRE-005: Determine fine aggregate content (Stage 5).
    
    Source: BRE BR 331, Section 5.5 (Calculation C5)
    Equation: Fine aggregate content = total aggregate content * proportion of fines
    
    Args:
        total_aggregate_content (float): Total aggregate in kg/m^3 (from Stage 4).
        fine_aggregate_proportion_percentage (float): Proportion of fine aggregate as a percentage (from Figure 6).
            For example, 27.0 for 27%.
        tracker (TraceTracker, optional): Tracker to log the calculation step.
        
    Returns:
        Dict containing:
            - 'fine_aggregate_content' (float): The fine aggregate content in kg/m^3
            
    Raises:
        InvalidEngineeringInputError: If total aggregate is <= 0 or proportion is outside (0, 100].
    """
    if total_aggregate_content <= 0:
        raise InvalidEngineeringInputError("Total aggregate content must be greater than 0.")
        
    if not (0 < fine_aggregate_proportion_percentage <= 100):
        raise InvalidEngineeringInputError(
            f"Fine aggregate proportion percentage must be between 0 and 100, "
            f"received {fine_aggregate_proportion_percentage}."
        )
        
    # Convert percentage to decimal fraction for calculation C5
    proportion_decimal = fine_aggregate_proportion_percentage / 100.0
    fine_aggregate = total_aggregate_content * proportion_decimal
    
    if tracker:
        tracker.add_step(
            step_id="EQ-BRE-005",
            description="Determine fine aggregate content",
            inputs={
                "total_aggregate_content": total_aggregate_content,
                "fine_aggregate_proportion_percentage": fine_aggregate_proportion_percentage
            },
            equation_or_table="C5: Fine aggregate = Total aggregate * (proportion % / 100)",
            source_id="EQ-BRE-005",
            output={
                "fine_aggregate_content": fine_aggregate
            },
            warnings=[]
        )
        
    return {
        "fine_aggregate_content": fine_aggregate
    }
