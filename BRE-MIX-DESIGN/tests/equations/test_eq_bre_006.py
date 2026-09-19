import pytest
from src.bre_engine.calculations.eq_bre_006 import determine_coarse_aggregate_content
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError

class TestEQBRE006:
    
    def test_invalid_inputs(self):
        # Negative / zero total aggregate
        with pytest.raises(InvalidEngineeringInputError, match="Total aggregate content must be greater than 0"):
            determine_coarse_aggregate_content(total_aggregate_content=0, fine_aggregate_content=500)
            
        # Negative / zero fine aggregate
        with pytest.raises(InvalidEngineeringInputError, match="Fine aggregate content must be greater than 0"):
            determine_coarse_aggregate_content(total_aggregate_content=2000, fine_aggregate_content=-100)
            
        # Fine aggregate greater than total aggregate
        with pytest.raises(InvalidEngineeringInputError, match="cannot be greater than or equal to total"):
            determine_coarse_aggregate_content(total_aggregate_content=2000, fine_aggregate_content=2100)
            
        # Fine aggregate equal to total aggregate
        with pytest.raises(InvalidEngineeringInputError, match="cannot be greater than or equal to total"):
            determine_coarse_aggregate_content(total_aggregate_content=2000, fine_aggregate_content=2000)
            
    def test_nominal_calculation_exact(self):
        # Exact arithmetic check matching Example 1 (unrounded mathematical internals)
        # Total = 1900, Fine = 1900 * 0.27 = 513
        result = determine_coarse_aggregate_content(
            total_aggregate_content=1900,
            fine_aggregate_content=513
        )
        assert pytest.approx(result["coarse_aggregate_content"], 0.1) == 1387.0
        
    def test_nominal_calculation_presentation_values(self):
        # If we fed it the final presentation-rounded values (as seen in BR 331 Table 4)
        # Total = 1900, Fine = 515 (rounded to nearest 5kg)
        result = determine_coarse_aggregate_content(
            total_aggregate_content=1900,
            fine_aggregate_content=515
        )
        assert pytest.approx(result["coarse_aggregate_content"], 0.1) == 1385.0
