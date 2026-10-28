import logging
import time

from fastapi import Request

log = logging.getLogger("api")


async def timing_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    ms = (time.perf_counter() - start) * 1000
    response.headers["X-Process-Time-ms"] = f"{ms:.2f}"
    log.info("%s %s -> %s (%.1f ms)", request.method, request.url.path,
             response.status_code, ms)
    return response
