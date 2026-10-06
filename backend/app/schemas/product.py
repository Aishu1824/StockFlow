from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=200)
    description: str | None = None
    price: Decimal = Field(gt=0)
    sku: str = Field(min_length=2, max_length=100)


class ProductUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=200
    )

    description: str | None = None

    price: Decimal | None = Field(
        default=None,
        gt=0
    )

    sku: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: Decimal
    sku: str

    model_config = ConfigDict(from_attributes=True)