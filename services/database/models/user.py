"""
services/database/models/user.py
Here i will write to make user table
i will store the user's information
"""

from typing import TYPE_CHECKING


from flask_login import UserMixin  # type: ignore

from sqlmodel import (
    Field,
    SQLModel,
    Relationship,
)

from utils.general_utils import (
    generate_hex_uuid4,
    current_posix_time,
)

if TYPE_CHECKING:
    from .user_role import UserRoleModel


class UserModel(SQLModel, UserMixin, table=True):
    __tablename__ = "user_data"  # type: ignore

    id_: str = Field(default_factory=generate_hex_uuid4, primary_key=True)

    first_name: str
    middle_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)

    phone_no: str | None = Field(default=None, unique=True)
    email_id: str | None = Field(default=None, unique=True)
    username: str | None = Field(default=None, unique=True)

    password_hashed: str

    created_time: int = Field(default_factory=current_posix_time)

    user_role_obj: UserRoleModel = Relationship(back_populates="user_obj")

    def get_id(self) -> str:
        """
        This is the method which will run by the flask-login
        it will get the unique identificaiton per user thats why i make this
        as the docs say this here-
        https://flask-login.readthedocs.io/en/latest/#your-user-class
        """
        return self.id_
