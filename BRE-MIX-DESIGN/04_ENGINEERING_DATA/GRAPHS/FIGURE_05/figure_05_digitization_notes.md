# DATA-002: Figure 5 Digitization Notes

## Current Status: SYNTHETIC_PLACEHOLDER

### Digitization Strategy
Figure 5 of BR 331 is a flat raster graph plotting `Estimated wet density` (Y) against `Free-water content` (X) for several curves of `Relative density of combined aggregate` (2.4 to 2.9).

Due to the lack of vector coordinates in the source PDF and the current unavailability of verified coordinate readings, the curves in `figure_05_points.json` have been synthesized using a volumetric physical approximation.

### WARNING: PROVENANCE ISSUE
The values in `figure_05_points.json` are **SYNTHETIC PLACEHOLDERS**. They are *not* digitized from the BRE Figure 5 graph. They must not be used as authoritative engineering inputs for downstream calculations (like EQ-BRE-004) in a production setting.

### Source Examples Used for Approximation
The synthetic values were mathematically benchmarked to match the exact examples provided in BR 331 Section 7 (Examples 1-5):
- **Example 1:** Free-water 160, Uncrushed (RD 2.6) $\rightarrow$ Wet Density 2400
- **Example 5:** Free-water 160, Crushed (RD 2.7) $\rightarrow$ Wet Density 2450

### Synthesis Method
The points in the dataset were generated using the approximation equation:
$D = 2400 + 500 \times (RD - 2.6) - 1.6 \times (W - 160)$

### Future Action Required
A human engineer must visually read the exact coordinates from Figure 5 in the printed BR 331 standard and replace the values in `figure_05_points.json` with a calibrated graph digitization. Only after the points physically originate from the graph (and match the examples) should the status be upgraded to `DIGITIZED_PENDING_VERIFICATION`.
