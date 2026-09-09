# InsightFlow

Portfolio-quality business analytics and data automation SaaS. The current repository is the **V0.1 architecture + wireframe milestone**.

## Current scope

- Next.js + TypeScript frontend shell
- neutral wireframe pages: Overview, Upload, Preview, Dashboard
- FastAPI backend
- CSV upload validation and temporary storage
- basic semantic column detection
- basic sales analytics service
- typed API schemas
- demo retail dataset
- backend unit tests

Not included yet: authentication, PostgreSQL, Excel, data quality score, deterministic insights, report export, advanced filtering, final visual design.

## Repository

```text
insightflow/
├── frontend/
│   ├── app/
│   ├── components/
│   └── lib/
├── backend/
│   ├── app/
│   └── tests/
├── sample-data/
├── docs/
├── docker-compose.yml
├── .env.example
└── README.md
```

## Run backend

```bash
cd backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API docs: `http://localhost:8000/docs`

## Run frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend: `http://localhost:3000`

The current frontend pages use mock data on purpose. This keeps the wireframe milestone stable while the final design sheet is being defined. The API client and types are already prepared for the integration milestone.

## Demo data

Use `sample-data/retail_sales.csv` for backend testing and the later end-to-end upload flow.

## Key product decision

InsightFlow separates raw source columns from business meaning:

```text
raw dataset -> semantic mapping -> analytics
```

Example: `total_price -> revenue`. Analytics should depend on the semantic role `revenue`, not the source name `total_price`.

## Next milestone

1. Apply supplied design sheet / design tokens.
2. Wire the upload page to the FastAPI endpoint.
3. Persist the upload result through the preview flow.
4. Send confirmed mappings to `/analyze`.
5. Replace dashboard mock data with the API response.
