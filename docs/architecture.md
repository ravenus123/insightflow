# InsightFlow architecture

InsightFlow is a monorepo with a Next.js desktop client and a FastAPI analytics API.

```text
Browser / Next.js
    │
    ├── marketing + workspace UI
    ├── semantic mapping
    └── charts / report presentation
    │ JSON + multipart
    ▼
FastAPI
    ├── API routes (HTTP only)
    ├── dataset parser (CSV/XLSX)
    ├── column detector
    ├── data-quality engine
    ├── analytics service
    └── deterministic insight rules
    │
    ├── PostgreSQL / SQLite dev metadata
    └── local/object-style uploaded dataset storage
```

## Key boundary
Analytics never hard-codes source column names. A dataset first becomes a **semantic mapping** (revenue, order date, product, customer, category, region, etc.), and analytics consumes those roles.

## Persistence
Manual local development defaults to SQLite. Docker Compose uses PostgreSQL so the project demonstrates a production-shaped database path without making local onboarding painful.

## No hidden AI dependency
The initial insight engine is deterministic and auditable. It uses comparisons, mix/concentration math and data-quality rules rather than an LLM.
