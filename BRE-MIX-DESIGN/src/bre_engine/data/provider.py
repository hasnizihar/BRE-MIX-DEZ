from abc import ABC, abstractmethod
from typing import Any, Dict

class EngineeringDataProvider(ABC):
    """
    Abstract interface for retrieving verified BRE Mix Design engineering data.
    
    The engine must NOT hard-code engineering tables, constants, or graphs.
    Instead, it queries this provider. If data is marked [PENDING_USER_DATA],
    the provider must raise EngineeringDataUnavailableError.
    """
    
    @abstractmethod
    def get_constant(self, constant_id: str) -> float:
        """Retrieve an exact mathematical or physical constant."""
        pass
        
    @abstractmethod
    def get_table_value(self, table_id: str, **kwargs) -> Any:
        """
        Retrieve a discrete value from a lookup table.
        kwargs specifies the lookup keys (e.g., aggregate_size=20, aggregate_type="Crushed").
        """
        pass
        
    @abstractmethod
    def get_graph_value(self, graph_id: str, x_value: float, **kwargs) -> float:
        """
        Retrieve an interpolated value from a continuous graph relationship.
        """
        pass
        
    @abstractmethod
    def get_standard_deviation(self, condition: str) -> float:
        """
        Retrieve standard deviation guidance (STD-BRE-001) based on production conditions.
        """
        pass
