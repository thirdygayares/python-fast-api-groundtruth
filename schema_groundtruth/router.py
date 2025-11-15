from typing import List
from fastapi import APIRouter, HTTPException

from product_schema import Product, ProductCreate, ProductUpdate
from product_service import list_products, create_product, get_product, update_product, \
    delete_product

router = APIRouter(
    prefix="/api/products",
    tags=["products"],
)

# Scenario 2: list products
@router.get("/", response_model=List[Product])
def get_products():
    return list_products()

# Scenario 1: create product
@router.post("/", response_model=Product, status_code=201)
def create_product_endpoint(payload: ProductCreate):
    return create_product(payload)

# Scenario 2 (part 2): get single product
@router.get("/{product_id}", response_model=Product)
def get_product_endpoint(product_id: int):
    product = get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Scenario 3: update product
@router.put("/{product_id}", response_model=Product)
def update_product_endpoint(product_id: int, payload: ProductUpdate):
    product = update_product(product_id, payload)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# delete product
@router.delete("/{product_id}", status_code=204)
def delete_product_endpoint(product_id: int):
    ok = delete_product(product_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Product not found")
    return