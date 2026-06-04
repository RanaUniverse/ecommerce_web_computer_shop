"""
app/features/catalog/schema/product_image.py

Here product image's thumbnail & gallery both will
defined here in this module
"""

from pydantic import model_validator


from sqlmodel import (
    Field,
    SQLModel,
)


from utils.general_utils import (
    current_posix_time,
)


class ImageSourceSchema(SQLModel):
    """
    I make this so that i can use this to check the image is exists correctly
    i will use the validator so that it will use in both in and out schema
    """

    filepath: str | None = Field(default=None)
    external_url: str | None = Field(default=None)

    alt_text: str | None = Field(default=None)

    @model_validator(mode="after")
    def validate_image_location(self):
        if not self.filepath and not self.external_url:
            raise ValueError(
                "Image's FIlepath or external url one of those must be present."
            )
        return self


class ImageBase(ImageSourceSchema):
    """
    This is generic class there for thumbnail and gallery both
    """

    creator_id: str | None = Field(
        default=None,
        foreign_key="user_data.id_",
    )

    created_time: int = Field(
        default_factory=current_posix_time,
    )


class ProductThumbnailImageOut(ImageSourceSchema):
    """
    this is what informaiton will go out for the thumbnail image
    """

    pass


class ProductGalleryImageOut(ImageSourceSchema):
    """
    this is the minimal information for the gallery images
    later i will want admin will pass external link for the images to have
    shows in the gallery image not directly from my disk
    """

    display_order: int
