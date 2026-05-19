"""
services/database/models/product_image.py
Here i will write the code for the the product's image
how the images will store i willwrite
"""

from typing import TYPE_CHECKING

from sqlmodel import (
    Field,
    Relationship,
)

if TYPE_CHECKING:
    from .product import ProductModel

from .base import ImageBase

# class ProductImageModel(ImageBase, table=True):
#     __tablename__ = "product_image_data"  # type: ignore

#     display_order: int | None = Field(default=0)

#     product_id: str = Field(foreign_key="product_data.id_")

#     product_obj: "ProductModel" = Relationship(
#         back_populates="product_image_obj",
#     )


class ProductGalleryImageModel(ImageBase, table=True):
    __tablename__ = "product_gallery_image_data"  # type: ignore

    display_order: int | None = Field(default=0)

    product_id: str = Field(
        foreign_key="product_data.id_",
        index=True,
    )

    product_obj: "ProductModel" = Relationship(
        back_populates="product_gallery_image_obj",
    )
