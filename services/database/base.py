"""
services/database/base.py
Here i will keep the base class which will need by different tables there
Example imageBase is need for both product's image and category's image
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

    creator_id: str | None = Field(
        default=None,
        foreign_key="user_data.id_",
    )

    created_time: int = Field(default_factory=current_posix_time)
