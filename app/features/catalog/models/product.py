"""
app/features/catalog/models/product.py

Product related table will be here
"""

from typing import (
    Optional,
    TYPE_CHECKING,
)

from sqlmodel import (
    Field,
    Relationship,
)


from ..schema.product import ProductCreate

from utils.general_utils import (
    generate_hex_uuid4,
    current_posix_time,
)

if TYPE_CHECKING:
    from .image import (
        ProductThumbnailImageModel,
        ProductGalleryImageModel,
    )
    from .brand import BrandModel
    from .category import CategoryModel


class ProductModel(
    ProductCreate,
    table=True,
):
    """
    I make product will depends on the category table,
    many product can be from one category
    maybe some products are not any part of category
    """

    __tablename__ = "product_data"  # type: ignore

    id_: str = Field(
        default_factory=generate_hex_uuid4,
        primary_key=True,
    )

    created_time: int = Field(
        default_factory=current_posix_time,
    )

    brand_obj: Optional["BrandModel"] = Relationship(
        back_populates="product_obj",
    )

    category_obj: Optional["CategoryModel"] = Relationship(
        back_populates="product_obj",
    )

    product_gallery_image_obj: list["ProductGalleryImageModel"] = Relationship(
        back_populates="product_obj",
    )

    product_thumbnail_image_obj: Optional["ProductThumbnailImageModel"] = Relationship(
        back_populates="product_obj",
    )
