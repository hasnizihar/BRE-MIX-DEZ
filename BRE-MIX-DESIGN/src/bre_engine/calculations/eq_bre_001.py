from src.bre_engine.errors.exceptions import InvalidEngineeringInputError

def calculate_target_mean_strength(f_ck: float, m: float, tracker: 'TraceTracker' = None) -> float:
    """
    EQ-BRE-001: Calculate the target mean compressive strength (f_m).
    
    Source: BRE BR 331, Stage 1 (SRC-BRE-001)
    Equation: f_m = f_ck + M
    
    Args:
        f_ck (float): Characteristic strength (N/mm²)
        m (float): Margin (N/mm²)
        tracker (TraceTracker, optional): Tracker to log the calculation step.
        
    Returns:
        float: Target mean strength in N/mm², rounded to 1 decimal place.
        
    Raises:
        InvalidEngineeringInputError: If inputs violate valid ranges.
    """
    if f_ck <= 0:
        raise InvalidEngineeringInputError(f"f_ck must be > 0. Got: {f_ck}")
    
    if m < 0:
        raise InvalidEngineeringInputError(f"Margin (m) must be >= 0. Got: {m}")
        
    f_m = f_ck + m
    f_m_rounded = round(f_m, 1)
    
    if tracker:
        tracker.add_step(
            step_id="EQ-BRE-001",
            description="Calculate Target Mean Strength",
            inputs={"f_ck": f_ck, "m": m},
            equation_or_table="f_m = f_ck + M",
            source_id="SRC-BRE-001",
            output=f_m_rounded
        )
        
    return f_m_rounded
