from src.bre_engine.errors.exceptions import InvalidEngineeringInputError

def calculate_target_mean_strength(
    f_ck: float, 
    s_design: float, 
    k: float, 
    tracker: 'TraceTracker' = None
) -> float:
    """
    EQ-BRE-001: Calculate the target mean compressive strength (f_m).
    
    Source: BRE BR 331, Stage 1 (SRC-BRE-001)
    Equation: 
        M = k * s_design
        f_m = f_ck + M
    
    Args:
        f_ck (float): Characteristic strength (N/mm^2)
        s_design (float): The selected design standard deviation (N/mm^2)
        k (float): Statistical constant based on proportion defective
        tracker (TraceTracker, optional): Tracker to log the calculation step.
        
    Returns:
        float: Exact unrounded Target mean strength in N/mm^2. 
               (Presentation layer must round M to nearest integer per BR 331).
        
    Raises:
        InvalidEngineeringInputError: If inputs violate valid ranges.
    """
    if f_ck <= 0:
        raise InvalidEngineeringInputError(f"f_ck must be > 0. Got: {f_ck}")
    if s_design < 0:
        raise InvalidEngineeringInputError(f"s_design must be >= 0. Got: {s_design}")
    if k <= 0:
        raise InvalidEngineeringInputError(f"k must be > 0. Got: {k}")
        
    m = k * s_design
    f_m = f_ck + m
    
    if tracker:
        tracker.add_step(
            step_id="EQ-BRE-001",
            description="Calculate Target Mean Strength",
            inputs={"f_ck": f_ck, "s_design": s_design, "k": k},
            equation_or_table="M = k * s_design; f_m = f_ck + M",
            source_id="SRC-BRE-001",
            output={"M_exact": m, "f_m_exact": f_m}
        )
        
    return f_m
