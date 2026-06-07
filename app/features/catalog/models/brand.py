"""
app/features/catalog/models/brand.py

Brand related table class will be here
"""

from typing import TYPE_CHECKING, Any, Optional


from sqlmodel import (
    Field,
    Relationship,
    SQLModel,
)


from ....shared.utils.general_utils import generate_hex_uuid4

if TYPE_CHECKING:
    from .image import BrandThumbnailImageModel
    from .product import ProductModel


class BrandModel(
    SQLModel,
    table=True,
):

    __tablename__ = "brand_data"  # type: ignore

    id_: str = Field(
        default_factory=generate_hex_uuid4,
        primary_key=True,
    )

    name: str = Field(
        unique=True,
        index=True,
    )

    description: str | None = Field(default=None)

    website_url: str | None = Field(default=None)

    logo_filename: str | None = Field(
        default=None,
        description="Currently i have no idea how i will use this",
    )

    product_obj: list["ProductModel"] = Relationship(
        back_populates="brand_obj",
    )
    brand_thumbnail_image_obj: Optional["BrandThumbnailImageModel"] = Relationship(
        back_populates="brand_obj",
    )

    def model_post_init(self, context: Any) -> None:
        if not self.name:
            return None

        self.name = self.name.strip()
