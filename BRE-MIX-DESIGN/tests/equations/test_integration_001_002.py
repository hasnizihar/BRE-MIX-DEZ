import pytest
import math
from src.bre_engine.calculations.eq_bre_001 import calculate_target_mean_strength
from src.bre_engine.calculations.lkp_bre_001 import determine_water_cement_ratio
from src.bre_engine.trace.tracker import TraceTracker

class MockLkpProvider:
    def get_table_value(self, **kwargs) -> float:
        return 42.0
    def get_figure_4_data(self) -> list:
        # Just return some dummy data to avoid errors
        return [
            {"cement_class": "42.5", "agg_type": "uncrushed", "datum_strength_at_05": 42.0, "points": [
                {"water_cement_ratio": 0.3, "strength": 62.0},
                {"water_cement_ratio": 0.5, "strength": 42.0}
            ]},
            {"cement_class": "42.5", "agg_type": "uncrushed", "datum_strength_at_05": 50.0, "points": [
                {"water_cement_ratio": 0.3, "strength": 70.0},
                {"water_cement_ratio": 0.5, "strength": 50.0}
            ]}
        ]

class TestIntegration001002:
    def test_integration_001_to_002(self):
        """
        Tests the sequence:
        fm = calculate_target_mean_strength
        M -> fm -> presentation_rounding -> determine_water_cement_ratio
        """
        tracker = TraceTracker()
        
        # 1. Stage 1 (EQ-BRE-001) calculates exact fm
        fm = calculate_target_mean_strength(f_ck=30.0, s_design=8.0, k=1.64, tracker=tracker)
        # fm = 30 + 1.64 * 8 = 43.12
        assert math.isclose(fm, 43.12)
        
        # Presentation rounding (round to nearest integer as required by BR 331)
        fm_rounded = round(fm)
        
        # 2. Stage 2 (EQ-BRE-002) takes fm_rounded
        provider = MockLkpProvider()
        wc = determine_water_cement_ratio(f_m=fm_rounded, cement_strength_class="42.5", aggregate_type="uncrushed", provider=provider)
        
        assert wc is not None
