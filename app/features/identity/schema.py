"""
app/features/identity/schema.py
Here i will write the schema so that i will sure what
what data to expose to whom and not to whom
"""

from sqlmodel import (
    Field,
    SQLModel,
)


class UserBase(SQLModel):

    first_name: str


class UserCreate(UserBase):

    middle_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    phone_no: str | None = Field(default=None, unique=True)
    email_id: str | None = Field(default=None, unique=True)
    username: str | None = Field(default=None, unique=True)
    password_hashed: str = Field(
        description="At time of saving this i will encrypt this so that at the "
        "moment it enter in my backend it become encrypted."
    )


class UserUpdate(SQLModel):
    first_name: str | None = None
    middle_name: str | None = None
    last_name: str | None = None
    phone_no: str | None = None
    email_id: str | None = None
    username: str | None = None


class UserPasswordUpdate(SQLModel):
    """
    I keep this separate so that password change will
    be done in separated logic like validate latest login
    """

    password_hashed: str | None = Field(
        description="At time of saving this i will encrypt this so that at the "
        "moment it enter in my backend it become encrypted."
    )


class UserOutPublic(UserBase):
    """
    this is showing normally to other user for comment
    review and so on for show user profile
    """

    id_: str


class UserOutSelf(UserOutPublic):
    """
    This is for showing detailed information to himself
    """

    middle_name: str | None = None
    last_name: str | None = None
    email_id: str | None = None
    phone_no: str | None = None
    username: str | None = None
    created_time: int


class UserOutAdmin(UserOutSelf):
    pass
