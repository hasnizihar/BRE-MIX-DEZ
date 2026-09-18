# AI Agent Rules

> **Purpose:** Rules governing AI coding agents working on this project.

---

## Core Rules

1. **Never invent engineering data.** Every equation, table value, constant, interpolation rule, and engineering limit must come from a documented source.

2. **Never modify verified engineering data without traceability.** Any change to data in `02_BRE_METHOD/`, `04_ENGINEERING_DATA/`, or `05_CALCULATIONS/` must update source register, traceability matrix, and changelog.

3. **Never silently change source editions.** The primary source is BRE BR 331, Second Edition, 1997. Do not substitute values from other editions or methods without explicit documentation.

4. **Never remove tests to make the build pass.** If a test fails, the code is wrong — not the test.

5. **Never modify expected validation values to make tests pass.** Golden test expected values are authoritative. If they cannot be reproduced, investigate the calculation.

6. **Never place engineering calculations directly in UI components.** All engineering logic belongs in the calculation engine layer.

7. **Never remove existing functionality without explicit approval.**

8. **Every engineering change requires documentation.** Update the relevant method file, traceability, and changelog.

9. **Every engineering calculation requires a source reference.** Include source ID, edition, section/page in code comments.

10. **Unknown information must be flagged, not guessed.** Use UNVERIFIED status and create a review item.

---

## Before Making Any Change

```
READ AGENTS.md
  ↓
READ relevant engineering specification
  ↓
UNDERSTAND the existing implementation
  ↓
PLAN the change
  ↓
IMPLEMENT
  ↓
TEST (all existing + new tests)
  ↓
VERIFY against engineering specification
  ↓
DOCUMENT changes
  ↓
UPDATE traceability
```

---

## Forbidden Actions

- Hardcoding engineering values that should be loaded from data files
- Using mysterious variable names instead of engineering names
- Combining BRE with ACI/IS/Eurocode methods
- Claiming BS compliance without specific justification
- Silently selecting values that should be user inputs
- Removing engineering comments or documentation

---

*Created: 2026-09-18*
