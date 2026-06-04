"""
app/shared/utils/custom_logger.py
Here i will make my own logger for my own usecase
"""

import logging


from ..config import config_settings, TEST_DIR

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    fmt="{asctime} - {levelname} - {name} - {filename} - {lineno} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)

LOG_FILE_NAME = config_settings.log_file_name

if config_settings.enable_file_logging:
    file_handler = logging.FileHandler(
        filename=TEST_DIR / LOG_FILE_NAME,
        mode="a",
        encoding="utf-8",
    )
    logger.addHandler(file_handler)
    file_handler.setFormatter(formatter)


if config_settings.enable_console_logging:
    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)
    console_handler.setFormatter(formatter)


if __name__ == "__main__":
    logger.debug("Somethings Happens")
