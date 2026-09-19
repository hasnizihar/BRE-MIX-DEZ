"""
Custom exceptions for the BRE Calculation Engine.
"""

class EngineeringDataUnavailableError(Exception):
    """
    Exception raised when required engineering data is missing or marked as [PENDING_USER_DATA].
    
    This ensures the application fails safely rather than inventing or estimating
    values that lack primary source verification.
    """
    def __init__(self, data_id: str, source: str, calculation: str, message: str = ""):
        self.data_id = data_id
        self.source = source
        self.calculation = calculation
        
        default_message = (
            f"Engineering data '{self.data_id}' is pending verification from source '{self.source}'. "
            f"Cannot complete calculation: {self.calculation}."
        )
        self.message = message or default_message
        super().__init__(self.message)

class InvalidEngineeringInputError(Exception):
    """Exception raised when user input violates the bounds of the engineering specification."""
    pass

class EngineeringConstraintError(Exception):
    """Exception raised when a calculated value violates a specified engineering constraint (e.g. maximum cement content) making the mix design physically impossible under current specifications."""
    pass
