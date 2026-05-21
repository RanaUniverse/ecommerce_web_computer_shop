"""
blueprints/testing/routes.py
i will write some testing things
"""

from flask import (
    render_template,
    flash,
    Blueprint,
)

from utils.constants import BS5Alert

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

    flash("Primary: Welcome to Rana Store 👋", BS5Alert.PRIMARY)

    flash("Secondary: Browse our latest deals and offers 🛍️", BS5Alert.SECONDARY)

    flash("Success: Item added to cart successfully 🛒", BS5Alert.SUCCESS)

    flash("Danger: Payment failed. Please try again ❌", BS5Alert.DANGER)

    flash("Warning: Limited stock available for some items ⚠️", BS5Alert.WARNING)

    flash("Info: New arrivals are now live 🔥", BS5Alert.INFO)

    flash("Light: Free shipping on orders above $50 🚚", BS5Alert.LIGHT)

    flash("Dark: Dark mode enabled 🌙", BS5Alert.DARK)

    return render_template(
        template_name_or_list="testing/index.html",
    )


@testing_bp.route(rule="/bs_toast")
def checking_features():
    return render_template(
        template_name_or_list="testing/bs_toast.html",
    )
