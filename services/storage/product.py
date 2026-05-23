"""
services/storage/product.py
Here i will write the product related things to save in my storage and so on
"""

from pathlib import Path

from werkzeug.utils import secure_filename

from werkzeug.datastructures import FileStorage

from utils.config import (
    IMAGE_THUMBNAIL_PREFIX,
    PRODUCT_IMAGE_UPLOAD_ROOT,
)

from ..database.operations import add_product_thumbnail_image_row

from services.database.models import ProductThumbnailImageModel
from utils.custom_logger import logger


def save_product_thumbnail_and_create_row(
    image_file: FileStorage,
    product_id: str,
    alt_text: str | None = None,
    creator_id: str | None = None,
) -> ProductThumbnailImageModel | None:
    """
    I want to save the image in the disk and also add the record simultaniously
    in the database thats why i keep both logic in this same function
    """

    image_filename_from_user = secure_filename(image_file.filename or "")
    image_extension = Path(image_filename_from_user).suffix.lower()
    image_name = f"{IMAGE_THUMBNAIL_PREFIX}{image_extension}"

    product_folder = PRODUCT_IMAGE_UPLOAD_ROOT / product_id
    product_folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    image_path = product_folder / image_name

    try:
        image_file.save(image_path)

    except Exception as e:
        # i wished this should not happens
        logger.warning(f"Image save to disk fials, {e}")
        return None

    db_image_obj = ProductThumbnailImageModel(
        filepath=str(image_path),
        alt_text=alt_text,
        creator_id=creator_id,
        product_id=product_id,
    )

    saved_row = add_product_thumbnail_image_row(
        thumbnail_obj=db_image_obj,
    )
    # if db insert fails i need to delte the image from storage
    if not saved_row:

        try:
            image_path.unlink(
                missing_ok=True,
            )
        except Exception as e:
            logger.warning("Image should delete when the db insertion fails", str(e))
            # i am not understand what to do here
            pass

        return None

    return saved_row
