"""
services/storage/product.py
Here i will write the product related things to save in my storage and so on
"""

from pathlib import Path

from werkzeug.utils import secure_filename

from werkzeug.datastructures import FileStorage

from utils.config import (
    THUMBNAIL_IMAGE_PREFIX,
    PRODUCT_IMAGE_UPLOAD_ROOT,
)

from ..database.controllers import add_one_product_image_row

from services.database.models import ProductImageModel
from utils.custom_logger import logger


def save_product_thumbnail(
    product_id: str,
    image_file: FileStorage,
) -> Path | None:
    """
    This will try to save the image in the system and then return the Path of this
    so that it can also be saved in the database
    """
    product_folder = PRODUCT_IMAGE_UPLOAD_ROOT / product_id
    product_folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    image_filename = secure_filename(image_file.filename or "")
    image_extension = Path(image_filename).suffix.lower()

    image_name = f"{THUMBNAIL_IMAGE_PREFIX}{image_extension}"

    image_path = product_folder / image_name

    try:
        image_file.save(image_path)
        return image_path

    except Exception:
        return None


def save_product_thumbnail_and_create_row(
    image_file: FileStorage,
    product_id: str,
    alt_text: str | None = None,
    creator_id: str | None = None,
) -> ProductImageModel | None:
    """
    i will pass the necessary details to save into
    the database row there i will use this
    thumbnail = true
    always else thumbnail will not saved
    """

    product_folder = PRODUCT_IMAGE_UPLOAD_ROOT / product_id
    product_folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    image_filename_from_user = secure_filename(image_file.filename or "")
    image_extension = Path(image_filename_from_user).suffix.lower()

    image_name = f"{THUMBNAIL_IMAGE_PREFIX}{image_extension}"

    image_path = product_folder / image_name
    print(image_path)
    print(str(image_path))
    try:
        image_file.save(image_path)

    except Exception as e:
        # i wished this should not happens
        logger.warning(f"Image save to disk fials, {e}")
        return None

    product_image_obj = ProductImageModel(
        filename=str(image_path),
        alt_text=alt_text,
        is_primary=True,
        creator_id=creator_id,
        product_id=product_id,
    )

    saved_row = add_one_product_image_row(
        product_image_obj=product_image_obj,
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
