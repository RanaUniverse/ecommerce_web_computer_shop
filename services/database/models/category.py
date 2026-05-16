"""
services/database/models/category.py
Here i will make the category table
this category will the place in which
the products will insert
"""

from typing import TYPE_CHECKING, Any, Optional

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
    name: str | None = Field(
        default=None,
        index=True,
        unique=True,
    )
    description: str | None = Field(default=None)

    # i use this to store bootstrap's icon value to shows later i will use svg or iamge
    icon_name: str | None = Field(default=None)

    private_note: str | None = Field(default=None)

    created_time: int = Field(default_factory=current_posix_time)

    parent_id: str | None = Field(
        default=None,
        foreign_key="category_data.id_",
    )

    parent_obj: Optional["CategoryModel"] = Relationship(
        back_populates="child_obj",
        sa_relationship_kwargs={
            "remote_side": "CategoryModel.id_",
        },
    )

    child_obj: list["CategoryModel"] = Relationship(
        back_populates="parent_obj",
    )

    product_obj: list["ProductModel"] = Relationship(
        back_populates="category_obj",
    )

    def model_post_init(self, context: Any) -> None:
        """
        I make this so that the name of the category will be
        good to store with some no space logic
        """
        # return super().model_post_init(context)
        if not self.name:
            # this exit just for i dont want to run this
            return None

        no_space_name = self.name.strip()
        self.name = no_space_name
