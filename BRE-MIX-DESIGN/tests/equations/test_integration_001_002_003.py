import pytest
import math
import os
from src.bre_engine.calculations.eq_bre_001 import calculate_target_mean_strength
from src.bre_engine.calculations.lkp_bre_001 import determine_water_cement_ratio
from src.bre_engine.calculations.eq_bre_003 import determine_cement_content
from src.bre_engine.data.json_provider import JsonEngineeringDataProvider
from src.bre_engine.trace.tracker import TraceTracker

class MockTableProvider(JsonEngineeringDataProvider):
    def get_table_value(self, table_id: str, **kwargs):
        if table_id == "TBL-BRE-002":
            return 42.0
        return super().get_table_value(table_id, **kwargs)

class TestIntegration001002003:
    def test_br331_example_1_stage_1_to_3(self):
        """
        Tests the complete chain:
        EQ-BRE-001 -> presentation rounding -> LKP-BRE-001 -> EQ-BRE-003
        Using Example 1 values against the actual VERIFIED JSON dataset.
        """
        tracker = TraceTracker()
        
        # We need the real data directory
        data_dir = os.path.join(
            os.path.dirname(__file__), 
            "..", "..", "04_ENGINEERING_DATA"
        )
        provider = MockTableProvider(data_dir=data_dir)
        
        # Example 1: f_ck = 30, Margin = 11.6 (2.33 * 5, but for test simplicity we inject margin pieces)
        # Actually in BR 331 Example 1: Target mean strength = 30 + 11.6 = 41.6, wait.
        # Wait, Example 1 in BR 331 says:
        # 1.1 Specified strength: 30
        # 1.3 Margin: 16 (from table or specified). Oh, Example 1 has margin = 16.
        # 1.4 Target mean strength = 30 + 16 = 46.
        
        # 1. Stage 1 (EQ-BRE-001) calculates exact fm
        fm = calculate_target_mean_strength(f_ck=30.0, s_design=8.0, k=2.0, tracker=tracker)
        assert math.isclose(fm, 46.0)
        
        # Internal engine shouldn't prematurely round, but presentation form rounds to nearest integer.
        # So we pass 46.0 which is exactly 46.
        
        # 2. Stage 2 (LKP-BRE-001) lookup W/C
        # Cement class 42.5, Uncrushed => Datum = 42
        wc = determine_water_cement_ratio(
            f_m=46.0, 
            cement_strength_class="42.5", 
            aggregate_type="Uncrushed", 
            provider=provider,
            tracker=tracker
        )
        
        # Check that it interpolates between datum 40 and 50 using actual Figure 4 JSON curves.
        # Datum 40 at 46 requires extrapolation? No, datum 42 is between 40 and 50.
        # Target = 46.
        assert abs(wc - 0.47) <= 0.02
        
        # 3. Stage 3 (EQ-BRE-003) calculates cement content
        # Example 1 specifies Free Water = 160
        result = determine_cement_content(
            free_water_content=160.0,
            wc_ratio=wc,
            tracker=tracker
        )
        
        cement = result["cement_content"]
        # Exact mathematical result 160 / ~0.47
        assert math.isclose(cement, 160 / wc)
        # Verify it maps near to the ~340 printed in the presentation form
        assert 330.0 <= cement <= 350.0
        
        # Check that the max W/C logic was available but not triggered for Example 1
        assert result["modified_wc_ratio"] is None
