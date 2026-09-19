import pytest
import json
import os
from src.bre_engine.errors.exceptions import EngineeringDataUnavailableError
from src.bre_engine.data.json_provider import JsonEngineeringDataProvider

def test_figure_04_schema():
    """Verify that the Figure 4 engineering data follows the correct schema and is verified."""
    file_path = os.path.join(
        "04_ENGINEERING_DATA", "GRAPHS", "FIGURE_04", "figure_04_points.json"
    )
    assert os.path.exists(file_path), "figure_04_points.json is missing"
    
    with open(file_path, 'r') as f:
        data = json.load(f)
        
    assert data["status"] == "VERIFIED", "Figure 4 must be VERIFIED for use in production"
    
    assert "x_axis" in data
    assert "y_axis" in data
    assert "curves" in data
    
    assert data["x_axis"]["domain"] == [0.3, 0.9]
    assert data["y_axis"]["domain"] == [0.0, 90.0]
    
    curves = data["curves"]
    assert len(curves) >= 2, "Curve interpolation requires at least 2 reference curves"
    
    # Check Curve 40
    curve_40 = next(c for c in curves if c["datum_strength_at_05"] == 40.0)
    pt_05 = next(p for p in curve_40["points"] if p["water_cement_ratio"] == 0.5)
    assert pt_05["strength"] == 40.0
    
def test_provider_raises_on_unverified_data(tmp_path):
    """If Figure 4 data is unverified or missing, it must block production."""
    # Create fake unverified data
    fake_dir = tmp_path / "04_ENGINEERING_DATA" / "GRAPHS" / "FIGURE_04"
    fake_dir.mkdir(parents=True)
    with open(fake_dir / "figure_04_points.json", 'w') as f:
        json.dump({"status": "PENDING_ENGINEERING_VERIFICATION", "curves": []}, f)
        
    provider = JsonEngineeringDataProvider(data_dir=str(tmp_path / "04_ENGINEERING_DATA"))
    
    with pytest.raises(EngineeringDataUnavailableError, match="pending engineering verification"):
        provider.get_figure_4_data()
