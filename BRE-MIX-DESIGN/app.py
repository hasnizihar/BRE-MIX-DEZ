"""
BRE Mix Design MVP - Web API Server

A simple Flask server that exposes the BRE calculation engine
as both a web UI and a JSON API.
"""
import os
import sys
import json
import math

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template, request, jsonify
from src.bre_engine.pipeline import BRECalculationEngine
from src.bre_engine.data.json_provider import JsonEngineeringDataProvider
from src.bre_engine.models.domain import (
    MixDesignInput,
    ConcreteRequirements,
    CementProperties,
    AggregateProperties,
)
from src.bre_engine.errors.exceptions import (
    InvalidEngineeringInputError,
    EngineeringDataUnavailableError,
    EngineeringConstraintError,
)

app = Flask(__name__, template_folder="templates", static_folder="static")

# Provider with Table 2 mock for MVP
class MVPDataProvider(JsonEngineeringDataProvider):
    """
    MVP data provider that includes Table 2 datum lookup.
    """
    TABLE_2 = {
        # (cement_strength_class, aggregate_type) -> datum at W/C=0.5, 28 days
        ("32.5", "Uncrushed"): 22,
        ("32.5", "Crushed"): 30,
        ("42.5", "Uncrushed"): 42,
        ("42.5", "Crushed"): 49,
        ("52.5", "Uncrushed"): 49,
        ("52.5", "Crushed"): 56,
    }
    
    def get_table_value(self, table_id: str, **kwargs):
        if table_id == "TBL-BRE-002":
            key = (kwargs.get("cement_strength_class"), kwargs.get("aggregate_type"))
            val = self.TABLE_2.get(key)
            if val is None:
                raise InvalidEngineeringInputError(
                    f"No Table 2 entry for {key}"
                )
            return val
        raise NotImplementedError(f"Table {table_id} not implemented in MVP")


def create_engine():
    data_dir = os.path.join(os.path.dirname(__file__), "04_ENGINEERING_DATA")
    provider = MVPDataProvider(data_dir=data_dir)
    return BRECalculationEngine(data_provider=provider)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/calculate", methods=["POST"])
def calculate():
    try:
        data = request.get_json()
        
        mix_input = MixDesignInput(
            project_id=data.get("project_id", "MVP_CALCULATION"),
            concrete=ConcreteRequirements(
                characteristic_strength=float(data["characteristic_strength"]),
                proportion_defective=float(data.get("proportion_defective", 5.0)),
                age_days=int(data.get("age_days", 28)),
                slump_class=data["slump_class"],
                max_wc_ratio=float(data["max_wc_ratio"]) if data.get("max_wc_ratio") else None,
                min_cement_content=float(data["min_cement_content"]) if data.get("min_cement_content") else None,
            ),
            cement=CementProperties(
                cement_type=data.get("cement_type", "CEM_I"),
                strength_class=data["cement_strength_class"],
            ),
            aggregate=AggregateProperties(
                max_aggregate_size=int(data["max_aggregate_size"]),
                fine_aggregate_type=data.get("fine_aggregate_type", "Uncrushed"),
                coarse_aggregate_type=data.get("coarse_aggregate_type", "Uncrushed"),
                fine_aggregate_rd=float(data.get("relative_density", 2.6)),
                coarse_aggregate_rd=float(data.get("relative_density", 2.6)),
                percentage_passing_600=float(data.get("fine_aggregate_proportion", 27.0)),
            ),
            standard_deviation_override=float(data["standard_deviation"]) if data.get("standard_deviation") else None,
        )
        
        engine = create_engine()
        result = engine.calculate(mix_input)
        
        # Build trace data
        trace_data = []
        for step in result.trace.steps:
            trace_data.append({
                "step_id": step.step_id,
                "description": step.description,
                "inputs": _serialize(step.inputs),
                "equation": step.equation_or_table,
                "source": step.source_id,
                "output": _serialize(step.output),
                "warnings": step.warnings,
            })
        
        # Round presentation values
        return jsonify({
            "success": True,
            "result": {
                "target_mean_strength": round(result.target_mean_strength, 1),
                "water_cement_ratio": round(result.water_cement_ratio, 2),
                "free_water_content": round(result.free_water_content),
                "cement_content": round(result.cement_content),
                "total_aggregate": round(result.total_aggregate),
                "fine_aggregate": _round_to_5(result.fine_aggregate),
                "coarse_aggregate": _round_to_5(result.coarse_aggregate),
                "raw": {
                    "target_mean_strength": float(result.target_mean_strength),
                    "water_cement_ratio": float(result.water_cement_ratio),
                    "cement_content": float(result.cement_content),
                    "total_aggregate": float(result.total_aggregate),
                    "fine_aggregate": float(result.fine_aggregate),
                    "coarse_aggregate": float(result.coarse_aggregate),
                },
            },
            "trace": trace_data,
        })
        
    except (InvalidEngineeringInputError, EngineeringConstraintError) as e:
        return jsonify({"success": False, "error": str(e), "type": "engineering"}), 400
    except EngineeringDataUnavailableError as e:
        return jsonify({"success": False, "error": str(e), "type": "data"}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e), "type": "internal"}), 500


def _round_to_5(value: float) -> int:
    """Round to nearest 5 kg as per BR 331 presentation rules."""
    return int(5 * round(value / 5))


def _serialize(obj):
    """Convert numpy types to native Python for JSON serialisation."""
    if isinstance(obj, dict):
        return {k: _serialize(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_serialize(v) for v in obj]
    if hasattr(obj, 'item'):  # numpy scalar
        return obj.item()
    return obj


if __name__ == "__main__":
    app.run(debug=True, port=5000)
