# DATA-003: Figure 6 Digitization Notes

## Current Status: [PENDING_USER_DATA]

### Graph Description
Figure 6 consists of multiple inter-dependent graphs spanning two pages (14-15) in BR 331. The graph lookup requires four dimensions:
1. **Maximum size of aggregate** (e.g., 10mm, 20mm, 40mm)
2. **Workability level (Slump)** (e.g., 0-10mm, 10-30mm, 30-60mm, 60-180mm)
3. **Free-water/cement ratio** (X-axis)
4. **Grading of fine aggregate** (% passing a 600 μm sieve) (Curve parameter)

### Digitization Decision
Due to the multi-dimensional nature of these plots and the fact they are embedded as raster images within the PDF, reliable programmatic digitization is impossible.
Attempting to reverse-engineer a formula or approximate these curves programmatically introduces unacceptable engineering risk and violates strict provenance guardrails.

Therefore, **no synthetic coordinates have been generated**. The JSON schema has been established, but the dataset is entirely empty.

### Future Action Required
A human engineer must visually read the exact coordinates from the printed BR 331 Figure 6 curves and populate the `figure_06_points.json` file. Only after the points physically originate from the graph should the status be upgraded to `DATA_AVAILABLE` or `DIGITIZED_PENDING_VERIFICATION`.
