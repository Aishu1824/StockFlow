from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: Decimal
    sku: str


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: Decimal
    sku: str

    model_config = ConfigDict(from_attributes=True)