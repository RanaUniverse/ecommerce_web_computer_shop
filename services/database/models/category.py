"""
services/database/models/category.py
Here i will make the category table
this category will the place in which
the products will insert
"""

from typing import TYPE_CHECKING

from sqlmodel import (
    Field,
    SQLModel,
    Relationship,
)

from utils.general_utils import (
    current_posix_time,
    generate_hex_uuid4,
)

if TYPE_CHECKING:
    from .product import ProductModel


class CategoryModel(SQLModel, table=True):
    """
    The relation between category and product are like
    one category can have many or no product at all
    """

    __tablename__ = "category_data"  # type: ignore

    id_: str | None = Field(
        default_factory=generate_hex_uuid4,
        primary_key=True,
    )
    name: str = Field(index=True)
    description: str | None = Field(default=None)

    created_time: int = Field(default_factory=current_posix_time)

    products: list["ProductModel"] = Relationship(back_populates="category")
