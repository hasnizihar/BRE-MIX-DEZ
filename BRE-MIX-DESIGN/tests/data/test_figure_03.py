import pytest
import json
import os
from src.bre_engine.errors.exceptions import EngineeringDataUnavailableError

def test_figure_03_schema():
    """Verify that the Figure 3 engineering data follows the correct schema and is verified."""
    file_path = os.path.join(
        "04_ENGINEERING_DATA", "GRAPHS", "FIGURE_03", "figure_03_points.json"
    )
    assert os.path.exists(file_path), "figure_03_points.json is missing"
    
    with open(file_path, 'r') as f:
        data = json.load(f)
        
    assert data["status"] == "VERIFIED", "Figure 3 must be VERIFIED for use in production"
    
    assert "line_a" in data
    assert "line_b" in data
    
    line_a = data["line_a"]
    line_b = data["line_b"]
    
    assert len(line_a) >= 3
    assert len(line_b) >= 3
    
    # Check Line A for fc >= 20 N/mm2 (where it should be 8.0)
    pt_20_a = next(pt for pt in line_a if pt["x"] == 20.0)
    assert pt_20_a["y"] == 8.0
    
    # Check Line B for fc >= 20 N/mm2 (where it should be 4.0)
    pt_20_b = next(pt for pt in line_b if pt["x"] == 20.0)
    assert pt_20_b["y"] == 4.0
