"""
services/database/operations.py
Here i will keep all the database operations in this place to easy to access
I will make the functions related to the
data insert, update or delete in this package
"""

from .user_data.operation import (
    add_new_user_row,
    get_user_row_by_phone_no,
    get_user_row_by_user_id,
)

from .brand_data.operation import (
    add_one_brand_row,
    get_all_brands_id_name,
    get_one_brand_row_by_id,
)

from .category_data.operation import (
    add_one_category_row,
    get_one_category_row_by_name,
    get_all_category_names,
)

from .product_data.operation import (
    add_one_product_row,
    get_product_out_public_schema_row,
    get_product_detail_out_public_schema_row,
)

from .product_image_data.operation import (
    add_product_thumbnail_image_row,
    add_product_thumbnail_external_url,
    add_product_gallery_image_rows,
)

__all__ = [
    "add_new_user_row",
    "get_user_row_by_phone_no",
    "get_user_row_by_user_id",
    "add_one_brand_row",
    "get_all_brands_id_name",
    "get_one_brand_row_by_id",
    "add_one_category_row",
    "get_one_category_row_by_name",
    "get_all_category_names",
    "add_one_product_row",
    "get_product_out_public_schema_row",
    "add_product_thumbnail_image_row",
    "add_product_thumbnail_external_url",
    "add_product_gallery_image_rows",
    "get_product_detail_out_public_schema_row",
]
