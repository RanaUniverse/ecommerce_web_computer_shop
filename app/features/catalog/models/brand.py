"""
app/features/catalog/models/brand.py

Brand related table class will be here
"""

"""
services/database/brand_data/model.py
"""

from typing import TYPE_CHECKING, Any


from sqlmodel import (
    Field,
    Relationship,
    SQLModel,
)


from utils.general_utils import (
    generate_hex_uuid4,
)

if TYPE_CHECKING:
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

    logo_filename: str | None = Field(default=None)

    product_obj: list["ProductModel"] = Relationship(
        back_populates="brand_obj",
    )

    def model_post_init(self, context: Any) -> None:
        if not self.name:
            return None

        self.name = self.name.strip()
