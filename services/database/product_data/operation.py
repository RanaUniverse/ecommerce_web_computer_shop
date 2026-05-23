"""
services/database/product_data/operation.py
Here i will keep the functions related to the
Product table's CRUD
"""

from typing import Any


from sqlmodel import Session


from ..core import engine

from ..models import ProductModel

from ..schemas import ProductOutPublic


from utils.custom_logger import logger


def add_one_product_row(product_obj: ProductModel) -> ProductModel | None:
    """
    This will add one product in the product table
    and upon success it will return this obj else none
    """
    with Session(engine) as session:
        try:
            session.add(product_obj)
            session.commit()
            session.refresh(product_obj)
            return product_obj

        except Exception as e:
            logger.error(f"Failed to create product: {e}")
            return None


def get_one_product_row_by_id(product_id: str) -> ProductModel | None:
    """
    Search By the Primary Key of the Product Table
    I will try to serach the product obj by the primary key.
    As i will search by primary key i will use .get() easily
    """
    with Session(engine) as session:
        product_obj = session.get(ProductModel, product_id)
        return product_obj


def delete_one_product_row_by_id(product_id: str) -> bool:
    """
    I will use this function when i will want to delete the product row
    it will try to delete if delete success say true else false
    """
    with Session(engine) as session:
        product_obj = session.get(ProductModel, product_id)
        if not product_obj:
            return False
        try:
            session.delete(product_obj)
            session.commit()
            return True
        except Exception as e:
            logger.warning(f"Delete product row fails, {e}")
            return False


def update_product_name(product_id: str, new_name: str):
    pass


def update_product_description(product_id: str, new_description: str | None):
    pass


def update_product_quantity(product_id: str, new_quantity: int):
    pass


def update_product_mrp_price(product_id: str, new_mrp_price: float | None):
    pass


def update_product_purchase_price(product_id: str, new_purchase_price: float | None):
    pass


def update_product_sell_price(product_id: str, new_sell_price: float | None):
    pass


def update_product_category(product_id: str, new_category_id: int | None):
    pass


def update_product_row(
    product_id: str, **kwargs: dict[str, Any]
) -> ProductModel | None:
    """
    This is a generic update on the productmodel table
    i need to check this how this function will work
    """
    with Session(engine) as session:
        product = session.get(ProductModel, product_id)

        if not product:
            return None

        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)

        session.add(product)
        session.commit()
        session.refresh(product)

        return product


def get_product_out_public_schema_row(product_id: str) -> ProductOutPublic | None:
    with Session(engine) as session:
        print("#####")
        print("Calling in the schema function there")
        product_obj = session.get(ProductModel, product_id)

        if not product_obj:
            print("in here product_obj not get so productoutpublc will also none")
            return None

        # This upper give product_obj now i need to conver ti to productOutPublic model
        product_out_public_obj = ProductOutPublic.model_validate(
            obj=product_obj,
        )

        print(product_out_public_obj)
        return product_out_public_obj
