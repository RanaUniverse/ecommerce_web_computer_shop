"""
services/database/controllers/product_image.py
Here i will make the table of the product_image and then
i will insert the row of image locaion and data
"""

from sqlmodel import Session


from ..core import engine
from ..models import ProductImageModel


from utils.custom_logger import logger


def add_one_product_image_row(
    product_image_obj: ProductImageModel,
) -> ProductImageModel | None:

    with Session(engine) as session:
        try:
            session.add(product_image_obj)
            session.commit()
            session.refresh(product_image_obj)

            return product_image_obj

        except Exception as e:
            logger.error(f"Failed to save product image: {e}")
            return None
