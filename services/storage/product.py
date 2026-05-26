"""
services/storage/product.py
Here i will write the product related things to save in my storage and so on
"""

from typing import TypedDict

from pathlib import Path

from werkzeug.utils import secure_filename

from werkzeug.datastructures import FileStorage

from utils.config import (
    IMAGE_THUMBNAIL_PREFIX,
    PRODUCT_IMAGE_UPLOAD_ROOT,
)

from utils.config import ALLOWED_IMAGE_EXTENSIONS
from ..database.operations import (
    add_product_thumbnail_image_row,
    add_product_gallery_image_rows,
)

from services.database.models import (
    ProductThumbnailImageModel,
    ProductGalleryImageModel,
)
from utils.config import STATIC_PATH
from utils.custom_logger import logger


# i have use this in another place i need to refactor
class GalleryImageRecord(TypedDict):
    image_path: str
    order: int


def save_product_thumbnail_and_create_row(
    image_file: FileStorage,
    product_id: str,
    alt_text: str | None = None,
    creator_id: str | None = None,
    external_url: str | None = None,
) -> ProductThumbnailImageModel | None:
    """
    I want to save the image in the disk and also add the record simultaniously
    in the database thats why i keep both logic in this same function
    """

    image_filename_from_user = secure_filename(image_file.filename or "")
    image_extension = Path(image_filename_from_user).suffix.lower()
    image_name = f"{IMAGE_THUMBNAIL_PREFIX}{image_extension}"

    product_folder = STATIC_PATH / PRODUCT_IMAGE_UPLOAD_ROOT / product_id
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
    filepath_without_static = image_path.relative_to(STATIC_PATH)

    db_image_obj = ProductThumbnailImageModel(
        filepath=str(filepath_without_static),
        alt_text=alt_text,
        creator_id=creator_id,
        product_id=product_id,
        external_url=external_url,
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


def save_product_gallery_images_and_create_rows(
    image_files: list[FileStorage],
    product_id: str,
    creator_id: str | None = None,
) -> list[ProductGalleryImageModel] | None:
    """
    This function will directly save thsoe in the disk and then call a external
    function which will insert in the database.
    I will call this function so that it will save the gallery images for the
    products in the file storage in the disk in static there
    i keep creator_id -> None, for some advance case of hidden creator
    """

    # here i will append objects and make a list
    image_records: list[GalleryImageRecord] = []

    product_folder = STATIC_PATH / PRODUCT_IMAGE_UPLOAD_ROOT / product_id
    product_folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    for order, file in enumerate(image_files, start=1):

        if not file or not file.filename:
            # i wish this will never executes when i will must get file_storagae obj
            continue

        image_filename_from_user = secure_filename(file.filename or "")
        image_extension = Path(image_filename_from_user).suffix.lower().lstrip(".")

        if image_extension not in ALLOWED_IMAGE_EXTENSIONS:
            # i wish this will be not executs as flask-wtf will check this
            logger.error(
                msg="even flask-wtf check this still image came withtout image file"
                f"{image_filename_from_user}_{image_extension}"
            )
            continue

        image_name = f"{image_filename_from_user}"
        image_path = product_folder / image_name

        try:
            file.save(image_path)
            filepath_without_static = image_path.relative_to(STATIC_PATH)
            image_records.append(
                {
                    "image_path": str(filepath_without_static),
                    "order": order,
                },
            )

        except Exception as e:
            # i wished this should not happens
            logger.warning(f"Image save to disk fials, {e}")
            return None

    # this is outside the loop so taht it will not insert many time
    db_record = add_product_gallery_image_rows(
        image_records=image_records,
        product_id=product_id,
        creator_id=creator_id,
    )
    if not db_record:

        for record in image_records:
            try:
                file_to_delete = STATIC_PATH / record["image_path"]
                file_to_delete.unlink(missing_ok=True)

            except Exception as e:
                logger.warning(f"Cleanup failed for {record['image_path']}: {e}")

        return None

    else:
        # when it will send the obj, i will later change this to only len(obj)
        return db_record
