import pytest
from src.bre_engine.calculations.eq_bre_005 import determine_fine_aggregate_content
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError

class TestEQBRE005:
    
    def test_invalid_inputs(self):
        with pytest.raises(InvalidEngineeringInputError, match="Total aggregate content must be greater than 0"):
            determine_fine_aggregate_content(total_aggregate_content=0, fine_aggregate_proportion_percentage=30.0)
            
        with pytest.raises(InvalidEngineeringInputError, match="between 0 and 100"):
            determine_fine_aggregate_content(total_aggregate_content=2000, fine_aggregate_proportion_percentage=0)
            
        with pytest.raises(InvalidEngineeringInputError, match="between 0 and 100"):
            determine_fine_aggregate_content(total_aggregate_content=2000, fine_aggregate_proportion_percentage=101)
            
    def test_nominal_calculation_example_1(self):
        # BR 331 Example 1 (Table 8 equivalent / or Table 7 if air entrained, but we found a standard example)
        # Actually in BR 331 Example 1 (Table 4 or Table 7): Total aggregate = 2150 (maybe), Proportion = 27%
        # Let's test 2150 and 27% -> 2150 * 0.27 = 580.5
        result = determine_fine_aggregate_content(
            total_aggregate_content=2150,
            fine_aggregate_proportion_percentage=27.0
        )
        assert pytest.approx(result["fine_aggregate_content"], 0.1) == 580.5
        
    def test_nominal_calculation_example_2(self):
        # Another standard mathematical check: 1850 total, 35% fines -> 1850 * 0.35 = 647.5
        result = determine_fine_aggregate_content(
            total_aggregate_content=1850,
            fine_aggregate_proportion_percentage=35.0
        )
        assert pytest.approx(result["fine_aggregate_content"], 0.1) == 647.5
        
    def test_boundary_proportion(self):
        # Allow 100% (though impractical for concrete)
        result = determine_fine_aggregate_content(
            total_aggregate_content=2000,
            fine_aggregate_proportion_percentage=100.0
        )
        assert result["fine_aggregate_content"] == 2000.0
