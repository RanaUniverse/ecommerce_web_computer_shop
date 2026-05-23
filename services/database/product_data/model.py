"""
services/database/product_data/model.py
"""

from typing import (
    Optional,
    TYPE_CHECKING,
)

from sqlmodel import (
    Field,
    Relationship,
)


from .schema import ProductCreate

from utils.general_utils import (
    generate_hex_uuid4,
    current_posix_time,
)

if TYPE_CHECKING:
    from ..user_data.model import UserModel
    from ..brand_data.model import BrandModel
    from ..product_image_data.model import (
        ProductGalleryImageModel,
        ProductThumbnailImageModel,
    )
    from ..category_data.model import CategoryModel


class ProductModel(ProductCreate, table=True):
    """
    I make product will depends on the category table,
    many product can be from one category
    maybe some products are not any part of category
    """

    __tablename__ = "product_data"  # type: ignore

    id_: str | None = Field(
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

    creator_obj: Optional["UserModel"] = Relationship(
        back_populates="created_product_obj",
    )
