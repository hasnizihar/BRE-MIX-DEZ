import pytest
from src.bre_engine.calculations.lkp_bre_001 import determine_water_cement_ratio
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError, EngineeringDataUnavailableError
from src.bre_engine.data.provider import EngineeringDataProvider

class MockBlockedDataProvider(EngineeringDataProvider):
    """Mocks a data provider where Figure 4 (DATA-001) is strictly blocked/missing."""
    
    def get_constant(self, constant_id: str) -> float:
        pass
        
    def get_table_value(self, table_id: str, **kwargs):
        if table_id == "TBL-BRE-002":
            return 49.0
        return 0.0
        
    def get_graph_value(self, graph_id: str, x_value: float, **kwargs) -> float:
        pass
        
    def get_figure_3_data(self) -> dict:
        return {}
        
    def get_figure_4_data(self) -> list:
        raise EngineeringDataUnavailableError(
            data_id="DATA-001 (Figure 4)",
            source="BR 331",
            calculation="Determine W/C ratio",
            message="Figure 4 numerical dataset is strictly pending engineering verification."
        )
        
    def get_figure_5_data(self) -> dict:
        return {}
        
    def get_figure_6_data(self) -> dict:
        return {}
        
    def get_standard_deviation(self, condition: str) -> float:
        pass

class MockValidCurveProvider(EngineeringDataProvider):
    """Mocks a data provider with valid curve data."""
    
    def get_constant(self, constant_id: str) -> float:
        pass
        
    def get_table_value(self, table_id: str, **kwargs):
        if table_id == "TBL-BRE-002":
            return 42.0
        return 0.0
        
    def get_graph_value(self, graph_id: str, x_value: float, **kwargs) -> float:
        pass
        
    def get_figure_3_data(self) -> dict:
        return {}
        
    def get_figure_4_data(self) -> list:
        return [
            {
                "datum_strength_at_05": 40.0,
                "points": [
                    {"water_cement_ratio": 0.3, "strength": 59.0},
                    {"water_cement_ratio": 0.4, "strength": 51.0},
                    {"water_cement_ratio": 0.5, "strength": 40.0},
                    {"water_cement_ratio": 0.6, "strength": 30.5},
                    {"water_cement_ratio": 0.7, "strength": 23.5}
                ]
            },
            {
                "datum_strength_at_05": 50.0,
                "points": [
                    {"water_cement_ratio": 0.3, "strength": 70.0},
                    {"water_cement_ratio": 0.4, "strength": 62.0},
                    {"water_cement_ratio": 0.5, "strength": 50.0},
                    {"water_cement_ratio": 0.6, "strength": 39.0},
                    {"water_cement_ratio": 0.7, "strength": 30.0}
                ]
            }
        ]
        
    def get_figure_5_data(self) -> dict:
        return {}
        
    def get_figure_6_data(self) -> dict:
        return {}
        
    def get_standard_deviation(self, condition: str) -> float:
        pass

class TestLKPBRE001:
    
    def test_invalid_negative_fm(self):
        """Target mean strength must be > 0."""
        provider = MockBlockedDataProvider()
        with pytest.raises(InvalidEngineeringInputError, match="Target mean strength f_m must be > 0"):
            determine_water_cement_ratio(f_m=-5.0, cement_strength_class="42.5", aggregate_type="Crushed", provider=provider)
            
    def test_determine_water_cement_ratio_example_1(self):
        """
        Verify against BR 331 Example 1 (Table 4).
        Datum (from Table 2) = 42 N/mm2. Target Mean Strength (f_m) = 46 N/mm2.
        Output W/C should be 0.47.
        """
        provider = MockValidCurveProvider()
        
        wc_ratio = determine_water_cement_ratio(
            f_m=46.0,
            cement_strength_class="42.5",
            aggregate_type="Uncrushed",
            provider=provider
        )
        assert pytest.approx(wc_ratio, abs=0.01) == 0.47
        
    def test_max_wc_ratio_capping(self):
        provider = MockValidCurveProvider()
        
        # Target 30, datum 42 => W/C is ~0.63
        # We cap it at 0.55
        wc_ratio = determine_water_cement_ratio(
            f_m=30.0,
            cement_strength_class="42.5",
            aggregate_type="Uncrushed",
            provider=provider,
            max_wc_ratio=0.55
        )
        assert wc_ratio == 0.55
        
    def test_max_wc_ratio_no_cap_needed(self):
        provider = MockValidCurveProvider()
        
        # Target 40, datum 42 => W/C is ~0.52
        # Cap is 0.55, so it shouldn't be capped
        wc_ratio = determine_water_cement_ratio(
            f_m=40.0,
            cement_strength_class="42.5",
            aggregate_type="Uncrushed",
            provider=provider,
            max_wc_ratio=0.55
        )
        assert pytest.approx(wc_ratio, abs=0.01) == 0.52
        
    def test_missing_data_001(self):
        """
        Verify that missing DATA-001 raises the correct EngineeringDataUnavailableError,
        preventing the calculation from proceeding with invented data.
        """
        provider = MockBlockedDataProvider()
        
        with pytest.raises(EngineeringDataUnavailableError) as exc_info:
            determine_water_cement_ratio(f_m=45.0, cement_strength_class="42.5", aggregate_type="Crushed", provider=provider)
            
        assert exc_info.value.data_id == "DATA-001 (Figure 4)"
