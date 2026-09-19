import pytest
import os
import json
from src.bre_engine.interpolation.graph_2d import Graph2DInterpolator
from src.bre_engine.errors.exceptions import EngineeringConstraintError

def get_figure_5_data():
    file_path = os.path.join(
        os.path.dirname(__file__), 
        "../../04_ENGINEERING_DATA/GRAPHS/FIGURE_05/figure_05_points.json"
    )
    with open(file_path, "r") as f:
        return json.load(f)

def get_interpolator():
    data = get_figure_5_data()
    return Graph2DInterpolator(data, allow_synthetic=False)

def test_figure_05_example_1_exact_match():
    """
    Validates that Figure 5 exactly reproduces the Example 1 value:
    Relative Density = 2.6
    Free Water Content = 160
    Expected Wet Density = 2400
    """
    interpolator = get_interpolator()
    wet_density = interpolator.interpolate(x_value=160.0, curve_value=2.6)
    assert wet_density == 2400.0

def test_figure_05_bounds():
    """
    Validates extreme interpolation bounds (min and max across both axes).
    """
    interpolator = get_interpolator()
    
    # 2.4 at 140
    wd_min_min = interpolator.interpolate(x_value=140.0, curve_value=2.4)
    assert wd_min_min == 2265.0
    
    # 2.9 at 240
    wd_max_max = interpolator.interpolate(x_value=240.0, curve_value=2.9)
    assert wd_max_max == 2515.0
    
def test_figure_05_1d_interpolation_along_curve():
    """
    Interpolates between x=140 and x=160 on curve 2.6.
    140 -> 2410
    160 -> 2400
    150 should be 2405.
    """
    interpolator = get_interpolator()
    wet_density = interpolator.interpolate(x_value=150.0, curve_value=2.6)
    assert wet_density == 2405.0
    
def test_figure_05_2d_interpolation():
    """
    Interpolates between x=160 on curves 2.6 and 2.7.
    2.6 at 160 -> 2400
    2.7 at 160 -> 2472
    2.65 at 160 should be 2436.
    """
    interpolator = get_interpolator()
    wet_density = interpolator.interpolate(x_value=160.0, curve_value=2.65)
    assert wet_density == 2436.0

def test_figure_05_extrapolation_blocked():
    interpolator = get_interpolator()
    
    # Free water < 140
    with pytest.raises(EngineeringConstraintError, match="outside the digitized bounds"):
        interpolator.interpolate(x_value=130.0, curve_value=2.6)
        
    # Free water > 240
    with pytest.raises(EngineeringConstraintError, match="outside the digitized bounds"):
        interpolator.interpolate(x_value=250.0, curve_value=2.6)
        
    # Relative density < 2.4
    with pytest.raises(EngineeringConstraintError, match="outside the digitized curves"):
        interpolator.interpolate(x_value=160.0, curve_value=2.3)
        
    # Relative density > 2.9
    with pytest.raises(EngineeringConstraintError, match="outside the digitized curves"):
        interpolator.interpolate(x_value=160.0, curve_value=3.0)
