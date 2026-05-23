"""
services/database/user_role_data/model.py
Here i will make a new table which will detarmines to keep the user's table's
data's role as string value i will use some values

customer -> it will by default value
businesses -> for shows low prices than others customer
staff -> access to see who has give orders and what thigns
manager -> allow to change product price, add product and details
owner -> shows statistics and data
developer -> its for me actually to get some inner things
"""

from typing import TYPE_CHECKING


from sqlmodel import (
    SQLModel,
    Field,
    Relationship,
)

if TYPE_CHECKING:
    from ..user_data.model import UserModel


class UserRoleModel(SQLModel, table=True):
    __tablename__ = "user_role_data"  # type: ignore

    id_: int = Field(default=None, primary_key=True)

    user_id: str = Field(
        default=None,
        foreign_key="user_data.id_",
        unique=True,
        index=True,
    )

    role: str = Field(default="customer")

    user_obj: UserModel = Relationship(
        back_populates="user_role_obj",
    )
