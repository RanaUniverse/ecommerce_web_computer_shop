"""
app/features/catalog/service/category.py

here i will write category related informations of business logic
"""

from sqlmodel import Session


from .. import exceptions as exc
from ..models.category import CategoryModel

from ..operations import category as category_ops

from ....shared.database import engine
from ..schema.category import (
    CategoryOutAdmin,
    CategoryCreateRequest,
    CategoryOutMinimal,
)


def list_of_category_names() -> list[str]:
    """
    This fun is called like to get all category name from my db
    i will want to shows the names to user

    # TODO

    Later i thinks to make this in cache so that the computation will not need
    to do each time it will shows list of all category
    """
    with Session(engine) as session:

        results = category_ops.get_all_category_names(
            session=session,
        )
        return results


def add_one_category(
    obj: CategoryCreateRequest,
    parent_category_name: str | None = None,
) -> CategoryOutAdmin:
    """
    Trying to add the category row there by taking input schema
    in this service fun it will return output schema

    This has Exception !!!
    """
    # model_obj = will i here do converion from schem to obj
    with Session(engine) as session:

        # first i will check the name of paretn category to think before insert
        if parent_category_name:
            cat_obj = category_ops.get_one_category_row_by_name(
                session=session,
                name=parent_category_name,
            )
            if not cat_obj:
                raise exc.ParentCategoryNotFoundError(
                    f"{parent_category_name} is not present as a category."
                )
            else:
                obj.parent_id = cat_obj.id_

        name = obj.name.strip() if obj.name else None
        if name:
            cat_obj = category_ops.get_one_category_row_by_name(
                session=session,
                name=name,
            )
            if cat_obj:
                raise exc.DuplicateCategoryNameError(
                    f"{name} is already a catagory present."
                )
        model_obj = CategoryModel.model_validate(
            obj=obj,
            from_attributes=True,
        )
        catgory_model = category_ops.add_one_category_row(
            session=session,
            category_obj=model_obj,
        )
        # again from the obj i need to make the categoryOUtAdmin here in this service layer
        if not catgory_model:
            raise exc.CategoryCreationFailError("Category insertion fails.")

        out_obj = CategoryOutAdmin.model_validate(
            obj=catgory_model,
            from_attributes=True,
        )
        return out_obj


def get_category_info_for_public(category_id: str) -> CategoryOutMinimal | None:
    """
    it will out schema of the category
    """

    with Session(engine) as session:
        model_obj = category_ops.get_one_category_row_by_id(
            session=session,
            category_id=category_id,
        )
        if not model_obj:
            return None

        out_obj = CategoryOutMinimal.model_validate(
            obj=model_obj,
            from_attributes=True,
        )
        return out_obj


def get_category_info_for_admin(category_id: str) -> CategoryOutAdmin | None:
    """
    it will out the schem for the amdin with many information
    """
    with Session(engine) as session:
        model_obj = category_ops.get_one_category_row_by_id(
            session=session,
            category_id=category_id,
        )
        if not model_obj:
            return None

        out_obj = CategoryOutAdmin.model_validate(
            obj=model_obj,
            from_attributes=True,
        )
        return out_obj


def all_category_minimal() -> list[CategoryOutMinimal]:
    """
    this will shows the all categoryOUtMInimal schemas for all the
    rows of the category
    """
    with Session(engine) as session:
        list_of_models = category_ops.get_all_categories(session=session)

        out_objs: list[CategoryOutMinimal] = []

        for x in list_of_models:
            schema_obj = CategoryOutMinimal.model_validate(
                obj=x,
                from_attributes=True,
            )

            out_objs.append(schema_obj)

        return out_objs
