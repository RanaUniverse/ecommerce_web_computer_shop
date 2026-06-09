"""
app/features/catalog/service/brand.py

Here i will write brand realted services
"""

from typing import Sequence


from sqlmodel import Session


from ..operations import brand as brand_ops
from ....shared.database import engine


def get_all_brands_id_name_pair() -> Sequence[tuple[str, str]]:
    with Session(engine) as session:
        info = brand_ops.get_all_brands_id_name(
            session=session,
        )
        return info
