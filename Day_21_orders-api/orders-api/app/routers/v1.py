"""v1: ORIGINAL synchronous API (kept as baseline)."""
from fastapi import APIRouter, Depends

from ..deps import Database, get_db
from ..models import OrderIn, OrderOut
from ..tasks import send_confirmation_sync

router = APIRouter(prefix="/api/v1", tags=["v1 (sync, deprecated)"], deprecated=True)


@router.get("/users/{uid}")
def get_user(uid: int, db: Database = Depends(get_db)):
    return db.get_user_sync(uid)


@router.post("/orders", response_model=OrderOut)
def create_order(order: OrderIn, db: Database = Depends(get_db)):
    db.get_user_sync(1)
    send_confirmation_sync(order.customer_email)  # blocks the response
    return OrderOut(**order.model_dump())
