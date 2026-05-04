"""
This is utils.custom_logger.py file
I make this for checking how this will work
"""

import logging


from .config import (
    ENABLE_CONSOLE_LOGGING,
    ENABLE_FILE_LOGGING,
    LOG_FILE_NAME,
    TEST_DIR,
)

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    fmt="{asctime} - {levelname} - {name} - {filename} - {lineno} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)


if ENABLE_FILE_LOGGING:
    file_handler = logging.FileHandler(
        filename=TEST_DIR / LOG_FILE_NAME,
        mode="a",
        encoding="utf-8",
    )
    logger.addHandler(file_handler)
    file_handler.setFormatter(formatter)


if ENABLE_CONSOLE_LOGGING:
    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)
    console_handler.setFormatter(formatter)


if __name__ == "__main__":
    logger.debug("Somethings Happens")
