# Benchmark Report: Sync (v1) vs Async (v2)

## 1. Objective
Measure response time and throughput of the API before (v1, synchronous) and after (v2, asynchronous) conversion.

## 2. Setup
- Machine / CPU / RAM: _fill in_
- Python / FastAPI / uvicorn versions: _fill in_
- Server: `uvicorn app.main:app --workers 1`
- Simulated I/O: DB call 0.5 s, email 2 s (see `app/config.py`)

## 3. Method
`benchmark/bench.py` fires N concurrent requests (10, 50, 100 for GET; 50 for POST),
repeats 3 times and reports the median of average latency, p95 and requests/second.

## 4. Results
Paste the table printed by `bench.py` (also saved in `benchmark/results.csv`).

| Endpoint | Concurrency | Sync avg (ms) | Async avg (ms) | Sync p95 | Async p95 | Sync RPS | Async RPS | Improvement |
|---|---|---|---|---|---|---|---|---|
| GET /users/{id} | 10 | | | | | | | |
| GET /users/{id} | 50 | | | | | | | |
| GET /users/{id} | 100 | | | | | | | |
| POST /orders | 50 | | | | | | | |

## 5. Analysis
- Sync endpoints run in a threadpool (about 40 threads by default), so beyond that
  concurrency requests queue and latency grows in steps.
- Async endpoints wait on all requests at once, so latency stays near the 0.5 s I/O time.
- POST improves further because the 2 s email moved into a background task.
- Async does not speed up CPU-bound work.

## 6. Conclusion
_Summarize your measured improvement (percent latency reduction, RPS gain) here._
