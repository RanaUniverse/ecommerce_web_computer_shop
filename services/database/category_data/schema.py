"""
services/database/category_data/schema.py
"""

from sqlmodel import SQLModel, Field


class CategoryMinimal(SQLModel):
    """
    this is for showing the name and id to make clickable category
    """

    id_: str
    name: str | None = Field(default=None)
