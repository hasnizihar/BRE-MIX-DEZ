from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field

# -----------------------------------------------------------------------------
# TRACEABILITY MODELS
# -----------------------------------------------------------------------------
class CalculationStep(BaseModel):
    """Represents a single traceable calculation step."""
    step_id: str
    description: str
    inputs: Dict[str, Any]
    equation_or_table: str
    source_id: str
    output: Any
    warnings: List[str] = Field(default_factory=list)

class CalculationTrace(BaseModel):
    """A complete trace of all calculations performed during a mix design."""
    steps: List[CalculationStep] = Field(default_factory=list)

class EngineeringWarning(BaseModel):
    """A warning generated when inputs approach or violate standard boundaries."""
    code: str
    message: str
    severity: str

class ValidationResult(BaseModel):
    """Result of an engineering validation check."""
    is_valid: bool
    warnings: List[EngineeringWarning] = Field(default_factory=list)
    errors: List[str] = Field(default_factory=list)

# -----------------------------------------------------------------------------
# INPUT MODELS
# -----------------------------------------------------------------------------
class ConcreteRequirements(BaseModel):
    characteristic_strength: float = Field(..., gt=0, description="f_ck in N/mm2")
    proportion_defective: float = Field(default=5.0, gt=0, lt=100, description="Percentage")
    age_days: int = Field(default=28, gt=0)
    slump_class: str = Field(..., description="e.g., Slump_10_30")
    max_wc_ratio: Optional[float] = Field(default=None, gt=0, le=1.0)
    min_cement_content: Optional[float] = Field(default=None, gt=0)

class CementProperties(BaseModel):
    cement_type: str = Field(..., description="e.g., CEM_I")
    strength_class: str = Field(..., description="e.g., 42.5")
    relative_density: float = Field(default=3.15, gt=0)

class AggregateProperties(BaseModel):
    max_aggregate_size: int = Field(..., description="d_max in mm")
    fine_aggregate_type: str = Field(..., description="Crushed or Uncrushed")
    coarse_aggregate_type: str = Field(..., description="Crushed or Uncrushed")
    fine_aggregate_rd: float = Field(default=2.6, gt=0)
    coarse_aggregate_rd: float = Field(default=2.6, gt=0)
    percentage_passing_600: float = Field(..., ge=0, le=100)
    fine_aggregate_moisture: float = Field(default=0.0, ge=0)
    coarse_aggregate_moisture: float = Field(default=0.0, ge=0)
    fine_aggregate_absorption: float = Field(default=0.0, ge=0)
    coarse_aggregate_absorption: float = Field(default=0.0, ge=0)

class MixDesignInput(BaseModel):
    project_id: str
    concrete: ConcreteRequirements
    cement: CementProperties
    aggregate: AggregateProperties
    standard_deviation_override: Optional[float] = Field(default=None, ge=0)

# -----------------------------------------------------------------------------
# RESULT MODELS
# -----------------------------------------------------------------------------
class MixDesignResult(BaseModel):
    """The final calculated concrete mix design."""
    target_mean_strength: float
    water_cement_ratio: float
    free_water_content: float
    cement_content: float
    total_aggregate: float
    fine_aggregate: float
    coarse_aggregate: float
    
    # Adjusted batch weights (wet)
    batch_water: float
    batch_fine_aggregate: float
    batch_coarse_aggregate: float
    
    trace: CalculationTrace
    validation: ValidationResult
