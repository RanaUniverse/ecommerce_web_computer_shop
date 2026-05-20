"""
blueprints/testing/routes.py
i will write some testing things
"""

from flask import (
    render_template,
    flash,
    Blueprint,
)

testing_bp = Blueprint(
    name="testing_bp",
    import_name=__name__,
    template_folder="templates",
)


@testing_bp.route("/")
def index():
    """
    Just for information
    """
    return "This is Testing Page"


@testing_bp.route("/bs_alert")
def bs_alert():
    """
    Here i will check the bs alert from the flash()
    """

    flash("Primary: Welcome to Rana Store 👋", "primary")

    flash("Secondary: Browse our latest deals and offers 🛍️", "secondary")

    flash("Success: Item added to cart successfully 🛒", "success")

    flash("Danger: Payment failed. Please try again ❌", "danger")

    flash("Warning: Limited stock available for some items ⚠️", "warning")

    flash("Info: New arrivals are now live 🔥", "info")

    flash("Light: Free shipping on orders above $50 🚚", "light")

    flash("Dark: Dark mode enabled 🌙", "dark")

    return render_template(
        template_name_or_list="testing/index.html",
    )
