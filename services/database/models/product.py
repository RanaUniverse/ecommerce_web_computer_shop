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


class ProductBase(SQLModel):

    name: str = Field(index=True)
    description: str | None = Field(default=None)
    hsn_no: int | None = Field(default=None)

    mrp_price: float | None = Field(default=None)
    sell_price: float | None = Field(default=None)

    brand_id: str | None = Field(
        default=None,
        foreign_key="brand_data.id_",
    )
    category_id: str | None = Field(
        default=None,
        foreign_key="category_data.id_",
    )


class ProductCreate(ProductBase):
    quantity: int | None = Field(default=None)
    purchase_price: float | None = Field(default=None)

    creator_id: str | None = Field(
        default=None,
        foreign_key="user_data.id_",
        index=True,
    )


class ProductOutPublic(ProductBase):
    pass


class ProductOutAdmin(ProductCreate):
    pass


class ProductUpdate(SQLModel):
    """
    This is when admin will update the product information
    """

    name: str | None = None
    description: str | None = None
    hsn_no: int | None = None

    quantity: int | None = None

    purchase_price: float | None = None
    sell_price: float | None = None
    mrp_price: float | None = None

    brand_id: str | None = None
    category_id: str | None = None


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

    created_time: int = Field(default_factory=current_posix_time)

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
