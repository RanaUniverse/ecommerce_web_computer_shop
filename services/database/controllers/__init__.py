"""
services/database/controllers/__init__.py
I will make the functions related to the
data insert, update or delete in this package
"""

from .brand import (
    add_one_brand_row,
    get_all_brand_names,
    get_all_products_of_brand,
    get_one_brand_row_by_id,
    get_all_brands_id_name,
)

from .category import (
    add_one_category_row,
    get_one_category_row_by_name,
    get_all_category_names,
)
from .product import add_one_product_row, get_one_product_row_by_id
from .product_image import (
    add_one_product_image_row,
    product_thumbnail_img_row,
    add_product_thumbnail_image_row,
)

from .user import (
    add_new_user_row,
    get_user_row_by_email_id,
    get_user_row_by_phone_no,
    get_user_row_by_username,
    get_user_row_by_user_id,
)

__all__ = [
    "add_new_user_row",
    "add_one_category_row",
    "add_one_product_row",
    "get_user_row_by_email_id",
    "get_user_row_by_phone_no",
    "get_user_row_by_username",
    "get_user_row_by_user_id",
    "get_one_category_row_by_name",
    "get_all_category_names",
    "add_one_brand_row",
    "get_all_brand_names",
    "get_all_products_of_brand",
    "get_one_brand_row_by_id",
    "get_all_brands_id_name",
    "add_one_product_image_row",
    "get_one_product_row_by_id",
    "product_thumbnail_img_row",
    "add_product_thumbnail_image_row",
]
