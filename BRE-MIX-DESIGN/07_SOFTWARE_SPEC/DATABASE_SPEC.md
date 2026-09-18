# Database Specification

## Storage Requirements

SQLite database for local project storage.

## Schema (Conceptual)

### projects
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PK | Project ID |
| name | TEXT | Project name |
| reference | TEXT | Mix reference |
| engineer | TEXT | Engineer name |
| created_at | DATETIME | Creation timestamp |
| updated_at | DATETIME | Last update |

### mix_designs
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PK | Design ID |
| project_id | INTEGER FK | Parent project |
| inputs_json | TEXT | All inputs as JSON |
| results_json | TEXT | All results as JSON |
| trace_json | TEXT | Calculation trace as JSON |
| method | TEXT | "BRE_BR331_1997" |
| engine_version | TEXT | Software version |
| data_version | TEXT | Engineering data version |
| created_at | DATETIME | Creation timestamp |

## Versioning

```
Engineering Dataset Version: BRE-1997-DATA-1.0
Calculation Engine Version:  1.0.0
Application Version:         0.1.0
```

---

*Created: 2026-09-18*
