import pytest
import math
from src.bre_engine.calculations.standard_deviation import calculate_standard_deviation, select_design_standard_deviation
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError

class MockFig3Provider:
    def get_figure_3_data(self) -> dict:
        return {
            "line_a": [
                {"x": 0.0, "y": 4.0},
                {"x": 20.0, "y": 8.0},
                {"x": 100.0, "y": 8.0}
            ],
            "line_b": [
                {"x": 0.0, "y": 2.0},
                {"x": 20.0, "y": 4.0},
                {"x": 100.0, "y": 4.0}
            ]
        }

def test_calculate_standard_deviation():
    """Verify n-1 calculation matches statistical standard deviation."""
    results = [30.5, 32.1, 29.8, 31.2, 33.0]
    n = len(results)
    mean = sum(results) / n
    variance = sum((x - mean) ** 2 for x in results) / (n - 1)
    expected_s = math.sqrt(variance)
    
    assert math.isclose(calculate_standard_deviation(results), expected_s)

def test_calculate_standard_deviation_invalid_n():
    """Cannot calculate sample standard deviation with n < 2."""
    with pytest.raises(InvalidEngineeringInputError, match="At least 2 are required"):
        calculate_standard_deviation([30.0])

def test_select_design_s_n_less_than_20_fc_gt_20():
    """n < 20, fc >= 20 -> Line A (8.0)."""
    provider = MockFig3Provider()
    s = select_design_standard_deviation(f_ck=25.0, n_results=19, provider=provider)
    assert s == 8.0

def test_select_design_s_n_less_than_20_fc_lt_20():
    """n < 20, fc < 20 -> Line A slope (Y = 4 + 0.2*fc)."""
    provider = MockFig3Provider()
    s = select_design_standard_deviation(f_ck=10.0, n_results=19, provider=provider)
    assert s == 6.0 # 4 + 0.2*10 = 6.0

def test_select_design_s_n_ge_20_fc_gt_20_calculated_s_dominates():
    """n >= 20, calculated s > Line B -> Use calculated s."""
    provider = MockFig3Provider()
    # Line B for fc=30 is 4.0
    s = select_design_standard_deviation(f_ck=30.0, n_results=20, calculated_s=5.0, provider=provider)
    assert s == 5.0

def test_select_design_s_n_ge_20_fc_gt_20_line_b_dominates():
    """n >= 20, calculated s < Line B -> Use Line B."""
    provider = MockFig3Provider()
    # Line B for fc=30 is 4.0
    s = select_design_standard_deviation(f_ck=30.0, n_results=20, calculated_s=3.0, provider=provider)
    assert s == 4.0

def test_select_design_s_n_ge_20_fc_lt_20_line_b_dominates():
    """n >= 20, fc < 20. Line B is Y = 2 + 0.1*fc."""
    provider = MockFig3Provider()
    # Line B for fc=10 is 3.0
    s = select_design_standard_deviation(f_ck=10.0, n_results=25, calculated_s=2.0, provider=provider)
    assert s == 3.0

def test_select_design_s_n_ge_20_missing_s():
    provider = MockFig3Provider()
    with pytest.raises(InvalidEngineeringInputError, match="must be provided"):
        select_design_standard_deviation(f_ck=30.0, n_results=20, provider=provider)
