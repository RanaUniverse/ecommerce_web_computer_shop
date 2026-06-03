"""
app/shared/config.py
Here i will keep write the configurations informations
"""

from pathlib import Path


from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

# the test dir is for storing the logger and normal
# database sqlite .db file to store here
TEST_DIR = Path("test_data")
TEST_DIR.mkdir(parents=True, exist_ok=True)


class Settings(BaseSettings):
    """
    This is for the env values coming from the .env like environment files
    pydantic will care about this and it will works
    """

    # application hosting related things
    app_host: str
    app_port: int
    app_debug: bool
    app_secret_key: str

    # logging related
    enable_console_logging: bool = True
    enable_file_logging: bool = True
    log_file_name: str = "sample_log_file.txt"

    # from below the database related thigns will be calculated in the computed fields
    sqlite_filename: str = "demo_data.db"
    use_postgres: bool = False
    db_username: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    # below is pydantic's settings thigns for there of env path
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    @property
    def db_url(self) -> str:
        if self.use_postgres:
            POSTGRES_URL = (
                f"postgresql+psycopg2://"
                f"{self.db_username}:"
                f"{self.db_password}@"
                f"{self.db_host}:"
                f"{self.db_port}/"
                f"{self.db_name}"
            )
            return POSTGRES_URL

        else:
            sqlite_filepath = TEST_DIR / self.sqlite_filename
            SQLITE_URL = f"sqlite:///" f"{sqlite_filepath}"
            return SQLITE_URL


# i will use this below instance in all my needed module
config_settings = Settings()  # type: ignore


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

STATIC_PATH = Path("static")
