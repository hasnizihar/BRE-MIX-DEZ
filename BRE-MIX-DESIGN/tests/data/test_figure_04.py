import pytest
import json
import os
import math
from src.bre_engine.errors.exceptions import EngineeringDataUnavailableError, InvalidEngineeringInputError
from src.bre_engine.data.json_provider import JsonEngineeringDataProvider
from src.bre_engine.interpolation.curve_family import CurveFamilyInterpolator

def load_figure_4_data():
    file_path = os.path.join(
        "04_ENGINEERING_DATA", "GRAPHS", "FIGURE_04", "figure_04_points.json"
    )
    with open(file_path, 'r') as f:
        return json.load(f)

def get_interpolator():
    data = load_figure_4_data()
    return CurveFamilyInterpolator(data["curves"])

def test_figure_04_schema():
    """Verify that the Figure 4 engineering data follows the correct schema and is verified."""
    data = load_figure_4_data()
        
    assert data["status"] == "VERIFIED", "Figure 4 must be VERIFIED for use in production"
    
    assert "x_axis" in data
    assert "y_axis" in data
    assert "curves" in data
    
    assert data["x_axis"]["domain"] == [0.3, 0.9]
    assert data["y_axis"]["domain"] == [0.0, 90.0]
    
    curves = data["curves"]
    assert len(curves) == 9, "Figure 4 has exactly 9 datum curves in BR 331"
    
    # Check Curve 40
    curve_40 = next(c for c in curves if c["datum_strength_at_05"] == 40.0)
    pt_05 = next(p for p in curve_40["points"] if p["water_cement_ratio"] == 0.5)
    assert pt_05["strength"] == 40.0
    
def test_provider_raises_on_unverified_data(tmp_path):
    """If Figure 4 data is unverified or missing, it must block production."""
    fake_dir = tmp_path / "04_ENGINEERING_DATA" / "GRAPHS" / "FIGURE_04"
    fake_dir.mkdir(parents=True)
    with open(fake_dir / "figure_04_points.json", 'w') as f:
        json.dump({"status": "PENDING_ENGINEERING_VERIFICATION", "curves": []}, f)
        
    provider = JsonEngineeringDataProvider(data_dir=str(tmp_path / "04_ENGINEERING_DATA"))
    
    with pytest.raises(EngineeringDataUnavailableError, match="pending engineering verification"):
        provider.get_figure_4_data()

def test_figure_04_example_1_validation():
    """
    Test Example 1: fm = 46 N/mm2.
    Expected W/C ratio is approximately 0.47.
    """
    interpolator = get_interpolator()
    wc_ratio = interpolator.find_x_for_y(target_y=46.0, datum_y=42.0)
    # Due to linear interpolation between 0.1 W/C nodes, 
    # the exact math yields ~0.46, which is within visual extraction tolerance of the 0.47 printed in Example 1.
    assert abs(wc_ratio - 0.47) <= 0.02

def test_figure_04_exact_curve():
    """
    Test exactly hitting a digitized curve boundary.
    Datum 40, target 40 -> W/C = 0.5.
    """
    interpolator = get_interpolator()
    wc_ratio = interpolator.find_x_for_y(target_y=40.0, datum_y=40.0)
    assert math.isclose(wc_ratio, 0.5)
    
def test_figure_04_between_adjacent_curves():
    """
    Test interpolating between two known adjacent curves.
    e.g., Datum 65, target 65 -> W/C = 0.5.
    """
    interpolator = get_interpolator()
    wc_ratio = interpolator.find_x_for_y(target_y=65.0, datum_y=65.0)
    assert math.isclose(wc_ratio, 0.5)

def test_figure_04_lower_upper_bounds():
    """Test lower and upper valid boundaries."""
    interpolator = get_interpolator()
    
    # Upper bound
    wc_upper = interpolator.find_x_for_y(target_y=70.0, datum_y=70.0)
    assert math.isclose(wc_upper, 0.5)
    
    # Lower bound
    wc_lower = interpolator.find_x_for_y(target_y=3.0, datum_y=3.0)
    assert math.isclose(wc_lower, 0.5)

def test_figure_04_outside_domain_fails():
    """Test outside valid domain boundaries (extrapolation is prohibited)."""
    interpolator = get_interpolator()
    
    # Above max datum (70)
    with pytest.raises(InvalidEngineeringInputError, match="outside the bounds"):
        interpolator.find_x_for_y(target_y=75.0, datum_y=75.0)
            
    # Below min datum (3)
    with pytest.raises(InvalidEngineeringInputError, match="outside the bounds"):
        interpolator.find_x_for_y(target_y=1.0, datum_y=1.0)
