"""
app/features/catalog/models/category.py

Here the category related table code will be here
"""

"""
services/database/category_data/model.py
"""

from typing import TYPE_CHECKING, Any, Optional

from sqlmodel import (
    Field,
    Relationship,
)


from ....shared.utils.general_utils import (
    current_posix_time,
    generate_hex_uuid4,
)
from ..schema.category import CategoryCreateRequest

if TYPE_CHECKING:
    from .product import ProductModel
    from .image import CategoryThumbnailImageModel


class CategoryModel(
    CategoryCreateRequest,
    table=True,
):
    """
    The relation between category and product are like
    one category can have many or no product at all
    """

    __tablename__ = "category_data"  # type: ignore

    id_: str | None = Field(
        default_factory=generate_hex_uuid4,
        primary_key=True,
    )

    created_time: int = Field(
        default_factory=current_posix_time,
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

    category_thumbnail_image_obj: Optional["CategoryThumbnailImageModel"] = (
        Relationship(
            back_populates="product_obj",
        )
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
