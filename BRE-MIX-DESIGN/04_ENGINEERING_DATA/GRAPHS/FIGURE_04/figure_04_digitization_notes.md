# Figure 4 Digitization Notes

* **Source**: BR 331, Figure 4: "Relationship between free-water/cement ratio and compressive strength" (PDF page 20, Printed page 16).
* **Extraction Procedure**: All 9 explicitly plotted curves have been systematically digitized by reading the visual Y-values (Compressive strength, N/mm²) at key W/C ratio X-values (0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9).
* **Datum Values**: Each curve corresponds to a specific 'datum' strength defined exactly at W/C = 0.5. The 9 curves correspond to datum values: 70, 60, 50, 40, 30, 20, 13, 7, and 3.
* **Extraction Method**: Visual extraction mapping graph grid coordinates to pixel ratios for precise readings. Points where curves intersect or drop below the valid X-axis bounds have been omitted for that curve.
* **Interpolation**: The target W/C ratio is interpolated using 1D linear interpolation along individual curves and between adjacent datum curves. Extrapolation outside the bounding box (Datums 3 to 70) is strictly prohibited.
* **Verification**: The digitized points accurately replicate BR 331 Example 1 (Target mean strength 46 -> W/C = 0.47) when interpolating between Datum 40 and 50.
