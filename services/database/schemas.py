"""
services/database/schema.py
I will keep all the schemas here so that i can easily import from this
module easily for all the db's schema
"""

from .product_data.schema import (
    ProductCreate,
    ProductOutPublic,
)

__all__ = [
    "ProductCreate",
    "ProductOutPublic",
]
