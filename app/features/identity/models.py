"""
app/features/identity/models.py
Here i will write the class for my table in the database
i will mainly import the schema creted in schema.py


For User Role:

customer -> it will by default value
business -> for shows low prices than others customer
staff -> access to see who has give orders and what thigns
manager -> allow to change product price, add product and details
owner -> shows statistics and data
developer -> its for me actually to get some inner things
"""

from typing import Optional


from flask_login import UserMixin  # type: ignore

from sqlmodel import (
    Field,
    SQLModel,
    Relationship,
)


from .schema import (
    UserCreate,
)

from ...shared.utils.general_utils import (
    current_posix_time,
    generate_hex_uuid4,
)

from .utils import user_roles


class UserModel(UserCreate, UserMixin, table=True):
    __tablename__ = "user_data"  # type: ignore

    id_: str = Field(
        default_factory=generate_hex_uuid4,
        primary_key=True,
    )

    created_time: int = Field(default_factory=current_posix_time)

    user_role_obj: Optional["UserRoleModel"] = Relationship(
        back_populates="user_obj",
    )

    def get_id(self) -> str:
        """
        This is the method which will run by the flask-login
        it will get the unique identificaiton per user thats why i make this
        as the docs say this here-
        https://flask-login.readthedocs.io/en/latest/#your-user-class
        """
        return self.id_


class UserRoleModel(SQLModel, table=True):
    __tablename__ = "user_role_data"  # type: ignore

    id_: str = Field(
        default_factory=generate_hex_uuid4,
        primary_key=True,
    )

    user_id: str = Field(
        default=None,
        foreign_key="user_data.id_",
        unique=True,
        index=True,
    )

    role: str = Field(
        default=user_roles.CUSTOMER,
    )

    description: str = Field(
        max_length=5000,
        description="Some information about the role why for this user has this role",
    )
    # the description is not any idea for now later i will add this

    user_obj: UserModel = Relationship(
        back_populates="user_role_obj",
    )
