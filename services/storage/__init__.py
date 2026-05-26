"""
services/storage/__init__.py
Here i will write some logic or funcion to insert item's or
product or category or different image to store in the filesystem
later i will able to change this to api if external
"""

from .product import (
    save_product_thumbnail_and_create_row,
    save_product_gallery_images_and_create_rows,
)

__all__ = [
    "save_product_thumbnail_and_create_row",
    "save_product_gallery_images_and_create_rows",
]
