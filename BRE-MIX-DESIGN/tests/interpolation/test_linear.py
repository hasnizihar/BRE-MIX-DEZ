import pytest
from src.bre_engine.interpolation.linear import linear_interpolate
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError

class TestLinearInterpolation:
    
    @pytest.fixture
    def sample_data(self):
        # A simple linear relationship y = 2x
        return [(10.0, 20.0), (20.0, 40.0), (30.0, 60.0)]
        
    def test_exact_points(self, sample_data):
        assert linear_interpolate(10.0, sample_data) == 20.0
        assert linear_interpolate(20.0, sample_data) == 40.0
        assert linear_interpolate(30.0, sample_data) == 60.0
        
    def test_mid_points(self, sample_data):
        assert linear_interpolate(15.0, sample_data) == 30.0
        assert linear_interpolate(25.0, sample_data) == 50.0
        
    def test_boundaries(self, sample_data):
        # Already covered by exact points but good to be explicit
        assert linear_interpolate(10.0, sample_data) == 20.0
        assert linear_interpolate(30.0, sample_data) == 60.0
        
    def test_out_of_bounds_low(self, sample_data):
        with pytest.raises(InvalidEngineeringInputError, match="Extrapolation is strictly not permitted"):
            linear_interpolate(9.9, sample_data)
            
    def test_out_of_bounds_high(self, sample_data):
        with pytest.raises(InvalidEngineeringInputError, match="Extrapolation is strictly not permitted"):
            linear_interpolate(30.1, sample_data)
            
    def test_invalid_dataset_not_enough_points(self):
        with pytest.raises(ValueError, match="at least two data points"):
            linear_interpolate(10.0, [(10.0, 20.0)])
            
    def test_invalid_dataset_unsorted(self):
        unsorted_data = [(20.0, 40.0), (10.0, 20.0), (30.0, 60.0)]
        with pytest.raises(ValueError, match="strictly increasing in x"):
            linear_interpolate(15.0, unsorted_data)
