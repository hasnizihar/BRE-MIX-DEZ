import math
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError

def calculate_standard_deviation(test_results: list[float]) -> float:
    """
    Calculate standard deviation from test results according to BR 331.
    Formula (page 7): s = sqrt(sum((x - m)^2) / (n - 1))
    
    Args:
        test_results (list[float]): List of raw test results (N/mm^2).
        
    Returns:
        float: Calculated standard deviation.
        
    Raises:
        InvalidEngineeringInputError: If fewer than 2 results are provided.
    """
    n = len(test_results)
    if n < 2:
        raise InvalidEngineeringInputError(f"Cannot calculate standard deviation with n={n} results. At least 2 are required.")
        
    m = sum(test_results) / n
    variance_sum = sum((x - m) ** 2 for x in test_results)
    s = math.sqrt(variance_sum / (n - 1))
    
    return s

def select_design_standard_deviation(
    f_ck: float,
    n_results: int,
    calculated_s: float = None,
    provider: 'EngineeringDataProvider' = None
) -> float:
    """
    Selects the design standard deviation based on BR 331 Figure 3 rules.
    
    Args:
        f_ck (float): Characteristic strength (N/mm^2)
        n_results (int): Number of previous test results
        calculated_s (float, optional): The calculated standard deviation if n >= 20.
        provider (EngineeringDataProvider): The verified data provider for Figure 3.
        
    Returns:
        float: The selected design standard deviation (N/mm^2).
        
    Raises:
        InvalidEngineeringInputError: If required inputs are missing or invalid.
        EngineeringDataUnavailableError: If Figure 3 data is unavailable/unverified.
    """
    if f_ck <= 0:
        raise InvalidEngineeringInputError(f"Characteristic strength (f_ck) must be > 0. Got: {f_ck}")
    if n_results < 0:
        raise InvalidEngineeringInputError(f"Number of results (n_results) must be >= 0. Got: {n_results}")
    if provider is None:
        raise ValueError("EngineeringDataProvider is required to access Figure 3 bounds.")
        
    fig3_data = provider.get_figure_3_data()
    line_a_pts = fig3_data.get("line_a", [])
    line_b_pts = fig3_data.get("line_b", [])
    
    def interpolate(pts, x_target):
        if not pts:
            raise ValueError("Figure 3 points missing.")
        
        # Exact match or find surrounding points
        for pt in pts:
            if pt["x"] == x_target:
                return pt["y"]
                
        # Find points for interpolation
        for i in range(len(pts) - 1):
            x1, y1 = pts[i]["x"], pts[i]["y"]
            x2, y2 = pts[i+1]["x"], pts[i+1]["y"]
            if x1 <= x_target <= x2:
                # Linear interpolation
                fraction = (x_target - x1) / (x2 - x1)
                return y1 + fraction * (y2 - y1)
                
        # If beyond maximum x, cap at the last point's y value
        if x_target > pts[-1]["x"]:
            return pts[-1]["y"]
            
        raise ValueError(f"Interpolation failed for x={x_target}")

    if n_results < 20:
        return interpolate(line_a_pts, f_ck)
    else:
        if calculated_s is None:
            raise InvalidEngineeringInputError(
                f"When n_results >= 20, calculated_s must be provided. Got: None"
            )
        if calculated_s < 0:
            raise InvalidEngineeringInputError(
                f"Standard deviation (calculated_s) must be >= 0. Got: {calculated_s}"
            )
            
        line_b_val = interpolate(line_b_pts, f_ck)
        return max(calculated_s, line_b_val)
