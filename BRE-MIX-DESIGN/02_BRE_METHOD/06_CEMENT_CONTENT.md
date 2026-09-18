# BRE Mix Design — Stage 3: Cement Content

> **Source:** SRC-BRE-001 — BRE BR 331, Second Edition, 1997
> **BRE Stage:** 3 (Cement Content)

---

## Purpose

Calculate the **cement content** (kg/m³) from the free water content and water/cement ratio, then check against any specified minimum and maximum limits.

---

## Equation

### EQ-BRE-003: Cement Content

```
C = W / (w/c)
```

| Variable | Meaning | Unit |
|----------|---------|------|
| C | Cement content | kg/m³ |
| W | Free water content (from Stage 2) | kg/m³ |
| w/c | Free water/cement ratio (from Stage 1) | dimensionless |

- **Source:** SRC-BRE-001
- **Verification Status:** VERIFIED — fundamental relationship, confirmed by all sources

---

## Checks

### Minimum Cement Content Check

If a minimum cement content (C_min) is specified (e.g., for durability):

```
IF C < C_min THEN:
    C = C_min
    Recalculate w/c ratio: w/c_actual = W / C_min
    FLAG: "Cement content governed by minimum requirement"
    CHECK: w/c_actual must still satisfy any maximum w/c limit
```

### Maximum Cement Content Check

If a maximum cement content (C_max) is specified (to avoid thermal cracking or other issues):

```
IF C > C_max THEN:
    C = C_max
    Recalculate w/c ratio: w/c_actual = W / C_max
    FLAG: "Cement content governed by maximum requirement"
    WARNING: Target mean strength may not be achievable
    ENGINEERING REVIEW REQUIRED
```

---

## Procedure

```
Step 1: Take W from Stage 2 and w/c from Stage 1
         ↓
Step 2: Calculate C = W / (w/c)
         ↓
Step 3: IF C_min is specified AND C < C_min:
          Set C = C_min
          Recalculate: w/c = W / C
          Flag: "Minimum cement content governs"
         ↓
Step 4: IF C_max is specified AND C > C_max:
          Set C = C_max
          Recalculate: w/c = W / C
          Warning: "Maximum cement content may limit strength"
         ↓
Step 5: Record final cement content (C) in kg/m³
```

---

## Engineering Notes

1. When minimum cement content governs, the actual w/c ratio will be lower than the strength-based value, meaning the concrete will be stronger than required. This is acceptable.

2. When maximum cement content governs, the actual w/c ratio will be higher than desired, meaning the concrete may not achieve the target strength. This requires engineering review — possible solutions include changing cement type, aggregate type, or accepting the limitation.

3. Typical cement contents in UK practice range from approximately 240 to 500 kg/m³. Values outside this range should trigger a warning.

4. **Minimum cement content sources:** In practice, minimum cement content is specified by BS 8500 based on exposure class and intended working life. The BRE method itself does not specify minimum cement content — it is an external input.

## Software Notes

- **Suggested function name:** `calculate_cement_content(W, wc_ratio, C_min=None, C_max=None)`
- **Returns:** `(C, wc_actual, flags[])`
- **Input validation:** W > 0, wc_ratio > 0

---

*Source: SRC-BRE-001*
*Verification Status: VERIFIED*
*Created: 2026-09-18*
