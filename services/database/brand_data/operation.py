"""
services/database/brand_data/operation.py
Here I will write functions related to brand:
- add brand
- get brand by id
- get brand by name
- get all brands
- get all products of a brand
"""

from typing import Sequence


from sqlmodel import Session, select


from ..core import engine

from ..models import BrandModel, ProductModel


from utils.custom_logger import logger


def add_one_brand_row(brand_obj: BrandModel) -> BrandModel | None:
    """
    Insert a new brand row in the brand table
    """
    with Session(engine) as session:
        try:
            session.add(brand_obj)
            session.commit()
            session.refresh(brand_obj)
            return brand_obj
        except Exception as e:
            logger.error(f"Failed to create brand: {e}")
            return None


def get_one_brand_row_by_id(brand_id: str) -> BrandModel | None:
    with Session(engine) as session:
        return session.get(BrandModel, brand_id)


def get_one_brand_row_by_name(name: str | None) -> BrandModel | None:
    """
    Return brand object by name
    for now maybe this will not need if i pass id_
    """
    if not name:
        return None

    name = name.strip()

    with Session(engine) as session:
        statement = select(BrandModel).where(BrandModel.name == name)
        result = session.exec(statement)
        return result.first()


def get_all_brand_names(reverse: bool = False) -> list[str]:
    with Session(engine) as session:
        statement = select(BrandModel.name)
        result = session.exec(statement)
        names = result.all()
        arrange_name = sorted(
            names,
            key=str.casefold,
            reverse=reverse,
        )
        return arrange_name


def get_all_products_of_brand(brand_id: str) -> list[ProductModel]:
    """
    Return all products for a given brand id
    i will use the brand.product_obj this way
    """
    with Session(engine) as session:
        brand_obj = session.get(BrandModel, brand_id)
        if brand_obj:
            return brand_obj.product_obj
        return []


def get_all_brands_id_name() -> Sequence[tuple[str, str]]:
    with Session(engine) as session:
        statement = select(BrandModel.id_, BrandModel.name).order_by(BrandModel.name)
        results = session.exec(statement).all()
        return results
