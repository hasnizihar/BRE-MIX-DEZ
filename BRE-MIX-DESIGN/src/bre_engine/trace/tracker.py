from typing import Any, Dict
from src.bre_engine.models.domain import CalculationTrace, CalculationStep

class TraceTracker:
    """Manages the lifecycle of a CalculationTrace during a mix design."""
    
    def __init__(self):
        self.trace = CalculationTrace()
        
    def add_step(self, step_id: str, description: str, inputs: Dict[str, Any], 
                 equation_or_table: str, source_id: str, output: Any, warnings: list = None):
        """Records a completed calculation step."""
        if warnings is None:
            warnings = []
            
        step = CalculationStep(
            step_id=step_id,
            description=description,
            inputs=inputs,
            equation_or_table=equation_or_table,
            source_id=source_id,
            output=output,
            warnings=warnings
        )
        self.trace.steps.append(step)
        
    def get_trace(self) -> CalculationTrace:
        return self.trace
