# Software Architecture

> **Purpose:** Define the recommended software architecture for the future BRE Mix Design desktop application.

---

## Architecture Overview

```
┌─────────────────────────────────────────────┐
│              DESKTOP UI LAYER                │
│  (Input forms, results display, reports)     │
│  Technology: PySide6 / WPF / Similar         │
└──────────────────────┬──────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────┐
│          APPLICATION SERVICES LAYER          │
│  (Project management, file I/O, export)      │
│  Orchestrates calculation and presentation   │
└──────────────────────┬──────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────┐
│       BRE CALCULATION ENGINE LAYER           │
│  (Pure engineering calculations)             │
│  NO UI dependencies                          │
│  NO database dependencies                    │
│  Fully testable in isolation                 │
│                                              │
│  ├── strength.py    — EQ-BRE-001/002        │
│  ├── wc_ratio.py    — GRAPH-BRE-001         │
│  ├── water.py       — TBL-BRE-003           │
│  ├── cement.py      — EQ-BRE-003            │
│  ├── aggregate.py   — EQ-BRE-004/005/006    │
│  ├── density.py     — GRAPH-BRE-002         │
│  ├── corrections.py — EQ-BRE-007/008/009    │
│  ├── validation.py  — Error/warning rules    │
│  ├── trace.py       — Calculation trace      │
│  └── mix_design.py  — Pipeline orchestrator  │
└──────────────────────┬──────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────┐
│          ENGINEERING DATA LAYER              │
│  (Tables, graphs, constants — read-only)     │
│                                              │
│  ├── tables/TBL-BRE-002.json                │
│  ├── tables/TBL-BRE-003.json                │
│  ├── graphs/GRAPH-BRE-001.json              │
│  ├── graphs/GRAPH-BRE-002.json              │
│  ├── graphs/GRAPH-BRE-003.json              │
│  └── constants.json                         │
└──────────────────────┬──────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────┐
│           VALIDATION LAYER                   │
│  (Golden tests, unit tests, boundary tests)  │
│                                              │
│  ├── golden/CASE-001/                       │
│  ├── golden/CASE-002/                       │
│  ├── unit_tests/                            │
│  └── boundary_tests/                        │
└─────────────────────────────────────────────┘
```

---

## Key Architecture Rules

1. **Engineering calculations must NEVER be in UI components**
2. **The calculation engine must be testable without launching the UI**
3. **Engineering data must be separate from application code** (loaded from JSON/data files)
4. **Every calculation must produce a trace** (not just final results)
5. **The engine must be stateless** — given the same inputs, always produce the same outputs

---

## Recommended Technology Stack

### Option A: Python (Recommended for AI-agent development)

```
PySide6          — Desktop UI
Python           — Calculation engine
SQLite           — Project database
Pydantic         — Data validation and models
Matplotlib       — Charts
ReportLab/FPDF   — PDF reports
pytest           — Testing
```

### Option B: C# / .NET (For commercial Windows application)

```
WPF or WinUI     — Desktop UI
C#               — Calculation engine
SQLite           — Project database
iTextSharp       — PDF reports
NUnit/xUnit      — Testing
```

---

## Data Flow

```
User Input → Input Validation → Calculation Engine → Results + Trace → Display / Report / Save
```

The result object from the calculation engine should contain:

```
MixDesignResult:
  ├── inputs (all user inputs)
  ├── intermediate_values (every calculated intermediate)
  ├── final_mix (W, C, FA, CA per m³)
  ├── batch_mix (corrected for moisture)
  ├── trace (step-by-step calculation with source references)
  ├── checks (list of engineering checks with pass/fail)
  ├── warnings (list of warning messages)
  ├── errors (list of error messages)
  └── metadata (method, edition, software version, timestamp)
```

---

*Created: 2026-09-18*
