# InsightFlow architecture — V0.1

## Goal

V0.1 proves the core product loop without authentication, persistence, AI, Excel support, or advanced data quality tooling.

```text
CSV upload
  -> parser
  -> schema inspection
  -> semantic column detection
  -> user-confirmed mapping
  -> analytics service
  -> typed API response
  -> dashboard
```

## Architectural boundary

The frontend presents state. The backend owns dataset interpretation and analytics.

Analytics code never depends on raw source column names. It receives semantic mappings such as `revenue -> total_price`.

## Temporary dataset strategy

Uploaded files are written to `/tmp/insightflow/{uuid}.csv` in V0.1. This keeps the upload and analyze calls separated without introducing PostgreSQL too early.

## V0.1 API

- `GET /api/v1/health`
- `POST /api/v1/datasets/upload`
- `POST /api/v1/datasets/{dataset_id}/analyze`

## Future boundaries

Later releases can add:

- PostgreSQL metadata persistence
- object storage / Parquet / DuckDB for larger datasets
- workspaces and users
- data quality runs
- deterministic insights
- reports and exports
- Excel imports
- AI-assisted querying as an optional layer
