import pytest
from src.bre_engine.calculations.eq_bre_001 import calculate_target_mean_strength
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError

class TestEQBRE001:
    """Test suite for EQ-BRE-001 (Target Mean Strength)."""
    
    def test_normal_case(self):
        """Test with typical known valid inputs."""
        # Example: C30 concrete, 5.0 N/mm2 margin
        f_m = calculate_target_mean_strength(f_ck=30.0, m=5.0)
        assert f_m == 35.0
        
        # Example with decimal inputs
        f_m = calculate_target_mean_strength(f_ck=32.5, m=4.2)
        assert f_m == 36.7

    def test_rounding(self):
        """Test that the output is rounded to 1 decimal place."""
        f_m = calculate_target_mean_strength(f_ck=30.12, m=4.34)
        assert f_m == 34.5  # 34.46 -> 34.5
        
    def test_boundary_case(self):
        """Test boundary conditions (m = 0)."""
        # A mix with zero margin (rare, but mathematically valid for M >= 0)
        f_m = calculate_target_mean_strength(f_ck=30.0, m=0.0)
        assert f_m == 30.0
        
    def test_invalid_negative_fck(self):
        """f_ck must be > 0."""
        with pytest.raises(InvalidEngineeringInputError, match="f_ck must be > 0"):
            calculate_target_mean_strength(f_ck=-10.0, m=5.0)
            
    def test_invalid_zero_fck(self):
        """f_ck must be > 0."""
        with pytest.raises(InvalidEngineeringInputError, match="f_ck must be > 0"):
            calculate_target_mean_strength(f_ck=0.0, m=5.0)
            
    def test_invalid_negative_margin(self):
        """Margin must be >= 0."""
        with pytest.raises(InvalidEngineeringInputError, match="Margin \\(m\\) must be >= 0"):
            calculate_target_mean_strength(f_ck=30.0, m=-2.5)
    def test_trace_tracking(self):
        """Test that the equation correctly logs to the trace tracker."""
        from src.bre_engine.trace.tracker import TraceTracker
        
        tracker = TraceTracker()
        f_m = calculate_target_mean_strength(f_ck=30.0, m=5.0, tracker=tracker)
        
        trace = tracker.get_trace()
        assert len(trace.steps) == 1
        
        step = trace.steps[0]
        assert step.step_id == "EQ-BRE-001"
        assert step.source_id == "SRC-BRE-001"
        assert step.inputs["f_ck"] == 30.0
        assert step.output == 35.0
