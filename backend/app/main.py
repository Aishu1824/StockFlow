from fastapi import FastAPI
app=FastAPI(
    title="StockFlow API",
    description="Order and Inventory Management Platform",
    version="0.1.0",
)

@app.get("/health")
def health_check():
    return {
        "status":"healthy",
        "service":"StockFlow API"
    }