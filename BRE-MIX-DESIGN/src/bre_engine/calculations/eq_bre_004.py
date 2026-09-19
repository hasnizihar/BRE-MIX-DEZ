from typing import Dict, Any, Optional
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError, EngineeringConstraintError

def determine_total_aggregate_content(
    wet_density: float,
    cement_content: float,
    free_water_content: float,
    tracker: 'TraceTracker' = None
) -> Dict[str, Any]:
    """
    EQ-BRE-004: Determine total aggregate content (Stage 4).
    
    Source: BRE BR 331, Section 5.4 (Calculation C4)
    Equation: Total aggregate content = D - C - W
    
    Args:
        wet_density (float): Estimated wet density of concrete in kg/m^3 (from Figure 5).
        cement_content (float): Cement content in kg/m^3 (from Stage 3).
        free_water_content (float): Free-water content in kg/m^3 (from Stage 2).
        tracker (TraceTracker, optional): Tracker to log the calculation step.
        
    Returns:
        Dict containing:
            - 'total_aggregate_content' (float): The total aggregate content in kg/m^3
            
    Raises:
        InvalidEngineeringInputError: If any input is non-positive.
        EngineeringConstraintError: If the resulting total aggregate content is non-positive.
    """
    if wet_density <= 0:
        raise InvalidEngineeringInputError("Wet density must be greater than 0.")
    if cement_content <= 0:
        raise InvalidEngineeringInputError("Cement content must be greater than 0.")
    if free_water_content <= 0:
        raise InvalidEngineeringInputError("Free-water content must be greater than 0.")
        
    # Calculation C4
    total_aggregate = wet_density - cement_content - free_water_content
    
    if total_aggregate <= 0:
        raise EngineeringConstraintError(
            f"Calculated total aggregate content ({total_aggregate:.2f} kg/m^3) is non-positive. "
            f"This indicates a physical impossibility where water + cement exceeds the wet density."
        )
        
    if tracker:
        tracker.add_step(
            step_id="EQ-BRE-004",
            description="Determine total aggregate content",
            inputs={
                "wet_density": wet_density,
                "cement_content": cement_content,
                "free_water_content": free_water_content
            },
            equation_or_table="C4: Aggregate = D - C - W",
            source_id="EQ-BRE-004",
            output={
                "total_aggregate_content": total_aggregate
            },
            warnings=[]
        )
        
    return {
        "total_aggregate_content": total_aggregate
    }
