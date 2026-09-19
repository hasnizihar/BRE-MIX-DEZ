import pytest
from src.bre_engine.calculations.eq_bre_002 import calculate_margin
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError, EngineeringDataUnavailableError
from src.bre_engine.trace.tracker import TraceTracker
from src.bre_engine.data.provider import EngineeringDataProvider

class MockDataProvider(EngineeringDataProvider):
    def get_constant(self, constant_id: str) -> float:
        pass
        
    def get_table_value(self, table_id: str, **kwargs):
        pass
        
    def get_graph_value(self, graph_id: str, x_value: float, **kwargs) -> float:
        pass
        
    def get_figure_3_data(self) -> dict:
        return {}
        
    def get_figure_4_data(self) -> list:
        return []
        
    def get_figure_5_data(self) -> dict:
        return {}
        
    def get_figure_6_data(self) -> dict:
        return {}
        
    def get_standard_deviation(self, condition: str) -> float:
        if condition == "n < 20":
            raise EngineeringDataUnavailableError(
                data_id="DATA-004",
                source="BR 331",
                calculation="EQ-BRE-002",
                message="Standard deviation for n < 20 is pending engineering review."
            )
        return 8.0  # mock value for >= 20

class TestEQBRE002:
    """Test suite for EQ-BRE-002 (Statistical Margin)."""
    
    def test_normal_case(self):
        """Test with typical known valid inputs."""
        # k = 1.64 (e.g. 5% defective), s = 5.0
        m = calculate_margin(k=1.64, s=5.0)
        assert m == 8.2
        
    def test_boundary_zero_sd(self):
        """Test boundary condition (s = 0)."""
        m = calculate_margin(k=1.64, s=0.0)
        assert m == 0.0
        
    def test_invalid_negative_k(self):
        """k must be > 0."""
        with pytest.raises(InvalidEngineeringInputError, match="k must be > 0"):
            calculate_margin(k=-1.64, s=5.0)
            
    def test_invalid_zero_k(self):
        """k must be > 0."""
        with pytest.raises(InvalidEngineeringInputError, match="k must be > 0"):
            calculate_margin(k=0.0, s=5.0)
            
    def test_invalid_negative_sd(self):
        """Standard deviation must be >= 0."""
        with pytest.raises(InvalidEngineeringInputError, match="Standard deviation \\(s\\) must be >= 0"):
            calculate_margin(k=1.64, s=-2.0)
            
    def test_missing_data_004(self):
        """
        Simulate pipeline attempting to fetch standard deviation when n < 20.
        Must raise EngineeringDataUnavailableError with DATA-004.
        """
        provider = MockDataProvider()
        
        with pytest.raises(EngineeringDataUnavailableError) as exc_info:
            # Pipeline simulates fetching standard deviation first
            s = provider.get_standard_deviation(condition="n < 20")
            calculate_margin(k=1.64, s=s)
            
        assert exc_info.value.data_id == "DATA-004"
        
    def test_trace_tracking(self):
        """Test that the equation correctly logs to the trace tracker."""
        tracker = TraceTracker()
        
        m = calculate_margin(k=1.64, s=5.0, tracker=tracker)
        
        trace = tracker.get_trace()
        assert len(trace.steps) == 1
        
        step = trace.steps[0]
        assert step.step_id == "EQ-BRE-002"
        assert step.source_id == "SRC-BRE-001"
        assert step.inputs["k"] == 1.64
        assert step.inputs["s"] == 5.0
        assert step.output == 8.2
