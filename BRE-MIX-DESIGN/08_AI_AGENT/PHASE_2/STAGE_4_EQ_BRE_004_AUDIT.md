# Stage 4 EQ-BRE-004 Audit

## Source
BR 331, "Design of normal concrete mixes", 2nd Edition.
Figure 5 (Printed page 18, PDF Page 22) and Section 5.4.

## Figure 5
Title: Relationship between wet density and free-water/cement ratio / aggregate characteristics. Wait, the exact title is "Estimated wet density of fully compacted concrete".

## Section 5.4
Calculation C4: Determine total aggregate content.
Total aggregate content = wet density (D) - cement content (C) - free-water content (W).

## Input Variables
- `Relative Density` of combined aggregate (on saturated and surface-dry basis). Range: 2.4 to 2.9. Defaults are 2.6 (uncrushed) and 2.7 (crushed).
- `Free-water content`. Range: 100 to 280 kg/m³.

## Output Variable
- `Wet density of concrete mix` in kg/m³. Range: 2100 to 2700.

## Units
- X-axis: kg/m³.
- Y-axis: kg/m³.
- Aggregate relative density: dimensionless.

## Graph Interpretation
A family of smooth, concave-downward curves. The lines are roughly parallel. For a given free-water content (X), wet density (Y) decreases. The curves represent different aggregate densities. 

## Curve Families
Six explicitly labeled curves: 2.9, 2.8, 2.7, 2.6, 2.5, 2.4.

## Interpolation
Requires 2D interpolation:
1. Interpolate along the closest Relative Density curves to find wet density for the given Free Water content.
2. Interpolate vertically between the two adjacent Relative Density curves to find the exact wet density.

## Domain
- X-axis bounds: `[140, 240]` digitized.
- Curve parameter bounds: `[2.4, 2.9]`.

## Rounding
Internal calculation preserves full precision. Presentation form rounds Wet Density to nearest integer (kg/m³).

## Example 1
Input: Free-water content = 160 kg/m³, Relative density = 2.6.
Expected Output (Wet Density) = 2400 kg/m³.

## External Constraints
None specifically applied at Stage 4 (unlike W/C constraints).

## Provenance
Data derived from Figure 5 directly.

## Open Questions
None.
