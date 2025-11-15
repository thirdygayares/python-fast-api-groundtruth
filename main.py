from fastapi import FastAPI
from schema_groundtruth.router import router as product_router

app = FastAPI()
app.include_router(product_router)