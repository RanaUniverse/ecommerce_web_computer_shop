"""
app/features/catalog/schema/category.py

Here i will make the category information
"""

from typing import Optional


from sqlmodel import (
    Field,
    SQLModel,
)


from .image import CategoryThumbnailImageOut


class CategoryCreateRequest(SQLModel):
    """
    This is here the informations which will need
    to create the Category information
    Comes from staff/admin at time of creating
    """

    name: str | None = Field(
        default=None,
    )
    description: str | None = Field(
        default=None,
    )
    icon_name: str | None = Field(
        default=None,
        description="Here i will prvode the bs5's icon name to shows if any",
    )
    private_note: str | None = Field(
        default=None,
        description="To Store some private informaiotn about this category",
    )
    parent_id: str | None = Field(
        default=None,
        description=(
            "Actually from the parent category name the id will "
            "generate there at beginnign"
        ),
    )


class CategoryUpdateRequest(SQLModel):
    """
    What what things to update only i need to pass those
    For admin only
    """

    name: str | None = None
    description: str | None = None
    icon_name: str | None = None
    private_note: str | None = None
    parent_id: str | None = None


class CategoryOutMinimal(SQLModel):
    """
    This is for showing the category name and its link with bs icon
    to shows the category name where user can press and see more
    information about the category to see more things later
    """

    id_: str
    name: str = Field(
        description="Shows the name with clickable link with the id_",
    )
    icon_name: str | None
    description: str | None = Field(
        description="I will use this value to shows as popup text.",
    )


class CategoryOutAdmin(SQLModel):
    """
    Full category information for admin view.
    Admin sees everything including private fields and timestamps.
    """

    model_config = {"from_attributes": True}

    id_: str
    name: str | None
    description: str | None
    icon_name: str | None
    private_note: str | None
    parent_id: str | None
    created_time: int

    parent_obj: Optional["CategoryOutMinimal"] = None
    child_obj: list["CategoryOutMinimal"] = []

    category_thumbnail_image_obj: Optional["CategoryThumbnailImageOut"] | None = None
