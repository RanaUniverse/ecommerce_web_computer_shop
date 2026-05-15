"""
services/database/models/product_image.py
Here i will write the code for the the product's image
how the images will store i willwrite
"""

from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

from utils.general_utils import current_posix_time, generate_hex_uuid4

if TYPE_CHECKING:
    from .product import ProductModel


class ProductImageModel(SQLModel, table=True):
    """
    for time of product createion the images will be uploded by admin
    the images will saved in the fodlers but the image's path
    will be keep recorded in the table so i did this

    creator_id: str | None = i use str or none so that i want some image i will not keep record of the creator's information

    i dont need createor_obj-> because i will not do search the owner of this image who uploded

    is_primary -> it say if the image will shows

    alt_text -> given by user when upload image

    filename-> if this present it means filepath will empty, i will generate the filepath by python code,

    external_url -> if i will want to give the image external url i will pass here

    """

    __tablename__ = "product_image_data"  # type: ignore

    id_: str = Field(default_factory=generate_hex_uuid4, primary_key=True)

    filename: str | None = Field(default=None)
    alt_text: str | None = Field(default=None)
    external_url: str | None = Field(default=None)

    is_primary: bool = Field(default=False)
    display_order: int | None = Field(default=0)

    creator_id: str | None = Field(default=None, foreign_key="user_data.id_")

    created_time: int = Field(default_factory=current_posix_time)

    product_id: str = Field(foreign_key="product_data.id_")
    product_obj: ProductModel = Relationship(
        back_populates="product_image_obj",
    )
