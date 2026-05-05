"""
services/database/controllers/category.py
Here i will keep the functions related to
category tables like CRUD here
"""

from sqlmodel import Session

from ..core import engine

from ..models.category import CategoryModel

from utils.custom_logger import logger


def add_one_category_row(category_obj: CategoryModel) -> CategoryModel | None:
    """
    This fun will try to insert new category row in the category table
    """
    with Session(engine) as session:
        try:
            session.add(category_obj)
            session.commit()
            session.refresh(category_obj)
            return category_obj
        except Exception as e:
            logger.error(f"Faild to new category, {e}")
            return None


def get_one_category_row_by_id(category_id: int):
    with Session(engine) as session:
        category_obj = session.get(CategoryModel, category_id)
        return category_obj


def delete_one_category_row_by_id(category_id: int):
    """
    In development
    This need to make for two thigns,
    Will the products will delete or not
    """
    pass
