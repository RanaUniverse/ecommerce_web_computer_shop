"""
app/features/catalog/schema/brand.py

Brand related information for the product will be here
"""

from sqlmodel import SQLModel


class BrandMinimalOut(SQLModel):
    """
    this to shows the brand name and link only
    """

    id_: str
    name: str
