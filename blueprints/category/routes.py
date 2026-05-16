"""
blueprints/category/routes.py
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

from .forms import CategoryAddForm

from services.database.models import CategoryModel
from services.database.controllers import add_one_category_row

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
    if form.validate_on_submit():  # type: ignore
        name = form.name.data
        description = form.description.data
        icon_name = form.icon_name.data
        private_note = form.private_note.data
        parent_id = form.parent_id.data or None
        # because i want to insert as None when parent id not abialbale

        print(parent_id, type(parent_id))

        new_category_obj = add_one_category_row(
            category_obj=CategoryModel(
                name=name or "",
                description=description,
                icon_name=icon_name,
                private_note=private_note,
                parent_id=parent_id,
            )
        )

        if not new_category_obj:
            flash(
                message="Something went wrong",
                category="error",
            )
            return redirect(url_for("category_bp.add"))
        else:
            flash(
                message="Category Creation Successful",
                category="primary",
            )
            flash(
                message="You Can Add Another Category Here",
                category="primary",
            )
            return redirect(url_for("category_bp.add"))

    return render_template(
        "category/add.html",
        form=form,
    )
