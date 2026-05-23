"""
services/database/models.py
Here i will keep import all the modles my table has
so that i can easily track all the tables
and then i can also use this to this in the
alembic>env py file
"""

from .brand_data.model import BrandModel
from .category_data.model import CategoryModel
from .product_data.model import ProductModel
from .product_image_data.model import (
    ProductGalleryImageModel,
    ProductThumbnailImageModel,
)
from .user_data.model import UserModel
from .user_role_data.model import UserRoleModel

__all__ = [
    "BrandModel",
    "CategoryModel",
    "ProductModel",
    "UserModel",
    "UserRoleModel",
    "ProductGalleryImageModel",
    "ProductThumbnailImageModel",
]
