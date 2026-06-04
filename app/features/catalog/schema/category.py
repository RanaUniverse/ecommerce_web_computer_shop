"""
app/features/catalog/schema/category.py

Here i will make the category information
"""

"""
services/database/category_data/schema.py
"""

from sqlmodel import (
    Field,
    SQLModel,
)


class CategoryMinimalOut(SQLModel):
    """
    this is for showing the name and id to make clickable category
    """

    id_: str
    name: str | None = Field(default=None)
