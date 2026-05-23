"""
services/database/product_image_data/operation.py
Here i will make the table of the product_image and then
i will insert the row of image location and data
"""

from sqlmodel import Session, select


from ..core import engine

from ..models import (
    ProductGalleryImageModel,
    ProductThumbnailImageModel,
)


from utils.custom_logger import logger


def add_one_product_image_row(
    product_image_obj: ProductGalleryImageModel,
) -> ProductGalleryImageModel | None:

    with Session(engine) as session:
        try:
            session.add(product_image_obj)
            session.commit()
            session.refresh(product_image_obj)

            return product_image_obj

        except Exception as e:
            logger.error(f"Failed to save product image: {e}")
            return None


def add_product_thumbnail_image_row(
    thumbnail_obj: ProductThumbnailImageModel,
) -> ProductThumbnailImageModel | None:
    """
    It will try to insert the thumbnail_img obj into its row
    """
    with Session(engine) as session:
        try:
            session.add(thumbnail_obj)
            session.commit()
            session.refresh(thumbnail_obj)
            return thumbnail_obj

        except Exception as e:
            logger.error(f"Failed to save into thumbnail image row in db, {e}")
            return None


def product_thumbnail_img_row(
    product_id: str,
) -> ProductGalleryImageModel | None:
    """
    Before calling this i need to make sure product_id
    is present so that it will not cause issue of not found
    """
    with Session(engine) as session:
        statement = select(ProductGalleryImageModel).where(
            ProductGalleryImageModel.product_id == product_id
        )
        obj = session.exec(statement).first()
        return obj
