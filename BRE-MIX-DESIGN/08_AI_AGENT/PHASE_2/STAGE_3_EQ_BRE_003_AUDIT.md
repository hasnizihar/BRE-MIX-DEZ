# EQ-BRE-003 Audit

## 1. Source
- **Document**: BR 331 (Design of Normal Concrete Mixes)
- **Section**: 5.3 (Determination of cement content - Stage 3)
- **Printed page**: 13
- **PDF page**: 17

## 2. BR 331 Equation
Calculation C3:
`Cement content = free-water content / free-water/cement ratio`

## 3. Inputs
- Free-water content (kg/m³)
- Target Free-water/cement ratio (dimensionless)
- Minimum cement content (kg/m³) (Optional external durability constraint)
- Maximum cement content (kg/m³) (Optional external durability constraint)

## 4. Outputs
- Cement content (kg/m³)
- Modified W/C ratio (if minimum cement constraint is triggered)

## 5. Units
kg/m³ / dimensionless = kg/m³

## 6. Constraints
- **Maximum constraint**: If `calculated_cement > max_cement`, BR 331 states the specification cannot be met. The engine must raise an unresolvable error.
- **Minimum constraint**: If `calculated_cement < min_cement`, BR 331 dictates adopting the `min_cement` value and calculating a modified W/C ratio (`free-water / min_cement`).
- **Physical constraints**: W/C ratio must be > 0. Free-water content must be > 0.

## 7. Rounding
- BR 331 does not explicitly mandate premature rounding of the calculation itself in Section 5.3. 
- Example 1 (Table 4) presents the final value as 340 kg/m³ (from 160 / 0.47 = 340.4255...).
- To prevent progressive precision loss downstream (e.g., in Stage 4 wet density calculations), the engineering calculation layer (`eq_bre_003.py`) should return full internal precision. The presentation layer handles rounding to the nearest 5 kg for the final mix design sheet.

## 8. Worked Examples
**Example 1 (Table 4)**:
- Free water: 160
- W/C ratio: 0.47
- Calculated cement: 160 / 0.47 = 340.4255...
- BR 331 presentation cement: 340
- Difference: Presentation rounding only. Calculation layer remains accurate.

## 9. Existing Implementation Audit
Audited `src/bre_engine/calculations/eq_bre_003.py`.
- Correctly implements C3 equation.
- Enforces strict positive > 0 checks for inputs to prevent division by zero.
- Correctly implements both max_cement and min_cement constraints exactly as specified in BR 331 Section 5.3.
- Returns full mathematical precision.

## 10. Identified Deviations
None. The existing implementation in `eq_bre_003.py` perfectly aligns with the BR 331 specification and cleanly separates mathematical calculation from presentation rounding.

## 11. Required Changes
No changes are required to `eq_bre_003.py` itself. The codebase already implements Stage 3 correctly. We need to implement extensive tests.

## 12. Verification Tests
- Test exact match against BR 331 Example 1 (full precision).
- Test basic arithmetic (`W=160, W/C=0.50 -> C=320`).
- Test zero and negative W/C (must fail).
- Test negative water (must fail).
- Test minimum cement constraint overrides C and modifies W/C.
- Test maximum cement constraint raises `EngineeringConstraintError`.
- Develop integration test `test_integration_001_002_003.py` chaining Stage 1 -> 2 -> 3.

## 13. Provenance Status
- **EQ-BRE-003**: `VERIFIED`
- **DATA-001 (Figure 4)**: **PENDING_ENGINEERING_VERIFICATION**. (Only 2 out of 9 curves were digitized. This restricts valid domain to datum strengths between 40-50, which is insufficient for a general-purpose engine. All 9 curves must be digitized before declaring this data fully ready).

## 14. Decision Gate
Proceed to write `implementation_plan.md` outlining the test updates and the Figure 4 downgrade.
