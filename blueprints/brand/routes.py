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

from utils.constants_messages import CommonMessages, BS5Alert, ProductMessages

brand_bp = Blueprint(
    name="brand_bp",
    import_name=__name__,
    template_folder="templates",
)


@brand_bp.route("/add", methods=["GET", "POST"])
def add():

    form = BrandAddForm()
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
                message=CommonMessages.MESSAGE_HELP_CENTER,
                category=BS5Alert.WARNING,
            )
        else:

            flash(
                message=ProductMessages.PRODUCT_CREATED,
                category=BS5Alert.INFO,
            )

            return redirect(url_for("general_bp.index"))

    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(
                    message=f"{field.upper()}: {error}",
                    category=BS5Alert.DANGER,
                )

    return render_template(
        "brand/add.html",
        form=form,
    )
