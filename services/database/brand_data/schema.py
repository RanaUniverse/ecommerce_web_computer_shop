"""
services/database/brand_data/schema.py
"""

from sqlmodel import SQLModel


class BrandMinimal(SQLModel):
    """
    this to shows the brand name and link only
    """

    id_: str
    name: str
