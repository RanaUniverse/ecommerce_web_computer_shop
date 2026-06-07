"""
app/features/catalog/schema/brand.py

Brand related information for the product will be here
"""

from sqlmodel import (
    SQLModel,
    Field,
)


class BrandCreateRequest(SQLModel):
    """
    For creating the Brand the information i will pass here
    """

    name: str = Field(
        unique=True,
        index=True,
    )
    description: str | None = Field(
        default=None,
        description="I will shows some informaiton to use on mouse over",
    )
    website_url: str | None = Field(
        default=None,
    )
    logo_filename: str | None = Field(
        default=None,
        description="Currently i have no idea how i will use this",
    )


class BrandUpdateRequest(SQLModel):
    """
    For update the brand informaiton for admin only
    """

    name: str | None = None
    description: str | None = None
    website_url: str | None = None
    logo_filename: str | None = None


class BrandOutMinimal(SQLModel):
    """
    This is for showing the brand name and basic
    information to the user
    """

    id_: str
    name: str = Field(
        description="Shows the brand name with clickable link using id_",
    )
    description: str | None = Field(
        default=None,
        description="I will use this value to shows as popup text.",
    )
    logo_filename: str | None = None
