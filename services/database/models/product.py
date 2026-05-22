"""
services/database/models/product.py
Here i will write the code to make the product table
"""

from typing import (
    Optional,
    TYPE_CHECKING,
)

from sqlmodel import (
    Field,
    SQLModel,
    Relationship,
)

if TYPE_CHECKING:
    from .category import CategoryModel
    from .product_image import ProductGalleryImageModel, ProductThumbnailImageModel
    from .brand import BrandModel
    from .user import UserModel


from utils.general_utils import (
    generate_hex_uuid4,
    current_posix_time,
)

# class ProductBase(SQLModel):


# class ProductCrete(SQLModel):


# class ProductOutPublic():

# class ProductOutAdmin():


class ProductModel(SQLModel, table=True):
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

    name: str = Field(index=True)
    description: str | None = Field(default=None)
    hsn_no: int | None = Field(default=None)
    created_time: int = Field(default_factory=current_posix_time)

    quantity: int | None = Field(default=None)

    mrp_price: float | None = Field(default=None)
    purchase_price: float | None = Field(default=None)
    sell_price: float | None = Field(default=None)

    category_id: str | None = Field(
        default=None,
        foreign_key="category_data.id_",
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

    brand_id: str | None = Field(
        default=None,
        foreign_key="brand_data.id_",
    )
    brand_obj: Optional["BrandModel"] = Relationship(back_populates="product_obj")

    creator_id: str | None = Field(
        default=None,
        foreign_key="user_data.id_",
        index=True,
    )
    creator_obj: Optional["UserModel"] = Relationship(
        back_populates="created_product_obj",
    )
