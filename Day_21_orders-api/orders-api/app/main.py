import logging

from fastapi import FastAPI

from .middleware import timing_middleware
from .routers import v1, v2

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Orders API", version="2.0",
              description="Sync (v1) vs async (v2) comparison project.")
app.middleware("http")(timing_middleware)
app.include_router(v1.router)
app.include_router(v2.router)


@app.get("/health", tags=["meta"])
async def health():
    return {"status": "ok"}
