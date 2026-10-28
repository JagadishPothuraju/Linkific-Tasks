# Orders API – Sync to Async Conversion (FastAPI)

Covers: async endpoints, async/await, middleware, background tasks,
dependency injection, validation, API versioning, performance benchmarking.

## Setup
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run
```bash
uvicorn app.main:app --workers 1
```
Open http://127.0.0.1:8000/docs

## Test
```bash
pytest -q
```

## Benchmark
With the server running, in another terminal:
```bash
python benchmark/bench.py
```
Copy the results into `docs/BENCHMARK_REPORT.md`.

## Layout
```
app/            main.py, config.py, models.py, deps.py, middleware.py, tasks.py, routers/v1.py, routers/v2.py
tests/          test_api.py
benchmark/      bench.py
docs/           API_DOCUMENTATION.md, BENCHMARK_REPORT.md
```
