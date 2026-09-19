"""
MVP Engineering QA Suite

Tests categories A-F from Plan 2.08:
A. Valid input
B. Missing required input
C. Impossible values
D. Figure 4 boundaries
E. Figure 5 boundaries
F. Figure 6 absence
"""
import pytest
import os
from src.bre_engine.pipeline import BRECalculationEngine
from src.bre_engine.data.json_provider import JsonEngineeringDataProvider
from src.bre_engine.models.domain import (
    MixDesignInput, ConcreteRequirements, CementProperties, AggregateProperties,
)
from src.bre_engine.errors.exceptions import (
    InvalidEngineeringInputError,
    EngineeringConstraintError,
    EngineeringDataUnavailableError,
)
from src.bre_engine.interpolation.graph_2d import Graph2DInterpolator
from src.bre_engine.interpolation.curve_family import CurveFamilyInterpolator
import json


class MVPProvider(JsonEngineeringDataProvider):
    TABLE_2 = {
        ("32.5", "Uncrushed"): 22, ("32.5", "Crushed"): 30,
        ("42.5", "Uncrushed"): 42, ("42.5", "Crushed"): 49,
        ("52.5", "Uncrushed"): 49, ("52.5", "Crushed"): 56,
    }
    def get_table_value(self, table_id, **kwargs):
        if table_id == "TBL-BRE-002":
            key = (kwargs.get("cement_strength_class"), kwargs.get("aggregate_type"))
            val = self.TABLE_2.get(key)
            if val is None:
                raise InvalidEngineeringInputError(f"No Table 2 entry for {key}")
            return val
        raise NotImplementedError(f"Table {table_id} not implemented")


def make_engine():
    data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "04_ENGINEERING_DATA")
    return BRECalculationEngine(data_provider=MVPProvider(data_dir=data_dir))


def make_valid_input(**overrides):
    concrete_kw = dict(
        characteristic_strength=30.0,
        proportion_defective=5.0,
        age_days=28,
        slump_class="Slump_10_30",
    )
    cement_kw = dict(cement_type="CEM_I", strength_class="42.5")
    agg_kw = dict(
        max_aggregate_size=20,
        fine_aggregate_type="Uncrushed",
        coarse_aggregate_type="Uncrushed",
        fine_aggregate_rd=2.6, coarse_aggregate_rd=2.6,
        percentage_passing_600=27.0,
    )
    for k, v in overrides.items():
        if k in concrete_kw: concrete_kw[k] = v
        elif k in cement_kw: cement_kw[k] = v
        elif k in agg_kw: agg_kw[k] = v
    return MixDesignInput(
        project_id="QA_TEST",
        concrete=ConcreteRequirements(**concrete_kw),
        cement=CementProperties(**cement_kw),
        aggregate=AggregateProperties(**agg_kw),
        standard_deviation_override=overrides.get("standard_deviation_override", 8.0),
    )


# ═══════════════════════════════════════════════
# A. Valid Input
# ═══════════════════════════════════════════════
class TestA_ValidInput:
    def test_standard_example_succeeds(self):
        engine = make_engine()
        result = engine.calculate(make_valid_input())
        assert result.target_mean_strength > 0
        assert result.water_cement_ratio > 0
        assert result.cement_content > 0
        assert result.total_aggregate > 0
        assert result.fine_aggregate > 0
        assert result.coarse_aggregate > 0
        
    def test_all_cement_classes(self):
        engine = make_engine()
        for cls in ["32.5", "42.5", "52.5"]:
            result = engine.calculate(make_valid_input(strength_class=cls))
            assert result.cement_content > 0

    def test_crushed_aggregate(self):
        engine = make_engine()
        result = engine.calculate(make_valid_input(
            coarse_aggregate_type="Crushed",
            fine_aggregate_type="Crushed",
            fine_aggregate_rd=2.7, coarse_aggregate_rd=2.7,
        ))
        assert result.cement_content > 0


# ═══════════════════════════════════════════════
# B. Missing Required Input
# ═══════════════════════════════════════════════
class TestB_MissingInput:
    def test_missing_characteristic_strength_rejected(self):
        with pytest.raises(Exception):
            MixDesignInput(
                project_id="QA",
                concrete=ConcreteRequirements(
                    characteristic_strength=None,  # Missing
                    proportion_defective=5.0,
                    age_days=28,
                    slump_class="Slump_10_30",
                ),
                cement=CementProperties(cement_type="CEM_I", strength_class="42.5"),
                aggregate=AggregateProperties(
                    max_aggregate_size=20,
                    fine_aggregate_type="Uncrushed", coarse_aggregate_type="Uncrushed",
                    percentage_passing_600=27.0,
                ),
            )


# ═══════════════════════════════════════════════
# C. Impossible Values
# ═══════════════════════════════════════════════
class TestC_ImpossibleValues:
    def test_negative_strength_rejected(self):
        with pytest.raises(Exception):
            make_valid_input(characteristic_strength=-10.0)

    def test_zero_strength_rejected(self):
        with pytest.raises(Exception):
            make_valid_input(characteristic_strength=0)

    def test_fine_proportion_over_100_rejected(self):
        with pytest.raises(Exception):
            make_valid_input(percentage_passing_600=120.0)

    def test_negative_aggregate_size_rejected(self):
        with pytest.raises(Exception):
            make_valid_input(max_aggregate_size=-5)

    def test_unsupported_defective_percentage(self):
        engine = make_engine()
        with pytest.raises(InvalidEngineeringInputError, match="Unsupported proportion defective"):
            engine.calculate(make_valid_input(proportion_defective=7.0))


# ═══════════════════════════════════════════════
# D. Figure 4 Boundaries
# ═══════════════════════════════════════════════
class TestD_Figure4Boundaries:
    def _get_fig4_interpolator(self):
        file_path = os.path.join(
            os.path.dirname(__file__), "..", "..", 
            "04_ENGINEERING_DATA", "GRAPHS", "FIGURE_04", "figure_04_points.json"
        )
        with open(file_path) as f:
            data = json.load(f)
        return CurveFamilyInterpolator(data["curves"])

    def test_all_verified_datums_produce_result(self):
        interp = self._get_fig4_interpolator()
        for datum in [3, 7, 13, 20, 30, 40, 50, 60, 70]:
            wc = interp.find_x_for_y(target_y=float(datum), datum_y=float(datum))
            assert 0.3 <= wc <= 0.9, f"datum={datum} produced wc={wc}"

    def test_extrapolation_below_datum_3_blocked(self):
        interp = self._get_fig4_interpolator()
        with pytest.raises(Exception):
            interp.find_x_for_y(target_y=1.0, datum_y=1.0)

    def test_extrapolation_above_datum_70_blocked(self):
        interp = self._get_fig4_interpolator()
        with pytest.raises(Exception):
            interp.find_x_for_y(target_y=95.0, datum_y=95.0)


# ═══════════════════════════════════════════════
# E. Figure 5 Boundaries
# ═══════════════════════════════════════════════
class TestE_Figure5Boundaries:
    def _get_fig5_interpolator(self):
        file_path = os.path.join(
            os.path.dirname(__file__), "..", "..", 
            "04_ENGINEERING_DATA", "GRAPHS", "FIGURE_05", "figure_05_points.json"
        )
        with open(file_path) as f:
            data = json.load(f)
        return Graph2DInterpolator(data, allow_synthetic=False)

    def test_valid_range_produces_result(self):
        interp = self._get_fig5_interpolator()
        for rd in [2.4, 2.5, 2.6, 2.7, 2.8, 2.9]:
            wd = interp.interpolate(x_value=180.0, curve_value=rd)
            assert 2100 <= wd <= 2700, f"rd={rd} produced wd={wd}"

    def test_extrapolation_below_rd_2_4_blocked(self):
        interp = self._get_fig5_interpolator()
        with pytest.raises(EngineeringConstraintError):
            interp.interpolate(x_value=180.0, curve_value=2.3)

    def test_extrapolation_above_rd_2_9_blocked(self):
        interp = self._get_fig5_interpolator()
        with pytest.raises(EngineeringConstraintError):
            interp.interpolate(x_value=180.0, curve_value=3.0)

    def test_extrapolation_below_water_140_blocked(self):
        interp = self._get_fig5_interpolator()
        with pytest.raises(EngineeringConstraintError):
            interp.interpolate(x_value=100.0, curve_value=2.6)

    def test_extrapolation_above_water_240_blocked(self):
        interp = self._get_fig5_interpolator()
        with pytest.raises(EngineeringConstraintError):
            interp.interpolate(x_value=260.0, curve_value=2.6)


# ═══════════════════════════════════════════════
# F. Figure 6 Absence
# ═══════════════════════════════════════════════
class TestF_Figure6Absence:
    def test_figure_6_data_marked_pending(self):
        """The system must not silently invent fine aggregate percentages."""
        file_path = os.path.join(
            os.path.dirname(__file__), "..", "..", 
            "04_ENGINEERING_DATA", "GRAPHS", "FIGURE_06"
        )
        # Figure 6 directory may or may not exist
        if os.path.isdir(file_path):
            json_path = os.path.join(file_path, "figure_06_points.json")
            if os.path.exists(json_path):
                with open(json_path) as f:
                    data = json.load(f)
                # It must NOT be marked VERIFIED yet
                assert data.get("status") != "VERIFIED", \
                    "Figure 6 should not be VERIFIED — it has not been digitized from source"

    def test_json_provider_figure_6_not_available(self):
        """Calling get_figure_6_data must raise NotImplementedError or DataUnavailable."""
        data_dir = os.path.join(
            os.path.dirname(__file__), "..", "..", "04_ENGINEERING_DATA"
        )
        provider = MVPProvider(data_dir=data_dir)
        with pytest.raises((NotImplementedError, EngineeringDataUnavailableError)):
            provider.get_figure_6_data()

    def test_pipeline_requires_user_supplied_fine_proportion(self):
        """The pipeline must accept fine aggregate % as user input since Figure 6 is unavailable."""
        engine = make_engine()
        # Should succeed with user-supplied proportion
        result = engine.calculate(make_valid_input(percentage_passing_600=35.0))
        assert result.fine_aggregate > 0
