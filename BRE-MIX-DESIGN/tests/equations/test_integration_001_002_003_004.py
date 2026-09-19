import pytest
import os
import math
from src.bre_engine.trace.tracker import TraceTracker
from src.bre_engine.calculations.eq_bre_001 import calculate_target_mean_strength
from src.bre_engine.calculations.lkp_bre_001 import determine_water_cement_ratio
from src.bre_engine.calculations.eq_bre_003 import determine_cement_content
from src.bre_engine.calculations.lkp_bre_002 import determine_wet_density
from src.bre_engine.calculations.eq_bre_004 import determine_total_aggregate_content
from src.bre_engine.data.json_provider import JsonEngineeringDataProvider

class MockTableProvider(JsonEngineeringDataProvider):
    def get_table_value(self, table_id: str, **kwargs):
        if table_id == "TBL-BRE-002":
            return 42
        return super().get_table_value(table_id, **kwargs)

class TestIntegrationStage1To4:
    def test_br331_example_1_stage_1_to_4(self):
        """
        Tests the complete chain:
        Target Mean Strength -> W/C Ratio -> Cement Content -> Wet Density -> Total Aggregate
        """
        tracker = TraceTracker()
        data_dir = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "04_ENGINEERING_DATA"
        )
        provider = MockTableProvider(data_dir=data_dir)
        
        # 1. Stage 1 (EQ-BRE-001) calculates exact fm
        fm = calculate_target_mean_strength(f_ck=30.0, s_design=8.0, k=2.0, tracker=tracker)
        assert math.isclose(fm, 46.0)
        
        # 2. Stage 2 (LKP-BRE-001) lookup W/C
        wc = determine_water_cement_ratio(
            f_m=46.0,
            cement_strength_class="42.5",
            aggregate_type="Uncrushed",
            provider=provider,
            tracker=tracker
        )
        assert abs(wc - 0.47) <= 0.02
        
        # 3. Stage 3 (EQ-BRE-003) calculates cement content
        # Example 1 specifies Free Water = 160
        result_3 = determine_cement_content(
            free_water_content=160.0,
            wc_ratio=wc,
            tracker=tracker
        )
        cement = result_3["cement_content"]
        assert 330.0 <= cement <= 350.0
        
        # 4. Stage 4 (LKP-BRE-002) determines wet density from Figure 5
        wet_density = determine_wet_density(
            free_water_content=160.0,
            relative_density=2.6,
            provider=provider,
            tracker=tracker
        )
        assert wet_density == 2400.0
        
        # 5. Stage 4 (EQ-BRE-004) calculates total aggregate content
        result_4 = determine_total_aggregate_content(
            wet_density=wet_density,
            cement_content=cement,
            free_water_content=160.0,
            tracker=tracker
        )
        total_aggregate = result_4["total_aggregate_content"]
        
        # Expected is 1900. Since cement varies from 330 to 350, aggregate will vary from 1890 to 1910
        assert 1890.0 <= total_aggregate <= 1910.0
