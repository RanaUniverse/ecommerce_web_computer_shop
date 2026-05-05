"""
utils/general_utils.py
Here i will write some commonly use function or like this thigns
i will use this to import those in some others modeules
"""

import time
from uuid import uuid4


def generate_hex_uuid4() -> str:
    """
    This will generate the uuid4 with a string value
    i will use this for random data in the columns mainly in database
    """
    return str(uuid4().hex)


def current_posix_time():
    """
    This will generate the current time as of posix
    1 january 1970 as of utc
    """
    current_time_int = int(time.time())
    return current_time_int
