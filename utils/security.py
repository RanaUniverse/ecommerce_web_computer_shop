"""
utils/security.py
Here i will write the function or somethigns related to
encryption, hashing or somethign like this
"""

from services.extensions import bcrypt


def generate_password_hash(password: str) -> str:
    """
    it will take the password and it will generate the password
    flask_bcruypt library is doign the work in behind
    """
    hashed_password = bcrypt.generate_password_hash(  # type: ignore
        password=password,
    ).decode()
    return hashed_password


def verify_hashed_password(hashed_password: str, password: str):
    is_password_match = bcrypt.check_password_hash(  # type: ignore
        hashed_password,
        password,
    )
    return is_password_match
