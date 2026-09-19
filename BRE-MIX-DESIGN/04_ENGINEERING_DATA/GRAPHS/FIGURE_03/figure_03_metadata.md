# Figure 3: Relationship between standard deviation and characteristic strength

## Source
**Document:** BRE BR 331 (Second Edition, 1997)
**Printed Page:** 8
**PDF Page:** 13
**Section References:** 4.2 The distribution of results, 4.4 Margin for mix design, 5.1 Selection of target water/cement ratio (Stage 1).

## Structure
**X-Axis:** Specified characteristic strength ($N/mm^2$)
**Y-Axis:** Standard deviation ($N/mm^2$)

## Procedural Rules
1. **n < 20 rule:** If previous information concerning the variability of strength tests comprises fewer than 20 results (or no data), the standard deviation to be adopted should be that obtained from **Line A**.
2. **n >= 20 rule:** If 20 or more results are available, the standard deviation is the calculated standard deviation of such results, provided that this value is **not less than Line B**.
3. **Calculation of s:** BR 331 Section 4.2 explicitly defines the statistical calculation of the standard deviation as $s = \sqrt{\frac{\sum (x - m)^2}{n - 1}}$.

## Piecewise Relationships
**Line A (n < 20):**
- For $f_c < 20$: $Y = 4 + 0.2 \times f_c$
- For $f_c \ge 20$: $Y = 8.0$

**Line B (n >= 20 Minimum bound):**
- For $f_c < 20$: $Y = 2 + 0.1 \times f_c$
- For $f_c \ge 20$: $Y = 4.0$

## Statistical Constants (k)
Section 4.4 tabulates `k` derived from the normal distribution based on proportion of defectives:
- 10% defectives = 1.28
- 5% defectives = 1.64
- 2.5% defectives = 1.96
- 1% defectives = 2.33

## Provenance
**Status:** `VERIFIED`
**Extraction Method:** Explicit textual bounds and structural graph interpolation from the source image.
