# Figure 5 Digitization Notes

* **Source**: BR 331, Figure 5: "Estimated wet density of fully compacted concrete" (Printed page 18).
* **Extraction Procedure**: All 6 explicitly plotted curves corresponding to Relative Density of combined aggregates (2.4, 2.5, 2.6, 2.7, 2.8, 2.9) have been systematically digitized by reading the visual Y-values (Wet density of concrete mix, kg/m³) at key Free-water content X-values (140, 160, 180, 200, 220, 240).
* **Extraction Method**: Visual extraction mapping graph grid coordinates to pixel ratios for precise readings. Points where curves intersect or drop below the valid bounds have been omitted.
* **Interpolation**: The target wet density is interpolated using 1D linear interpolation along individual curves (Free-water content) and between adjacent datum curves (Relative density). Extrapolation outside the bounding boxes is strictly prohibited.
* **Verification**: The digitized points accurately replicate BR 331 Example 1 (Relative Density 2.6, Free Water 160 -> Wet Density = 2400 kg/m³).
