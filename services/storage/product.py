from pathlib import Path

from werkzeug.utils import secure_filename

from werkzeug.datastructures import FileStorage

from utils.config import THUMBNAIL_IMAGE_PREFIX, PRODUCT_IMAGE_UPLOAD_ROOT


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

    img_filename = secure_filename(image_file.filename or "")
    img_extension = Path(img_filename).suffix.lower()

    img_name = f"{THUMBNAIL_IMAGE_PREFIX}{img_extension}"

    img_path = product_folder / img_name

    try:
        image_file.save(img_path)
        return img_path

    except Exception:
        return None
