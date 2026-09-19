from src.bre_engine.errors.exceptions import InvalidEngineeringInputError

def calculate_margin(k: float, s: float, tracker: 'TraceTracker' = None) -> float:
    """
    EQ-BRE-002: Calculate the statistical margin (M) above characteristic strength.
    
    Source: BRE BR 331, Stage 1 (SRC-BRE-001)
    Equation: M = k * s
    
    Args:
        k (float): Constant from standard normal distribution
        s (float): Standard deviation (N/mm²)
        tracker (TraceTracker, optional): Tracker to log the calculation step.
        
    Returns:
        float: Margin in N/mm²
        
    Raises:
        InvalidEngineeringInputError: If inputs violate valid ranges.
    """
    if k <= 0:
        raise InvalidEngineeringInputError(f"k must be > 0. Got: {k}")
        
    if s < 0:
        raise InvalidEngineeringInputError(f"Standard deviation (s) must be >= 0. Got: {s}")
        
    m = k * s
    
    if tracker:
        tracker.add_step(
            step_id="EQ-BRE-002",
            description="Calculate statistical margin",
            inputs={"k": k, "s": s},
            equation_or_table="M = k * s",
            source_id="SRC-BRE-001",
            output=m
        )
        
    return m
