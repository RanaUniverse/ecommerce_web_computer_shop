"""
blueprints/testing/routes.py
i will write some testing things
"""

from flask import (
    render_template,
    flash,
    Blueprint,
)

from utils.constants_messages import BS5Alert

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

    flash(
        message="Primary: Welcome to Rana Store 👋",
        category=BS5Alert.PRIMARY,
    )

    flash(
        message="Secondary: Browse our latest deals and offers 🛍️",
        category=BS5Alert.SECONDARY,
    )

    flash(
        message="Success: Item added to cart successfully 🛒",
        category=BS5Alert.SUCCESS,
    )

    flash(
        message="Danger: Payment failed. Please try again ❌",
        category=BS5Alert.DANGER,
    )

    flash(
        message="Warning: Limited stock available for some items ⚠️",
        category=BS5Alert.WARNING,
    )

    flash(
        message="Info: New arrivals are now live 🔥",
        category=BS5Alert.INFO,
    )

    flash(
        message="Light: Free shipping on orders above $50 🚚",
        category=BS5Alert.LIGHT,
    )

    flash(
        message="Dark: Dark mode enabled 🌙",
        category=BS5Alert.DARK,
    )

    return render_template(
        template_name_or_list="testing/index.html",
    )


@testing_bp.route(rule="/bs_toast")
def checking_features():
    return render_template(
        template_name_or_list="testing/bs_toast.html",
    )
