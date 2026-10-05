from fastapi import FastAPI

from app.api.products import router as product_router


app = FastAPI(
    title="StockFlow API",
    description="Order and Inventory Management Platform",
    version="0.1.0"
)


app.include_router(product_router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "stockflow-api"
    }