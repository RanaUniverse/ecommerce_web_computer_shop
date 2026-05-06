"""
services/database/models/user.py
Here i will write to make user table
i will store the user's information
"""

from sqlmodel import (
    Field,
    SQLModel,
)

from utils.general_utils import (
    generate_hex_uuid4,
    current_posix_time,
)


class UserModel(SQLModel, table=True):
    __tablename__ = "user_data"  # type: ignore

    id_: str = Field(default_factory=generate_hex_uuid4, primary_key=True)

    first_name: str
    middle_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)

    created_time: int = Field(default_factory=current_posix_time)

    phone_no: str
    email_id: str | None
    username: str | None

    password_hashed: str
