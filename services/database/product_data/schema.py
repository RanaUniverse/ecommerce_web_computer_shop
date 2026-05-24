"""
services/database/product_data/schema.py
Here i will make the schemas class so that i can sure
what what data i will share with whom,
ProductOut will have for public and admin differently
"""

from typing import Optional


from sqlmodel import (
    Field,
    SQLModel,
)


from ..product_image_data.schema import ProductThumbnailImageOut


class ProductBase(SQLModel):
    """
    This class is for sharable by all the Product related classes
    """

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
    """
    This is when one will entry to product in the database
    """

    quantity: int | None = Field(default=None)
    purchase_price: float | None = Field(default=None)

    creator_id: str | None = Field(
        default=None,
        foreign_key="user_data.id_",
        index=True,
    )


class ProductOutPublic(ProductBase):
    """
    This is because to shows the product details to user to buy
    """

    # the id_ will come from the database table thats why i keep here to shows public
    id_: str
    product_thumbnail_image_obj: Optional[ProductThumbnailImageOut] = None


class ProductOutAdmin(ProductCreate):
    """
    This is for showing the admin of product details to check
    statistics and also after create this will return for showing the data
    """

    id_: str


class ProductUpdate(SQLModel):
    """
    This is when admin will update the product information
    the field will come only have the value to update and all others
    are kept as none this is why all has None here
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
