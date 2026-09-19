# Figure 3 Digitization Notes

**Source Image**: Extracted directly from BR 331 PDF page 13 (printed page 8).
**Resolution**: High-quality structural evaluation by subagent.

## Verification Procedure
The bounding rules for `fc >= 20 N/mm^2` are explicitly stated in the BR 331 text.
- Line A: "a standard deviation of 8 N/mm2 should be used for concrete with a characteristic strength of 20 N/mm2 or more"
- Line B: "(4 N/mm2 for concrete with a characteristic strength of 20 N/mm2 or more)"

The regions for `fc < 20 N/mm^2` were analyzed from the graphical presentation.
- The standard deviation must be non-zero for $f_c=0$. 
- For Line A, the intercept is $4$ N/mm^2. It slopes up linearly to $8$ N/mm^2 at $f_c=20$. Equation: $Y = 4 + 0.2 \times X$.
- For Line B, the intercept is $2$ N/mm^2. It slopes up linearly to $4$ N/mm^2 at $f_c=20$. Equation: $Y = 2 + 0.1 \times X$.

## Structure
Because these are simple piecewise linear definitions, we encode the inflection points in `figure_03_points.json`. The software can then easily interpolate linearly between these points without complex mathematical curve fitting.
