import pytest
from src.bre_engine.interpolation.graph_2d import Graph2DInterpolator
from src.bre_engine.errors.exceptions import EngineeringConstraintError, EngineeringDataUnavailableError

@pytest.fixture
def figure_05_mock_data():
    return {
        "status": "DATA_AVAILABLE",
        "curves": [
            {
                "relative_density": 2.4,
                "points": [
                    {"free_water": 120, "wet_density": 2364.0},
                    {"free_water": 240, "wet_density": 2172.0}
                ]
            },
            {
                "relative_density": 2.6,
                "points": [
                    {"free_water": 120, "wet_density": 2464.0},
                    {"free_water": 160, "wet_density": 2400.0},
                    {"free_water": 180, "wet_density": 2368.0},
                    {"free_water": 240, "wet_density": 2272.0}
                ]
            },
            {
                "relative_density": 2.7,
                "points": [
                    {"free_water": 120, "wet_density": 2514.0},
                    {"free_water": 160, "wet_density": 2450.0},
                    {"free_water": 240, "wet_density": 2322.0}
                ]
            }
        ]
    }

class TestFigure05Interpolation:
    
    def test_exact_points(self, figure_05_mock_data):
        interpolator = Graph2DInterpolator(figure_05_mock_data)
        # Match Example 1
        assert interpolator.interpolate(x_value=160, curve_value=2.6) == 2400.0
        # Match Example 5
        assert interpolator.interpolate(x_value=160, curve_value=2.7) == 2450.0
        
    def test_w_interpolation(self, figure_05_mock_data):
        interpolator = Graph2DInterpolator(figure_05_mock_data)
        # Interpolate W between 160 and 180 on RD 2.6
        # W=170 -> exact midpoint between 2400 and 2368 => 2384
        val = interpolator.interpolate(x_value=170, curve_value=2.6)
        assert pytest.approx(val, 0.01) == 2384.0
        
    def test_rd_interpolation(self, figure_05_mock_data):
        interpolator = Graph2DInterpolator(figure_05_mock_data)
        # Interpolate RD between 2.6 and 2.7 for W=160
        # RD=2.65 -> midpoint between 2400 and 2450 => 2425
        val = interpolator.interpolate(x_value=160, curve_value=2.65)
        assert pytest.approx(val, 0.01) == 2425.0
        
    def test_2d_interpolation(self, figure_05_mock_data):
        interpolator = Graph2DInterpolator(figure_05_mock_data)
        # Interpolate RD=2.65, W=170
        val = interpolator.interpolate(x_value=170, curve_value=2.65)
        assert pytest.approx(val, 0.01) == 2409.0
        
    def test_out_of_bounds_w(self, figure_05_mock_data):
        interpolator = Graph2DInterpolator(figure_05_mock_data)
        with pytest.raises(EngineeringConstraintError, match="outside the digitized bounds"):
            interpolator.interpolate(x_value=100, curve_value=2.6)
            
    def test_out_of_bounds_rd(self, figure_05_mock_data):
        interpolator = Graph2DInterpolator(figure_05_mock_data)
        with pytest.raises(EngineeringConstraintError, match="outside the digitized curves"):
            interpolator.interpolate(x_value=160, curve_value=2.3)
            
    def test_synthetic_rejection(self, figure_05_mock_data):
        # Change status to SYNTHETIC_PLACEHOLDER
        figure_05_mock_data["status"] = "SYNTHETIC_PLACEHOLDER"
        
        with pytest.raises(EngineeringDataUnavailableError, match="SYNTHETIC_PLACEHOLDER"):
            Graph2DInterpolator(figure_05_mock_data, allow_synthetic=False)
            
        # Should succeed if allow_synthetic is True
        Graph2DInterpolator(figure_05_mock_data, allow_synthetic=True)
