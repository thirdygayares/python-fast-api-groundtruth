from typing import Optional
from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    name: str = Field(..., example="Coffee Mug")
    price: float = Field(..., ge=0, example=199.0)
    in_stock: bool = Field(default=True, example=True)

class ProductCreate(ProductBase):
    """
    Data the client must send when creating a product.
    """
    pass

class ProductUpdate(BaseModel):
    """
    Data the client can send when updating a product.
    """
    name: Optional[str] = None
    price: Optional[float] = Field(None, ge=0)
    in_stock: Optional[bool] = None

class Product(ProductBase):
    """
    Full Product representation returned by the API.
    Includes the `id`.
    """
    id: int