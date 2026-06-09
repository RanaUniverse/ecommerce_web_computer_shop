"""
app/features/catalog/service/category.py

here i will write category related informations of business logic
"""

from sqlmodel import Session


from ..operations import category as category_ops

from ....shared.database import engine


def get_list_of_all_category_name() -> list[str]:
    with Session(engine) as session:

        results = category_ops.get_all_category_names(
            session=session,
        )
        return results
