"""
services/database/controllers/__init__.py
I will make the functions related to the
data insert, update or delete in this package
"""

from .category import add_one_category_row
from .product import add_one_product_row
from .user import add_new_user_row

__all__ = [
    "add_new_user_row",
    "add_one_category_row",
    "add_one_product_row",
]
