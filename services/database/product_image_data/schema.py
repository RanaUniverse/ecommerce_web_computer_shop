"""
services/database/product_image_data/schema.py
"""

from sqlmodel import (
    Field,
    SQLModel,
)


class ProductThumbnailImageOut(SQLModel):
    """
    this is what informaiton will go out for the thumbnail image
    """

    filepath: str | None = Field(default=None)
    external_url: str | None = Field(default=None)
    alt_text: str | None = Field(default=None)

    # filepath: str | None = None
    # alt_text: str | None = None
    # external_url: str | None = None


class ProductGalleryImageOut(SQLModel):
    """
    this is the minimal information for the gallery images
    later i will want admin will pass external link for the images to have
    shows in the gallery image not directly from my disk
    """

    display_order: int
    
    filepath: str | None = Field(default=None)
    external_url: str | None = Field(default=None)
    alt_text: str | None = Field(default=None)
