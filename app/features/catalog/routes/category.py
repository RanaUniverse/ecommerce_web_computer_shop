"""
app/features/catalog/routes/category.py

Product Category will be written here

I will write all the endpoints of the category realted
like category making, editing and so on
"""

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    url_for,
)


from .. import exceptions as exc

from ..forms.category import CategoryAddForm

from ..schema.category import CategoryCreateRequest

from ..service import category as category_ser

from ....shared.utils.constants_messages import (
    BS5Alert,
    ProductCategoryMessages,
)

category_bp = Blueprint(
    name="category_bp",
    import_name=__name__,
    template_folder="templates",
)


@category_bp.route(rule="/add", methods=["GET", "POST"])
def add():
    """
    This is when admin will want to create new category
    """

    form = CategoryAddForm()
    list_of_category = category_ser.list_of_category_names()

    if form.validate_on_submit():  # type: ignore
        name = form.name.data
        description = form.description.data
        icon_name = form.icon_name.data
        private_note = form.private_note.data
        # parent_id = form.parent_id.data or None
        parent_category = form.parent_category_name.data or None
        # because i want to insert as None when parent id not passed

        category_create_obj = CategoryCreateRequest(
            name=name,
            description=description,
            icon_name=icon_name,
            private_note=private_note,
        )

        try:
            # here i will actually return a page which will shows the category info
            # TODO
            # i will use this below and it will stop wrning
            new_category_obj = category_ser.add_one_category(  # type: ignore
                obj=category_create_obj,
                parent_category_name=parent_category,
            )
            flash(
                message=ProductCategoryMessages.CATEGORY_CREATED,
                category=BS5Alert.SUCCESS,
            )
            return redirect(url_for("category_bp.add"))

        except (
            exc.ParentCategoryNotFoundError,
            exc.DuplicateCategoryNameError,
            exc.CategoryCreationFailError,
        ) as e:
            flash(
                message=e.frontend_error_msg,
                category=BS5Alert.WARNING,
            )
            status_code = e.frontend_status_code

        except Exception:
            flash(
                message="An unexpected error occurred. Please try again later.",
                category=BS5Alert.DANGER,
            )
            status_code = 500

        return (
            render_template(
                "category/add.html",
                form=form,
                items=list_of_category,
            ),
            status_code,
        )

    return render_template(
        "category/add.html",
        form=form,
        items=list_of_category,
    )
