import pytest
import math
from src.bre_engine.calculations.lkp_bre_002 import determine_wet_density
from src.bre_engine.data.json_provider import JsonEngineeringDataProvider
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError, EngineeringConstraintError
from src.bre_engine.trace.tracker import TraceTracker
import os

class MockFigure5Provider(JsonEngineeringDataProvider):
    """
    Returns actual Figure 5 curves without needing the full framework.
    """
    def __init__(self):
        super().__init__(data_dir=os.path.join(os.path.dirname(__file__), "..", "..", "04_ENGINEERING_DATA"))
        
def test_lkp_bre_002_valid():
    provider = MockFigure5Provider()
    tracker = TraceTracker()
    
    # 2.6 at 160 should be 2400
    wet_density = determine_wet_density(
        free_water_content=160.0,
        relative_density=2.6,
        provider=provider,
        tracker=tracker
    )
    
    assert wet_density == 2400.0
    
    # Check trace
    trace = tracker.get_trace()
    assert trace.steps[0].step_id == "LKP-BRE-002"
    assert trace.steps[0].inputs["free_water_content"] == 160.0
    
def test_lkp_bre_002_invalid_inputs():
    provider = MockFigure5Provider()
    
    with pytest.raises(InvalidEngineeringInputError):
        determine_wet_density(-10, 2.6, provider)
        
    with pytest.raises(InvalidEngineeringInputError):
        determine_wet_density(160, -2.6, provider)
