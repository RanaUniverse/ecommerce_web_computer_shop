"""
app/features/catalog/models/product_image.py

Product gallery, thumbnail image both type will be here
"""

from typing import TYPE_CHECKING


from sqlmodel import Field, Relationship


from ..schema.image import ImageBase

if TYPE_CHECKING:
    from .product import ProductModel


class ProductThumbnailImageModel(ImageBase, table=True):
    __tablename__ = "product_thumbnail_image_data"  # type: ignore

    product_id: str = Field(
        foreign_key="product_data.id_",
        index=True,
        unique=True,
    )

    product_obj: "ProductModel" = Relationship(
        back_populates="product_thumbnail_image_obj",
    )


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
