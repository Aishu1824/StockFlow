from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def create_product(
    db: Session,
    product_data: ProductCreate
):
    product = Product(
        name=product_data.name,
        description=product_data.description,
        price=product_data.price,
        sku=product_data.sku
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def get_product(
    db: Session,
    product_id: int
):
    statement = select(Product).where(
        Product.id == product_id
    )

    return db.scalar(statement)


def get_products(
    db: Session,
    skip: int = 0,
    limit: int = 20,
    search: str | None = None
):
    statement = select(Product)

    if search:
        statement = statement.where(
            Product.name.ilike(f"%{search}%")
        )

    statement = (
        statement
        .offset(skip)
        .limit(limit)
    )

    return list(db.scalars(statement).all())


def update_product(
    db: Session,
    product: Product,
    product_data: ProductUpdate
):
    updates = product_data.model_dump(
        exclude_unset=True
    )

    for field, value in updates.items():
        setattr(product, field, value)

    db.commit()
    db.refresh(product)

    return product


def delete_product(
    db: Session,
    product: Product
):
    db.delete(product)
    db.commit()