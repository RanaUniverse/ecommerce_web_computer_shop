"""
services/database/models/__init__.py
Here i will make the models ie the table in my sql table
"""

from .category import CategoryModel
from .product import ProductModel
from .user import UserModel

__all__ = [
    "CategoryModel",
    "ProductModel",
    "UserModel",
]
