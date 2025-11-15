from typing import List, Optional

from product_schema import Product, ProductCreate, ProductUpdate

PRODUCTS: List[Product] = []
_next_id = 1

def list_products() -> List[Product]:
    return PRODUCTS

def create_product(data: ProductCreate) -> Product:
    global _next_id
    new_product = Product(id=_next_id, **data.model_dump())
    _next_id += 1
    PRODUCTS.append(new_product)
    return new_product

def get_product(product_id: int) -> Optional[Product]:
    for product in PRODUCTS:
        if product.id == product_id:
            return product
    return None

def update_product(product_id: int, data: ProductUpdate) -> Optional[Product]:
    product = get_product(product_id)
    if not product:
        return None

    stored_data = product.model_dump()
    update_data = data.model_dump(exclude_unset=True)
    stored_data.update(update_data)

    updated_product = Product(**stored_data)
    index = PRODUCTS.index(product)
    PRODUCTS[index] = updated_product
    return updated_product

def delete_product(product_id: int) -> bool:
    product = get_product(product_id)
    if not product:
        return False
    PRODUCTS.remove(product)
    return True