"""
app/features/catalog/operations/category.py
"""

"""
services/database/category_data/operation.py
Here i will keep the functions related to
category tables like CRUD here
"""


from sqlmodel import Session, select


from ..models.category import CategoryModel

from ....shared.utils.custom_logger import logger


def add_one_category_row(
    session: Session,
    category_obj: CategoryModel,
) -> CategoryModel | None:
    """
    This fun will try to insert new category row in the category table
    """
    try:
        session.add(category_obj)
        session.commit()
        session.refresh(category_obj)
        return category_obj
    except Exception as e:
        logger.error(f"Failed to add new Category, {e}")
        return None


def get_one_category_row_by_id(
    session: Session,
    category_id: str,
):
    category_obj = session.get(CategoryModel, category_id)
    return category_obj


def delete_one_category_row_by_id(
    session: Session,
    category_id: int,
):
    """
    In development
    This need to make for two thigns,
    Will the products will delete or not
    """
    pass


def get_one_category_row_by_name(
    session: Session,
    name: str | None,
) -> CategoryModel | None:
    """
    i will pass the naem of the category if if not present it will send none
    i shoudl not pass empty string here
    as i sure name is unique so i will use first()
    """
    if not name:
        return None

    name = name.strip()

    statement = select(
        CategoryModel,
    ).where(
        CategoryModel.name == name,
    )
    results = session.exec(statement)
    obj = results.first()

    return obj


# TODO I need to work on this below fun carefully
def get_all_category_names(
    session: Session,
    reverse: bool = False,
) -> list[str]:

    statement = select(
        CategoryModel.name,
    ).where(
        CategoryModel.name is not None,
    )
    results = session.exec(statement)

    names = results.all()
    arrange_name = sorted(  # type: ignore
        names,  # type: ignore i was sure by upper logic that None will not come
        key=str.casefold,  # type: ignore
        reverse=reverse,
    )
    return arrange_name  # type: ignore


def get_all_categories(
    session: Session,
) -> list[CategoryModel]:

    statement = select(CategoryModel).order_by(CategoryModel.name)
    objs = list(session.exec(statement=statement))

    return objs
