from typing import List, Dict, Any
from src.bre_engine.errors.exceptions import InvalidEngineeringInputError
from src.bre_engine.interpolation.linear import linear_interpolate

class CurveFamilyInterpolator:
    """
    Interpolates a value from a family of reference curves, as required by BR 331 Figure 4.
    
    Instead of selecting a single fixed curve, a new custom curve is generated
    parallel to the reference curves, anchored by a specific datum point.
    """
    
    def __init__(self, curves_data: List[Dict[str, Any]], datum_x: float = 0.5):
        """
        Args:
            curves_data: List of dicts, each representing a reference curve.
                         Each must have 'datum_strength_at_05' and 'points' (list of {water_cement_ratio, strength}).
            datum_x: The x-value where the datum anchors are defined (default 0.5 for BR 331).
        """
        # Sort curves by their datum strength at x=0.5
        self.curves = sorted(curves_data, key=lambda c: c['datum_strength_at_05'])
        self.datum_x = datum_x
        
        if len(self.curves) < 2:
            raise ValueError("Curve family interpolation requires at least two reference curves.")

    def _get_strength_on_reference_curve(self, curve: Dict[str, Any], x: float) -> float:
        """Extracts/interpolates the strength on a specific reference curve for a given x."""
        points = [(p['water_cement_ratio'], p['strength']) for p in curve['points']]
        return linear_interpolate(x, points)

    def _get_strength_on_custom_curve(self, target_x: float, datum_y: float) -> float:
        """
        Finds the strength at `target_x` for a custom curve that passes through (datum_x, datum_y).
        It does this by linearly interpolating between the two reference curves that bracket the datum.
        """
        # 1. Find bracketing reference curves based on their datum y (at datum_x)
        lower_curve = None
        upper_curve = None
        
        # Check out of bounds
        if datum_y < self.curves[0]['datum_strength_at_05'] or datum_y > self.curves[-1]['datum_strength_at_05']:
            raise InvalidEngineeringInputError(
                f"Datum strength {datum_y} is outside the bounds of the reference curves "
                f"[{self.curves[0]['datum_strength_at_05']}, {self.curves[-1]['datum_strength_at_05']}]."
            )
            
        # Exact match
        for curve in self.curves:
            if curve['datum_strength_at_05'] == datum_y:
                return self._get_strength_on_reference_curve(curve, target_x)
                
        # Find brackets
        for i in range(len(self.curves) - 1):
            if self.curves[i]['datum_strength_at_05'] < datum_y < self.curves[i+1]['datum_strength_at_05']:
                lower_curve = self.curves[i]
                upper_curve = self.curves[i+1]
                break
                
        # 2. Interpolate the target_x value between the two bracketing curves
        y_lower_datum = lower_curve['datum_strength_at_05']
        y_upper_datum = upper_curve['datum_strength_at_05']
        ratio = (datum_y - y_lower_datum) / (y_upper_datum - y_lower_datum)
        
        y_lower_target = self._get_strength_on_reference_curve(lower_curve, target_x)
        y_upper_target = self._get_strength_on_reference_curve(upper_curve, target_x)
        
        return y_lower_target + ratio * (y_upper_target - y_lower_target)

    def find_x_for_y(self, target_y: float, datum_y: float, x_min: float = 0.3, x_max: float = 0.9, step: float = 0.01) -> float:
        """
        Finds the x (W/C ratio) that yields `target_y` (target mean strength) 
        on the custom curve defined by `datum_y`.
        """
        # Generate the custom curve by evaluating it at discrete x points
        # Then perform standard 1D linear interpolation to find x for target_y
        
        import numpy as np
        
        x_values = list(np.arange(x_min, x_max + step, step))
        # Ensure exact bounds are included due to floating point inaccuracies
        if x_values[-1] < x_max:
            x_values.append(x_max)
            
        custom_points = []
        for x in x_values:
            try:
                y = self._get_strength_on_custom_curve(x, datum_y)
                # Cap at 90 as per the physical limits of the chart if necessary, but we just record the point
                custom_points.append((x, y))
            except InvalidEngineeringInputError as e:
                if "Datum strength" in str(e):
                    raise
                # If a reference curve doesn't extend this far, we just stop evaluating
                continue
                
        if not custom_points:
            raise InvalidEngineeringInputError("Unable to construct custom curve within valid bounds.")
            
        # The custom curve maps x -> y (decreasing).
        # We need to interpolate y -> x. Since y is decreasing, we reverse the lists to make y strictly increasing
        # so we can use standard linear interpolation.
        
        # We only consider points where y actually decreases to avoid zero-slope issues
        valid_points = []
        for i in range(len(custom_points)):
            if i == 0 or custom_points[i][1] < custom_points[i-1][1]:
                valid_points.append((custom_points[i][1], custom_points[i][0])) # (y, x)
                
        valid_points.sort(key=lambda p: p[0]) # sort by y ascending
        
        if len(valid_points) < 2:
            raise InvalidEngineeringInputError("Not enough points to interpolate target W/C.")
            
        try:
            return linear_interpolate(target_y, valid_points)
        except InvalidEngineeringInputError:
             y_min = valid_points[0][0]
             y_max = valid_points[-1][0]
             raise InvalidEngineeringInputError(
                 f"Target strength {target_y} is outside the valid range [{y_min:.1f}, {y_max:.1f}] "
                 f"for the curve anchored at datum {datum_y}. Extrapolation is strictly not permitted."
             )
