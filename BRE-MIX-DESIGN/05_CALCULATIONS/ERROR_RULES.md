# Error Rules

> Engineering validation rules for the BRE mix design software.

---

## Error Classification

| Level | Meaning | Software Behaviour |
|-------|---------|-------------------|
| **ERROR** | Cannot calculate — missing or invalid input | Block calculation; display message |
| **WARNING** | Calculation possible but engineering attention required | Allow calculation; display prominent warning |
| **INFORMATION** | Useful engineering note | Display note |

---

## Error Rules

### ERR-001: Missing characteristic strength
- **Level:** ERROR
- **Condition:** f_ck not provided or f_ck ≤ 0
- **Message:** "Characteristic compressive strength must be provided and greater than zero."

### ERR-002: Invalid cement class
- **Level:** ERROR
- **Condition:** Cement class not in {42.5, 52.5}
- **Message:** "Cement strength class must be 42.5 or 52.5."

### ERR-003: Invalid aggregate type
- **Level:** ERROR
- **Condition:** Aggregate type not in {Crushed, Uncrushed}
- **Message:** "Aggregate type must be Crushed or Uncrushed."

### ERR-004: Invalid aggregate size
- **Level:** ERROR
- **Condition:** Max aggregate size not in {10, 20, 40}
- **Message:** "Maximum aggregate size must be 10, 20, or 40 mm."

### ERR-005: Missing workability
- **Level:** ERROR
- **Condition:** Neither slump nor Vebe time provided
- **Message:** "A workability measure (slump or Vebe time) must be provided."

### ERR-006: Missing relative density
- **Level:** ERROR
- **Condition:** RD_agg not provided or ≤ 0
- **Message:** "Relative density of combined aggregate (SSD) must be provided."

### ERR-007: Missing fine aggregate grading
- **Level:** ERROR
- **Condition:** %600 not provided
- **Message:** "Percentage of fine aggregate passing 600 µm sieve is required."

---

## Warning Rules

### WARN-001: Unusual characteristic strength
- **Level:** WARNING
- **Condition:** f_ck < 20 or f_ck > 60
- **Message:** "Characteristic strength is outside the typical range (20–60 N/mm²) for the BRE method."

### WARN-002: Unusual relative density
- **Level:** WARNING
- **Condition:** RD_agg < 2.3 or RD_agg > 2.9
- **Message:** "Relative density of aggregate is outside the typical range (2.3–2.9)."

### WARN-003: Minimum cement governs
- **Level:** WARNING
- **Condition:** Calculated C < C_min
- **Message:** "Cement content increased to meet minimum requirement of {C_min} kg/m³."

### WARN-004: Maximum cement governs
- **Level:** WARNING
- **Condition:** Calculated C > C_max
- **Message:** "Cement content limited by maximum requirement of {C_max} kg/m³. Target strength may not be achievable."

### WARN-005: Unusual cement content
- **Level:** WARNING
- **Condition:** C < 240 or C > 500
- **Message:** "Cement content ({C} kg/m³) is outside the typical range (240–500 kg/m³)."

### WARN-006: Fine aggregate proportion outside typical range
- **Level:** WARNING
- **Condition:** P_fine < 20 or P_fine > 55
- **Message:** "Fine aggregate proportion ({P_fine}%) is outside the typical range (20–55%)."

### WARN-007: Negative batch water
- **Level:** WARNING
- **Condition:** W_batch < 0 after moisture correction
- **Message:** "Negative batch water calculated. Check aggregate moisture values."

### WARN-008: w/c ratio limited by durability
- **Level:** WARNING
- **Condition:** w/c_strength > w/c_max
- **Message:** "w/c ratio limited to {w/c_max} by durability specification. Actual strength will exceed target."

---

## Information Rules

### INFO-001: Interpolated value
- **Level:** INFORMATION
- **Condition:** A value was obtained by interpolation
- **Message:** "The value was obtained by interpolation."

### INFO-002: Design for non-standard age
- **Level:** INFORMATION
- **Condition:** Age ≠ 28 days
- **Message:** "Mix designed for {age}-day strength. Standard design age is 28 days."

### INFO-003: Mixed aggregate types
- **Level:** INFORMATION
- **Condition:** Fine and coarse aggregate types differ
- **Message:** "Water content adjusted for mixed aggregate types using weighted average."

---

*Created: 2026-09-18*
