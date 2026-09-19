import pytest
import math
from src.bre_engine.calculations.eq_bre_001 import calculate_target_mean_strength
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError

def test_eq_bre_001_exact_math():
    """Verify that M = k * s_design and fm = f_ck + M happens exactly without premature rounding."""
    # Example: M = 1.64 * 8.1 = 13.284
    # f_m = 30 + 13.284 = 43.284
    fm = calculate_target_mean_strength(f_ck=30.0, s_design=8.1, k=1.64)
    assert math.isclose(fm, 43.284)

def test_eq_bre_001_br_331_example_1():
    """
    Test using exact inputs from BR 331 Example 1 before any presentation rounding occurs.
    fc = 30 N/mm2, 5% defective (k=1.64), n < 20 (Line A = 8).
    M = 1.64 * 8 = 13.12
    fm = 30 + 13.12 = 43.12
    """
    fm = calculate_target_mean_strength(f_ck=30.0, s_design=8.0, k=1.64)
    assert math.isclose(fm, 43.12)
    # Note: Presentation rounding is expected to round M=13.12 -> 13, so fm -> 43, 
    # but the calculation module itself returns 43.12 exactly.

def test_invalid_fck():
    with pytest.raises(InvalidEngineeringInputError, match="must be > 0"):
        calculate_target_mean_strength(f_ck=0.0, s_design=8.0, k=1.64)

def test_invalid_s_design():
    with pytest.raises(InvalidEngineeringInputError, match="must be >= 0"):
        calculate_target_mean_strength(f_ck=30.0, s_design=-1.0, k=1.64)

def test_invalid_k():
    with pytest.raises(InvalidEngineeringInputError, match="must be > 0"):
        calculate_target_mean_strength(f_ck=30.0, s_design=8.0, k=0.0)
