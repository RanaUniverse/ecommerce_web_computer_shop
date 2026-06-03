"""
app/shared/config.py
Here i will keep write the configurations informations
"""

from pathlib import Path


from pydantic import BaseModel

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

# the test dir is for storing the logger and normal
# database sqlite .db file to store here
TEST_DIR = Path("test_data")
TEST_DIR.mkdir(parents=True, exist_ok=True)


class ShopDetails(BaseModel):
    """
    This is where i will keep the name of the details of the shop
    like name and very important constants for the business this is for

    This model contains details that are displayed throughout the
    application, such as contact information, address, branding,
    social media links, and business-related settings.
    """

    brand_name: str = "Rana Universe"

    shop_name: str = "Rana Computer Shop"
    shop_tagline: str = "Computers, Accessories & Tech Solutions"

    shop_description: str = (
        "Trusted computer shop for laptops, accessories, "
        "gaming products, and repair services."
    )

    shop_gstin: str = "XYZ123ABC789RANA"
    shop_pan: str = "ABCDE1234Z"

    shop_phone: str = "9988776655"
    shop_whatsapp: str = "9998887776"
    shop_email: str = "example+shop@gmail.com"
    shop_support_email: str = "example+support@gmail.com"

    shop_address: str = "Kalinagar NH 116 B"
    shop_city: str = "City of Rana"
    shop_state: str = "West Bengal"
    shop_country: str = "India"
    shop_pincode: str = "721430"

    shop_full_address: str = (
        "Rana Universe, Contai-Nandakumar Road, Henria, "
        "Purba Medinipur, West Bengal 721430, India"
    )

    shop_url_facebook: str = "https://facebook.com/RanaUniverse"
    shop_url_instagram: str = "https://instagram.com/RanaUniverse"
    shop_url_telegram: str = "https://t.me/RanaUniverse"
    shop_url_youtube: str = "https://youtube.com/@RanaUniverse"

    free_delivery_min_amount: int = 1000

    shop_opening_time: str = "10 AM - 10 PM"
    shop_online_support_timing: str = "8 AM - 6 PM"

    @property
    def whatsapp_link(self) -> str:
        return f"https://wa.me/91{self.shop_whatsapp}"


# i will use this instance everywhere later
shop_details = ShopDetails()


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
