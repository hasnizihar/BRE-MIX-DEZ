# Validation Plan

> **Purpose:** Define the validation strategy for the BRE mix design calculation engine.

---

## Level 1: Equation Validation

Test each equation individually with known inputs and expected outputs.

| Test ID | Equation | Input | Expected Output | Status |
|---------|----------|-------|----------------|--------|
| TEST-EQ-001 | EQ-BRE-001 | f_ck=30, M=13.12 | f_m=43.12 | Planned |
| TEST-EQ-002 | EQ-BRE-002 | k=1.64, s=8 | M=13.12 | Planned |
| TEST-EQ-003 | EQ-BRE-003 | W=195, w/c=0.50 | C=390 | Planned |
| TEST-EQ-004 | EQ-BRE-004 | D=2370, C=390, W=195 | A=1785 | Planned |
| TEST-EQ-005 | EQ-BRE-005 | A=1785, P=40% | FA=714 | Planned |
| TEST-EQ-006 | EQ-BRE-006 | A=1785, FA=714 | CA=1071 | Planned |

---

## Level 2: Component Validation

Test each calculation stage as a complete unit.

| Test ID | Component | Description | Status |
|---------|-----------|-------------|--------|
| TEST-CMP-001 | Target mean strength | Full Stage 1 with k factor selection | Planned |
| TEST-CMP-002 | w/c ratio determination | Table 2 lookup + Figure 4 | Planned |
| TEST-CMP-003 | Water content | Table 3 lookup with all aggregate sizes | Planned |
| TEST-CMP-004 | Cement content | With min/max checks | Planned |
| TEST-CMP-005 | Total aggregate | With wet density estimation | Planned |
| TEST-CMP-006 | Fine/coarse split | Figure 6 lookup | Planned |
| TEST-CMP-007 | Moisture corrections | Field correction equations | Planned |

---

## Level 3: Complete Worked Example Validation

Test the entire pipeline against golden test cases.

| Test ID | Case | Description | Status |
|---------|------|-------------|--------|
| TEST-GOLD-001 | CASE-001 | C30, 42.5 cement, uncrushed, 20mm | Planned |
| TEST-GOLD-002 | CASE-002 | C40, 42.5 cement, crushed, 20mm | Planned |

---

## Level 4: Boundary Value Testing

| Test ID | Boundary | Description | Status |
|---------|----------|-------------|--------|
| TEST-BND-001 | Minimum f_ck | f_ck = 10 N/mm² (very low) | Planned |
| TEST-BND-002 | Maximum f_ck | f_ck = 70 N/mm² (very high) | Planned |
| TEST-BND-003 | w/c = 0.30 | Minimum practical w/c ratio | Planned |
| TEST-BND-004 | w/c = 0.80 | Maximum practical w/c ratio | Planned |
| TEST-BND-005 | Slump = 0 | Minimum slump | Planned |
| TEST-BND-006 | Slump = 180 | Maximum slump | Planned |
| TEST-BND-007 | All 10mm sizes | Smallest aggregate | Planned |
| TEST-BND-008 | All 40mm sizes | Largest aggregate | Planned |
| TEST-BND-009 | Min cement governs | C_min > calculated C | Planned |
| TEST-BND-010 | Max cement governs | C_max < calculated C | Planned |

---

## Level 5: Invalid Input Testing

| Test ID | Invalid Input | Expected Behaviour | Status |
|---------|--------------|-------------------|--------|
| TEST-INV-001 | f_ck = 0 | ERROR | Planned |
| TEST-INV-002 | f_ck = -10 | ERROR | Planned |
| TEST-INV-003 | Cement class = "35" | ERROR | Planned |
| TEST-INV-004 | Aggregate size = 15 | ERROR | Planned |
| TEST-INV-005 | Slump = -5 | ERROR | Planned |
| TEST-INV-006 | RD_agg = 0 | ERROR | Planned |
| TEST-INV-007 | No workability specified | ERROR | Planned |
| TEST-INV-008 | %600 = 150 | ERROR (>100%) | Planned |

---

## Level 6: Independent Engineering Verification

| Test ID | Method | Description | Status |
|---------|--------|-------------|--------|
| TEST-IND-001 | Manual calculation | Engineer performs manual BRE calculation and compares | Planned |
| TEST-IND-002 | Third-party tool | Compare results with another BRE calculator (if available) | Planned |
| TEST-IND-003 | Reverse calculation | Given known mix, verify the design reproduces it | Planned |

---

## Validation Acceptance Criteria

1. All Level 1–3 tests must pass before UI development begins
2. Level 4–5 tests must pass before beta release
3. Level 6 tests must be completed before production release
4. Golden test expected values must NEVER be modified to make tests pass
5. Tolerances on golden tests account for digitization uncertainty in Figures 4, 5, 6

---

*Created: 2026-09-18*
