from pydantic import BaseModel, EmailStr, Field


class OrderIn(BaseModel):
    customer_email: EmailStr
    item: str = Field(min_length=1, max_length=100)
    quantity: int = Field(gt=0, le=100)


class OrderOut(OrderIn):
    status: str = "created"
