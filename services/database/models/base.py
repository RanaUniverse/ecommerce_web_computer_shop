"""
services/database/models/base.py
Here i will defines the base class for some tables so that it will easy
"""

from sqlmodel import (
    SQLModel,
    Field,
)

from utils.general_utils import (
    current_posix_time,
    generate_hex_uuid4,
)


class ImageBase(SQLModel):
    """
    This is generic class there
    """

    id_: str = Field(
        default_factory=generate_hex_uuid4,
        primary_key=True,
    )

    filepath: str | None = Field(default=None)
    alt_text: str | None = Field(default=None)

    external_url: str | None = Field(default=None)

    is_primary: bool = Field(default=False)

    display_order: int | None = Field(default=0)

    creator_id: str | None = Field(
        default=None,
        foreign_key="user_data.id_",
    )

    created_time: int = Field(default_factory=current_posix_time)
