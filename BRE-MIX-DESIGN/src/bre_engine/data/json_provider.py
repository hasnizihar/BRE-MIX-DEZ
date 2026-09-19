import os
import json
from typing import Any
from src.bre_engine.data.provider import EngineeringDataProvider
from src.bre_engine.errors.exceptions import EngineeringDataUnavailableError

class JsonEngineeringDataProvider(EngineeringDataProvider):
    def __init__(self, data_dir: str = "04_ENGINEERING_DATA"):
        self.data_dir = data_dir
        
    def _load_json(self, relative_path: str) -> dict:
        full_path = os.path.join(self.data_dir, relative_path)
        if not os.path.exists(full_path):
            raise EngineeringDataUnavailableError(
                data_id=relative_path,
                source="BR 331",
                calculation="N/A",
                message=f"Dataset {relative_path} is missing."
            )
        with open(full_path, 'r') as f:
            return json.load(f)

    def get_constant(self, constant_id: str) -> float:
        raise NotImplementedError()
        
    def get_table_value(self, table_id: str, **kwargs) -> Any:
        raise NotImplementedError()
        
    def get_graph_value(self, graph_id: str, x_value: float, **kwargs) -> float:
        raise NotImplementedError()
        
    def get_figure_3_data(self) -> dict:
        data = self._load_json(os.path.join("GRAPHS", "FIGURE_03", "figure_03_points.json"))
        if data.get("status") != "VERIFIED":
            raise EngineeringDataUnavailableError(
                data_id="DATA-004",
                source="BR 331",
                calculation="Figure 3 lookup",
                message="Figure 3 numerical dataset is strictly pending engineering verification."
            )
        return data
        
    def get_figure_4_data(self) -> list:
        data = self._load_json(os.path.join("GRAPHS", "FIGURE_04", "figure_04_points.json"))
        if data.get("status") != "VERIFIED":
            raise EngineeringDataUnavailableError(
                data_id="DATA-001 (Figure 4)",
                source="BR 331",
                calculation="Determine W/C ratio",
                message="Figure 4 numerical dataset is strictly pending engineering verification."
            )
        return data["curves"]
        
    def get_figure_5_data(self) -> list:
        data = self._load_json(os.path.join("GRAPHS", "FIGURE_05", "figure_05_points.json"))
        if data.get("status") != "VERIFIED":
            raise EngineeringDataUnavailableError(
                data_id="DATA-002 (Figure 5)",
                source="BR 331",
                calculation="Determine Wet Density",
                message="Figure 5 numerical dataset is strictly pending engineering verification."
            )
        return data["curves"]
        
    def get_figure_6_data(self) -> dict:
        raise NotImplementedError()
        
    def get_standard_deviation(self, condition: str) -> float:
        raise NotImplementedError()
