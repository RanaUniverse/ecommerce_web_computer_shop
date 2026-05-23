"""
blueprints/brand/routes.py
"""

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    url_for,
)

from .forms import BrandAddForm

from services.database.models import BrandModel
from services.database.operations import add_one_brand_row

brand_bp = Blueprint(
    name="brand_bp",
    import_name=__name__,
    template_folder="templates",
)


@brand_bp.route("/add", methods=["GET", "POST"])
def add():

    form = BrandAddForm()
    print(form.errors)
    if form.validate_on_submit():  # type: ignore
        name = form.name.data
        description = form.description.data
        url = form.website_url.data
        logo_filename = form.logo_filename.data

        new_brand_obj = add_one_brand_row(
            brand_obj=BrandModel(
                name=name or "",
                description=description,
                website_url=url,
                logo_filename=logo_filename,
            )
        )
        if not new_brand_obj:
            flash(
                message="Somethign Went wrong, contact admin",
                category="warning",
            )
        else:

            flash(
                message="Brand Created Successfully",
                category="primary",
            )

            return redirect(url_for("general_bp.index"))

    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{field.upper()}: {error}", "danger")

    return render_template(
        "brand/add.html",
        form=form,
    )
