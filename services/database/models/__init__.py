"""
services/database/models/__init__.py
Here i will make the models ie the table in my sql table
"""

from .brand import BrandModel
from .category import CategoryModel
from .product import ProductModel
from .product_image import ProductImageModel
from .user import UserModel
from .user_role import UserRoleModel

__all__ = [
    "BrandModel",
    "CategoryModel",
    "ProductModel",
    "UserModel",
    "UserRoleModel",
    "ProductImageModel",
]
