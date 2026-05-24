"""
utils/config.py
i want to use this as settings values of like
some file name if i will use like this or some extra and so on
"""

from pathlib import Path

TEST_DIR = Path("test_data")
TEST_DIR.mkdir(parents=True, exist_ok=True)


# Below is for the log file
ENABLE_CONSOLE_LOGGING: bool = True
ENABLE_FILE_LOGGING: bool = True
LOG_FILE_NAME: str = "sample_log_file.txt"


# Below is for related with the database

# if i will want to use postgres i will use true else
# if i want to use sqlite i will use false
IS_USING_POSTGRES: bool = True


sqlite_file_name = TEST_DIR / "demo_data.db"
SQLITE_DATABASE_URL = f"sqlite:///{sqlite_file_name}"


DB_USERNAME = "rana"
DB_PASSWORD = "abc"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "r"

POSTGRES_DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

if IS_USING_POSTGRES:
    DATABASE_URL = POSTGRES_DATABASE_URL
else:
    DATABASE_URL = SQLITE_DATABASE_URL


# Below i will write the values that will need for the
# flask run from main.py some values

HOST_ADDRESS = "0.0.0.0"
PORT_INT = 9999
DEBUG_BOOL: bool = True


# Below are for the websit's content like brand and so on
# BRAND_NAME = "Rana Universe"


# Below is need for flask's app config
SECRET_KEY = "This is secret value."


# some settings like values which i will pass in many places
MESSAGE_ADMIN_CONTACT = "Please contact the administrator for assistance."
MESSAGE_HELP_CENTER = "If the problem continues, please contact the Help Center."
MESSAGE_TRY_AGAIN = "Something went wrong. Please try again later."


# where the images of the products will saved
# i remove the static/ because by default i will keep those in static
PRODUCT_IMAGE_UPLOAD_ROOT = Path("uploads/images/product")
CATEGORY_IMAGE_UPLOAD_ROOT = Path("uploads/images/category")

ALLOWED_IMAGE_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp",
}

IMAGE_THUMBNAIL_PREFIX = "product_thumbnail"

# This image is in the static folder which i will use in the url_for
IMAGE_NOT_FOUND_IMAGE_PATH = "images/image_not_found.png"
