# Orders API – Documentation (v2.0)

Interactive docs: `/docs` (Swagger) and `/redoc`.

## Versions
| Version | Style | Status |
|---|---|---|
| `/api/v1` | Synchronous (`def`, runs in threadpool, email sent inline) | Deprecated |
| `/api/v2` | Asynchronous (`async def`, background tasks) | Recommended |

Migration: change `/api/v1` to `/api/v2`. Request and response schemas are identical.

## Endpoints
### GET `/api/{v}/users/{uid}`
Returns `{"id": 1, "name": "user-1"}`.

### GET `/api/v2/users?ids=1,2,3` (v2 only)
Fetches users concurrently with `asyncio.gather`; returns a list.

### POST `/api/{v}/orders`
Body:
```json
{"customer_email": "a@b.com", "item": "book", "quantity": 2}
```
Response `200`:
```json
{"customer_email": "a@b.com", "item": "book", "quantity": 2, "status": "created"}
```
- v1: responds after the confirmation email is sent (~2.5 s).
- v2: responds immediately; the email is sent by a background task afterwards (~0.5 s).

### GET `/health`
Returns `{"status": "ok"}`.

## Validation
| Field | Rule |
|---|---|
| `customer_email` | valid email |
| `item` | 1–100 characters |
| `quantity` | integer, 1–100 |

Invalid input returns `422`:
```json
{"detail": [{"type": "greater_than", "loc": ["body", "quantity"],
             "msg": "Input should be greater than 0", "input": 0}]}
```

## Headers
Every response includes `X-Process-Time-ms`, set by the timing middleware.

## Architecture notes
- **Middleware** `app/middleware.py`: timing header and request logging.
- **Dependency injection** `app/deps.py`: `get_db()` supplies `Database` via `Depends`.
- **Background jobs** `app/tasks.py`: `send_confirmation` via `BackgroundTasks`.
- Simulated latencies live in `app/config.py`. Replace them with real I/O
  (`httpx.AsyncClient`, `asyncpg`, etc.). Blocking calls inside `async def` stall the event loop.
