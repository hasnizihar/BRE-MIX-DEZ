import pytest
import math
from src.bre_engine.interpolation.curve_family import CurveFamilyInterpolator
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError

class TestCurveFamilyInterpolator:
    
    @pytest.fixture
    def mock_curves_data(self):
        # Let's create two mock curves using S = S_05 * exp(-1.56(w-0.5))
        # Curve 1: S_05 = 40
        # Curve 2: S_05 = 50
        def make_points(s_05):
            return [{'water_cement_ratio': w, 'strength': s_05 * math.exp(-1.56*(w - 0.5))} 
                    for w in [0.3, 0.4, 0.5, 0.6, 0.7]]
                    
        return [
            {'datum_strength_at_05': 40, 'points': make_points(40)},
            {'datum_strength_at_05': 50, 'points': make_points(50)}
        ]

    def test_interpolation_exact_datum(self, mock_curves_data):
        interpolator = CurveFamilyInterpolator(mock_curves_data)
        
        # Datum = 40 (exact match to Curve 1)
        # Find x where y = 40 * exp(-1.56*(0.6 - 0.5)) = 40 * 0.8555 = 34.22
        target_y = 40 * math.exp(-1.56 * (0.6 - 0.5))
        x = interpolator.find_x_for_y(target_y=target_y, datum_y=40.0)
        
        # Should return exactly 0.6
        assert pytest.approx(x, 0.01) == 0.6
        
    def test_interpolation_mid_datum(self, mock_curves_data):
        interpolator = CurveFamilyInterpolator(mock_curves_data)
        
        # Datum = 45 (midpoint between Curve 1 and Curve 2)
        # Because we linearly interpolate the *strengths*, the strength at w=0.6 for custom curve is
        # exactly the midpoint of strengths of Curve 1 and Curve 2 at w=0.6.
        s_curve1_06 = 40 * math.exp(-1.56 * 0.1) # 34.22
        s_curve2_06 = 50 * math.exp(-1.56 * 0.1) # 42.78
        target_y = (34.22 + 42.78) / 2 # 38.5
        
        x = interpolator.find_x_for_y(target_y=target_y, datum_y=45.0)
        assert pytest.approx(x, 0.01) == 0.6
        
    def test_datum_out_of_bounds(self, mock_curves_data):
        interpolator = CurveFamilyInterpolator(mock_curves_data)
        with pytest.raises(InvalidEngineeringInputError, match="Datum strength 60.0 is outside the bounds"):
            interpolator.find_x_for_y(target_y=30, datum_y=60.0)
            
    def test_target_strength_out_of_bounds(self, mock_curves_data):
        interpolator = CurveFamilyInterpolator(mock_curves_data)
        # Curve 1 limits: at W/C=0.7, y = 40 * exp(-1.56*0.2) = 29.2
        # If we ask for y = 20, it should throw
        with pytest.raises(InvalidEngineeringInputError, match="Target strength 20 is outside the valid range"):
            interpolator.find_x_for_y(target_y=20, datum_y=40.0, x_max=0.7)
