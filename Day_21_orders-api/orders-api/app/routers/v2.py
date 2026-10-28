"""v2: ASYNC API (async/await + background tasks)."""
import asyncio

from fastapi import APIRouter, BackgroundTasks, Depends

from ..deps import Database, get_db
from ..models import OrderIn, OrderOut
from ..tasks import send_confirmation

router = APIRouter(prefix="/api/v2", tags=["v2 (async)"])


@router.get("/users/{uid}")
async def get_user(uid: int, db: Database = Depends(get_db)):
    return await db.get_user(uid)


@router.get("/users")
async def get_many_users(ids: str, db: Database = Depends(get_db)):
    """Concurrent fan-out: ?ids=1,2,3 fetches all users in parallel."""
    uids = [int(i) for i in ids.split(",") if i.strip()]
    return await asyncio.gather(*(db.get_user(u) for u in uids))


@router.post("/orders", response_model=OrderOut)
async def create_order(order: OrderIn, bg: BackgroundTasks,
                       db: Database = Depends(get_db)):
    await db.get_user(1)
    bg.add_task(send_confirmation, order.customer_email)  # returns immediately
    return OrderOut(**order.model_dump())
