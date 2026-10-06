from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductUpdate
)
from app.services.product_service import (
    create_product,
    delete_product,
    get_product,
    get_products,
    update_product
)


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return create_product(db, product)


@router.get(
    "/",
    response_model=list[ProductResponse]
)
def list_products(
    skip: int = 0,
    limit: int = 20,
    search: str | None = None,
    db: Session = Depends(get_db)
):
    return get_products(
        db,
        skip=skip,
        limit=limit,
        search=search
    )


@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = get_product(db, product_id)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return product


@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def update(
    product_id: int,
    product_data: ProductUpdate,
    db: Session = Depends(get_db)
):
    product = get_product(db, product_id)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return update_product(
        db,
        product,
        product_data
    )


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = get_product(db, product_id)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    delete_product(db, product)