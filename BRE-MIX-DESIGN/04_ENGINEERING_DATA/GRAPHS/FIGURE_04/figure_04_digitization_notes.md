# Figure 4 Digitization Notes

* **Source Image**: `scratch/page16_fig4.png` rendered at 300 DPI from PDF Page 17.
* **Extraction Procedure**: A browser subagent inspected the visual curves and extracted exact pixel-to-value coordinates for key structural reference curves (Datum 40 and 50) at `X = [0.3, 0.4, 0.5, 0.6, 0.7]`.
* **Interpolation**: The provider interpolates target strength using 2D curve family interpolation. The Y-values (strengths) are strictly evaluated against these exact visual extractions.
* **Limitations**: The curves below 20 N/mm² are extremely dense and heavily non-linear. This digitization captures the structural range (Curve 40 to 50). Values falling outside this bounded interpolation require exact extraction of those specific reference curves.
