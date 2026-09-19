from typing import Dict, Any
from src.bre_engine.interpolation.graph_2d import Graph2DInterpolator
from src.bre_engine.data.provider import EngineeringDataProvider
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError

def determine_wet_density(
    free_water_content: float,
    relative_density: float,
    provider: EngineeringDataProvider,
    tracker: 'TraceTracker' = None
) -> float:
    """
    LKP-BRE-002: Determine estimated wet density of concrete (Stage 4).
    
    Source: BRE BR 331, Figure 5 (Printed page 18)
    Method: Continuous 2D graph lookup/interpolation based on Free-water content
            and Relative density of combined aggregate.
            
    Args:
        free_water_content (float): Free-water content in kg/m^3 (from Stage 2).
        relative_density (float): Relative density of combined aggregate (assumed or measured).
        provider (EngineeringDataProvider): Interface to securely retrieve Figure 5 data.
        tracker (TraceTracker, optional): Tracker for auditing.
        
    Returns:
        float: Estimated wet density of concrete in kg/m^3.
        
    Raises:
        InvalidEngineeringInputError: If inputs are non-positive.
        EngineeringDataUnavailableError: If Figure 5 is missing/unverified.
        EngineeringConstraintError: If inputs require extrapolation outside the validated graph bounds.
    """
    if free_water_content <= 0:
        raise InvalidEngineeringInputError("Free-water content must be greater than 0.")
    if relative_density <= 0:
        raise InvalidEngineeringInputError("Relative density must be greater than 0.")
        
    # 1. Fetch VERIFIED data from Figure 5
    figure_5_data = provider.get_figure_5_data()
    
    # 2. Package it for the Graph2DInterpolator 
    # Note: the interpolator expects a dict with 'status' and 'curves', but we returned a list of curves 
    # from provider.get_figure_5_data() to follow the pattern of get_figure_4_data().
    # Let's wrap it in a dict for the interpolator.
    interp_data = {
        "status": "DATA_AVAILABLE",  # If provider returned it, it passed verification
        "curves": figure_5_data
    }
    
    interpolator = Graph2DInterpolator(interp_data, allow_synthetic=False)
    
    # 3. Perform 2D Interpolation
    wet_density = interpolator.interpolate(x_value=free_water_content, curve_value=relative_density)
    
    if tracker:
        tracker.add_step(
            step_id="LKP-BRE-002",
            description="Determine estimated wet density",
            inputs={
                "free_water_content": free_water_content,
                "relative_density": relative_density
            },
            equation_or_table="Figure 5",
            source_id="DATA-002",
            output={
                "wet_density": wet_density
            },
            warnings=[]
        )
        
    return wet_density
