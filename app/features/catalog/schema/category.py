"""
app/features/catalog/schema/category.py

Here i will make the category information
"""

from sqlmodel import (
    Field,
    SQLModel,
)


class CategoryCreateRequest(SQLModel):
    """
    This is here the informations which will need
    to create the Category information
    Comes from staff/admin at time of creating
    """

    name: str | None = Field(
        default=None,
        index=True,
        unique=True,
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
        foreign_key="category_data.id_",
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
