from fastapi import FastAPI

from app.api.products import router as product_router


app = FastAPI(
    title="StockFlow API",
    description="Order and Inventory Management Platform",
    version="0.1.0"
)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(product_router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "stockflow-api"
    }