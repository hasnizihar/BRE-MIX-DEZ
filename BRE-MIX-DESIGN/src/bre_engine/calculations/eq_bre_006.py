from typing import Dict, Any, Optional
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError

def determine_coarse_aggregate_content(
    total_aggregate_content: float,
    fine_aggregate_content: float,
    tracker: 'TraceTracker' = None
) -> Dict[str, Any]:
    """
    EQ-BRE-006: Determine coarse aggregate content (Stage 5).
    
    Source: BRE BR 331, Section 5.5 (Printed page 16, PDF page 21).
    Note: BR 331 does not assign this calculation a formal 'C' identifier like C4 or C5.
    
    Equation: Coarse aggregate content = total aggregate content - fine aggregate content
    
    Args:
        total_aggregate_content (float): Total aggregate in kg/m^3 (from Stage 4).
        fine_aggregate_content (float): Fine aggregate content in kg/m^3 (from EQ-BRE-005).
        tracker (TraceTracker, optional): Tracker to log the calculation step.
        
    Returns:
        Dict containing:
            - 'coarse_aggregate_content' (float): The coarse aggregate content in kg/m^3
            
    Raises:
        InvalidEngineeringInputError: If total or fine aggregate is <= 0, or if fine > total.
    """
    if total_aggregate_content <= 0:
        raise InvalidEngineeringInputError("Total aggregate content must be greater than 0.")
        
    if fine_aggregate_content <= 0:
        raise InvalidEngineeringInputError("Fine aggregate content must be greater than 0.")
        
    if fine_aggregate_content >= total_aggregate_content:
        raise InvalidEngineeringInputError(
            f"Fine aggregate content ({fine_aggregate_content}) cannot be greater than "
            f"or equal to total aggregate content ({total_aggregate_content})."
        )
        
    # Exact mathematical subtraction. 
    # The rounding to the nearest 5kg found in BR 331 tables is a presentation/batching 
    # rule for the final form, not a mathematical constraint of the equation itself.
    coarse_aggregate = total_aggregate_content - fine_aggregate_content
    
    if tracker:
        tracker.add_step(
            step_id="EQ-BRE-006",
            description="Determine coarse aggregate content",
            inputs={
                "total_aggregate_content": total_aggregate_content,
                "fine_aggregate_content": fine_aggregate_content
            },
            equation_or_table="Coarse aggregate = Total aggregate - Fine aggregate",
            source_id="EQ-BRE-006",
            output={
                "coarse_aggregate_content": coarse_aggregate
            },
            warnings=[]
        )
        
    return {
        "coarse_aggregate_content": coarse_aggregate
    }
