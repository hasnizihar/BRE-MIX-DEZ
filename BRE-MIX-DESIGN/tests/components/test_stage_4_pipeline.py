import pytest
import json
import os
from src.bre_engine.interpolation.graph_2d import Graph2DInterpolator
from src.bre_engine.calculations.eq_bre_004 import determine_total_aggregate_content
from src.bre_engine.errors.exceptions import EngineeringDataUnavailableError

class TestStage4Pipeline:
    """
    Tests the integration of DATA-002 (Figure 5) into the Stage 4 pipeline,
    specifically ensuring the provenance block functions correctly.
    """
    
    def test_production_pipeline_blocks_synthetic_data(self):
        # 1. Load actual Figure 5 data from disk
        file_path = os.path.join(
            os.path.dirname(__file__), 
            "../../04_ENGINEERING_DATA/GRAPHS/FIGURE_05/figure_05_points.json"
        )
        with open(file_path, "r") as f:
            data = json.load(f)
            
        # Ensure we test the synthetic block by modifying the data in memory
        data["status"] = "SYNTHETIC_PLACEHOLDER"
        assert data["status"] == "SYNTHETIC_PLACEHOLDER"
        
        # 2. Attempt to instantiate the provider/interpolator as a production service would
        with pytest.raises(EngineeringDataUnavailableError, match="SYNTHETIC_PLACEHOLDER"):
            interpolator = Graph2DInterpolator(data, allow_synthetic=False)
            # The calculation never even gets reached because the data fetch fails.
            
    def test_test_pipeline_allows_synthetic_data(self):
        # 1. Load actual Figure 5 data
        file_path = os.path.join(
            os.path.dirname(__file__), 
            "../../04_ENGINEERING_DATA/GRAPHS/FIGURE_05/figure_05_points.json"
        )
        with open(file_path, "r") as f:
            data = json.load(f)
            
        # 2. Instantiate with allow_synthetic=True
        interpolator = Graph2DInterpolator(data, allow_synthetic=True)
        
        # 3. Perform Figure 5 lookup (e.g. RD=2.6, W=160)
        wet_density = interpolator.interpolate(x_value=160, curve_value=2.6)
        assert wet_density == 2400.0
        
        # 4. Pipe into EQ-BRE-004
        result = determine_total_aggregate_content(
            wet_density=wet_density,
            cement_content=340,
            free_water_content=160
        )
        
        # 2400 - 340 - 160 = 1900
        assert result["total_aggregate_content"] == 1900.0
