import pytest
import math
from src.bre_engine.calculations.eq_bre_003 import determine_cement_content
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError, EngineeringConstraintError

def test_eq_bre_003_example_1():
    """
    Test exact Example 1 values from BR 331 Table 4.
    W = 160, W/C = 0.47
    C = 160 / 0.47 = 340.4255...
    """
    result = determine_cement_content(free_water_content=160.0, wc_ratio=0.47)
    
    # Do not prematurely round the internal calculation
    assert math.isclose(result["cement_content"], 340.4255319148936)
    assert result["modified_wc_ratio"] is None

def test_eq_bre_003_basic_arithmetic():
    """
    Test basic arithmetic W=160, W/C=0.50 -> C=320
    """
    result = determine_cement_content(free_water_content=160.0, wc_ratio=0.50)
    assert math.isclose(result["cement_content"], 320.0)
    assert result["modified_wc_ratio"] is None

def test_eq_bre_003_invalid_wc_zero():
    """W/C = 0 must fail."""
    with pytest.raises(InvalidEngineeringInputError, match="must be greater than 0"):
        determine_cement_content(free_water_content=160.0, wc_ratio=0.0)

def test_eq_bre_003_invalid_wc_negative():
    """W/C < 0 must fail."""
    with pytest.raises(InvalidEngineeringInputError, match="must be greater than 0"):
        determine_cement_content(free_water_content=160.0, wc_ratio=-0.5)

def test_eq_bre_003_invalid_water_negative():
    """Negative water must fail."""
    with pytest.raises(InvalidEngineeringInputError, match="must be greater than 0"):
        determine_cement_content(free_water_content=-160.0, wc_ratio=0.50)

def test_eq_bre_003_minimum_cement_rule():
    """
    Test that if calculated cement is below minimum, the minimum is adopted
    and W/C ratio is modified.
    Calculated = 160 / 0.8 = 200.
    Minimum = 250.
    Modified W/C = 160 / 250 = 0.64.
    """
    result = determine_cement_content(
        free_water_content=160.0, 
        wc_ratio=0.80, 
        min_cement_content=250.0
    )
    
    assert math.isclose(result["cement_content"], 250.0)
    assert result["modified_wc_ratio"] is not None
    assert math.isclose(result["modified_wc_ratio"], 0.64)

def test_eq_bre_003_maximum_cement_rule():
    """
    Test that if calculated cement exceeds max, an EngineeringConstraintError is raised.
    Calculated = 160 / 0.3 = 533.33...
    Maximum = 400.
    """
    with pytest.raises(EngineeringConstraintError, match="exceeds specified maximum"):
        determine_cement_content(
            free_water_content=160.0, 
            wc_ratio=0.30, 
            max_cement_content=400.0
        )
