# InsightFlow

**Business analytics and data automation platform for transforming raw sales data into clean dashboards, quality checks, KPIs and actionable deterministic insights.**

InsightFlow is a portfolio-quality full-stack project built to look and behave like a real commercial analytics product rather than a dashboard template. The UI is desktop-first, dark, layered and glassy; the data pipeline is explicit and auditable.

## What is included

- Premium marketing site and desktop analytics workspace
- Projects, import, semantic mapping, quality, dashboard, reports and settings screens
- CSV **and XLSX** ingestion
- Automatic semantic column detection with confidence scores
- Manual mapping for revenue, order date, order ID, customer, product, category, region, quantity and unit price
- Data-quality score with explainable deductions
- Revenue, orders, customers, AOV, trends, category/region mix, top products and top customers
- Deterministic business insights — no LLM needed for the core product
- FastAPI OpenAPI docs
- SQLite-friendly manual dev setup and PostgreSQL Docker setup
- SQLAlchemy models + Alembic migration
- Local JWT authentication API foundation
- Demo retail data so reviewers can use the full product without preparing a file
- Python test coverage for column detection, analytics and quality logic

## Stack

**Frontend:** Next.js 15, React 19, TypeScript, Recharts, custom CSS design system, Lucide icons  
**Backend:** FastAPI, Pydantic, Pandas, NumPy, OpenPyXL, SQLAlchemy, Alembic, PyJWT  
**Data:** PostgreSQL in Docker / SQLite fallback for frictionless local development

## Run locally (recommended for development)

### 1. Backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

API: `http://127.0.0.1:8000`  
Interactive docs: `http://127.0.0.1:8000/docs`

The backend defaults to `backend/.data/insightflow.db`, so PostgreSQL is **not required** for the manual local workflow.

### 2. Frontend

Open a second terminal:

```powershell
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000`.

Use **Open demo** on the landing page, then **Import data → Load demo dataset** to walk through the complete mapping → quality → analytics flow without the backend. Uploading your own CSV/XLSX uses the FastAPI backend.

## Docker + PostgreSQL

```bash
docker compose up --build
```

This runs Next.js on `:3000`, FastAPI on `:8000`, and PostgreSQL as the metadata store.

## Tests

```bash
cd backend
pytest
```

## Core architecture

```text
Raw CSV / XLSX
      │
      ▼
Schema inspection
      │
      ▼
Semantic mapping
      │
      ├── revenue
      ├── date
      ├── product
      ├── customer
      ├── category
      └── region
      │
      ▼
Data-quality gate
      │
      ▼
Analytics engine
      │
      ├── KPIs
      ├── time series
      ├── breakdowns
      └── deterministic insights
      │
      ▼
Premium desktop workspace / export
```

The important engineering rule is that analytics operates on **business meaning**, never on hard-coded source names such as `total_price_final`.

## Repository

```text
insightflow/
├── frontend/
│   ├── app/
│   ├── components/
│   └── lib/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── domain/
│   │   ├── schemas/
│   │   └── services/
│   ├── alembic/
│   └── tests/
├── sample-data/
└── docs/
```

## Design philosophy

The visual reference was a premium purple finance interface. InsightFlow translates that mood into a **desktop analytics product**: soft liquid-glass surfaces, restrained ambient purple light, quiet motion, crisp hierarchy, custom workspace composition, and no generic “AI SaaS” neon overload.

See `docs/design-system.md` and `docs/architecture.md` for the rationale.
