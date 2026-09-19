from typing import Dict, Any, List
from src.bre_engine.errors.exceptions import EngineeringConstraintError

class Graph2DInterpolator:
    """
    Interpolates a 2D surface from discrete curves defined by a primary parameter.
    
    Used for relationships like Figure 5 where a continuous Y value (Wet Density)
    is derived from a continuous X value (Free-water) and a continuous Curve parameter (Relative Density).
    """
    
    def __init__(self, data: Dict[str, Any], allow_synthetic: bool = False):
        """
        Expects data in the format:
        {
            "status": "DATA_AVAILABLE",
            "curves": [ ... ]
        }
        """
        from src.bre_engine.errors.exceptions import EngineeringDataUnavailableError
        self.data = data
        
        status = self.data.get("status", "")
        if status == "SYNTHETIC_PLACEHOLDER" and not allow_synthetic:
            raise EngineeringDataUnavailableError(
                data_id="DATA-002 (Figure 5)",
                source="BR 331",
                calculation="Graph 2D Interpolation",
                message="Figure 5 data is currently a SYNTHETIC_PLACEHOLDER. It has not been physically digitized from the BRE standard. Set allow_synthetic=True if running interpolation tests."
            )
            
        self.curves = sorted(self.data.get("curves", []), key=lambda c: c["relative_density"])
        
    def _interpolate_1d(self, x: float, x0: float, y0: float, x1: float, y1: float) -> float:
        """Linear interpolation between two points."""
        if x0 == x1:
            return y0
        return y0 + (x - x0) * (y1 - y0) / (x1 - x0)

    def _interpolate_along_curve(self, curve: Dict[str, Any], x_target: float) -> float:
        """Interpolates the Y value for a given X along a specific curve."""
        points = sorted(curve["points"], key=lambda p: p["free_water"])
        
        # Exact match
        for p in points:
            if p["free_water"] == x_target:
                return p["wet_density"]
                
        # Boundary checks
        if x_target < points[0]["free_water"] or x_target > points[-1]["free_water"]:
            raise EngineeringConstraintError(
                f"Free-water content {x_target} is outside the digitized bounds "
                f"[{points[0]['free_water']}, {points[-1]['free_water']}] of the graph. Extrapolation is not permitted."
            )
            
        # Interpolate between points
        for i in range(len(points) - 1):
            p1, p2 = points[i], points[i+1]
            if p1["free_water"] < x_target < p2["free_water"]:
                return self._interpolate_1d(
                    x=x_target,
                    x0=p1["free_water"],
                    y0=p1["wet_density"],
                    x1=p2["free_water"],
                    y1=p2["wet_density"]
                )
                
        raise ValueError("Failed to interpolate along curve.")

    def interpolate(self, x_value: float, curve_value: float) -> float:
        """
        Performs 2D interpolation for a given x (Free-water) and curve parameter (Relative Density).
        """
        # Exact curve match
        for curve in self.curves:
            if curve["relative_density"] == curve_value:
                return self._interpolate_along_curve(curve, x_value)
                
        # Boundary checks for curve parameter
        if curve_value < self.curves[0]["relative_density"] or curve_value > self.curves[-1]["relative_density"]:
            raise EngineeringConstraintError(
                f"Relative density {curve_value} is outside the digitized curves "
                f"[{self.curves[0]['relative_density']}, {self.curves[-1]['relative_density']}]. Extrapolation is not permitted."
            )
            
        # Interpolate between curves
        for i in range(len(self.curves) - 1):
            c1, c2 = self.curves[i], self.curves[i+1]
            if c1["relative_density"] < curve_value < c2["relative_density"]:
                y1 = self._interpolate_along_curve(c1, x_value)
                y2 = self._interpolate_along_curve(c2, x_value)
                return self._interpolate_1d(
                    x=curve_value,
                    x0=c1["relative_density"],
                    y0=y1,
                    x1=c2["relative_density"],
                    y1=y2
                )
                
        raise ValueError("Failed to interpolate between curves.")
