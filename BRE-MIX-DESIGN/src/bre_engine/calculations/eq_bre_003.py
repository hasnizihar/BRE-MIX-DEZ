from typing import Optional, Dict, Any
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError, EngineeringConstraintError

def determine_cement_content(
    free_water_content: float,
    wc_ratio: float,
    min_cement_content: Optional[float] = None,
    max_cement_content: Optional[float] = None,
    tracker: 'TraceTracker' = None
) -> Dict[str, Any]:
    """
    EQ-BRE-003: Determine cement content (Stage 3).
    
    Source: BRE BR 331, Section 5.3 (Calculation C3)
    
    Args:
        free_water_content (float): Free-water content in kg/m^3 (from Stage 2)
        wc_ratio (float): Free-water/cement ratio (from Stage 1/2)
        min_cement_content (float, optional): Specified minimum cement content in kg/m^3
        max_cement_content (float, optional): Specified maximum cement content in kg/m^3
        tracker (TraceTracker, optional): Tracker to log the calculation step.
        
    Returns:
        Dict containing:
            - 'cement_content' (float): The final cement content in kg/m^3
            - 'modified_wc_ratio' (float, optional): Populated if the minimum cement constraint was triggered.
            
    Raises:
        InvalidEngineeringInputError: If inputs are non-positive.
        EngineeringConstraintError: If the calculated cement content exceeds the specified max_cement_content.
    """
    if free_water_content <= 0:
        raise InvalidEngineeringInputError("Free-water content must be greater than 0.")
    if wc_ratio <= 0:
        raise InvalidEngineeringInputError("W/C ratio must be greater than 0.")
        
    # Calculation C3
    calculated_cement = free_water_content / wc_ratio
    
    final_cement = calculated_cement
    modified_wc_ratio = None
    warnings = []
    
    if max_cement_content is not None and calculated_cement > max_cement_content:
        # Unresolvable conflict as per BR 331 Section 5.3
        raise EngineeringConstraintError(
            f"Calculated cement content ({calculated_cement:.2f} kg/m^3) exceeds specified "
            f"maximum ({max_cement_content} kg/m^3). "
            f"The specification cannot be met simultaneously on strength and workability requirements. "
            f"Consider changing cement type/class or aggregate size/type."
        )
        
    if min_cement_content is not None and calculated_cement < min_cement_content:
        final_cement = min_cement_content
        modified_wc_ratio = free_water_content / final_cement
        warnings.append(
            f"Calculated cement content ({calculated_cement:.2f} kg/m^3) is below specified "
            f"minimum ({min_cement_content} kg/m^3). Adopted minimum. W/C ratio modified."
        )
        
    if tracker:
        tracker.add_step(
            step_id="EQ-BRE-003",
            description="Determine cement content",
            inputs={
                "free_water_content": free_water_content,
                "wc_ratio": wc_ratio,
                "min_cement_content": min_cement_content,
                "max_cement_content": max_cement_content
            },
            equation_or_table="C3: cement = water / (w/c)",
            source_id="EQ-BRE-003",
            output={
                "cement_content": final_cement,
                "modified_wc_ratio": modified_wc_ratio
            },
            warnings=warnings
        )
        
    return {
        "cement_content": final_cement,
        "modified_wc_ratio": modified_wc_ratio
    }
