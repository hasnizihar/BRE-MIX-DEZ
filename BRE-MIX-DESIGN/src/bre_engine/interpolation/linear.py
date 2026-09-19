from typing import List, Tuple
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError

def linear_interpolate(x: float, data_points: List[Tuple[float, float]]) -> float:
    """
    Performs strict linear interpolation on a set of known (x, y) coordinates.
    
    Args:
        x (float): The input value to interpolate.
        data_points (List[Tuple[float, float]]): The known data curve as (x, y) pairs.
        
    Returns:
        float: The interpolated y value.
        
    Raises:
        InvalidEngineeringInputError: If x is outside the bounds of the provided data
                                      (extrapolation is strictly prohibited).
        ValueError: If data_points contains less than 2 points or is not sorted by x.
    """
    if len(data_points) < 2:
        raise ValueError("Interpolation requires at least two data points.")
        
    # Ensure data is sorted by x
    for i in range(1, len(data_points)):
        if data_points[i][0] <= data_points[i-1][0]:
            raise ValueError("Data points must be strictly increasing in x.")
            
    x_min = data_points[0][0]
    x_max = data_points[-1][0]
    
    if x < x_min or x > x_max:
        raise InvalidEngineeringInputError(
            f"Input {x} is outside the known range [{x_min}, {x_max}]. "
            "Extrapolation is strictly not permitted."
        )
        
    # Exact point matches
    for point in data_points:
        if x == point[0]:
            return point[1]
            
    # Interpolation
    for i in range(len(data_points) - 1):
        x0, y0 = data_points[i]
        x1, y1 = data_points[i+1]
        
        if x0 < x < x1:
            # Linear interpolation formula: y = y0 + (x - x0) * (y1 - y0) / (x1 - x0)
            return y0 + (x - x0) * (y1 - y0) / (x1 - x0)
            
    # Should not reach here due to earlier bounds check
    raise RuntimeError("Failed to interpolate.")
