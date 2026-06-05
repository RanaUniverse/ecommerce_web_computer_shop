"""
app/features/general/routes.py
Here i will keep the some general routes endpoints
"""

from flask import (
    Blueprint,
    render_template,
)


from ...shared.config import config_shop_details

general_bp = Blueprint(
    name="general_bp",
    import_name=__name__,
    template_folder="templates",
)


@general_bp.app_context_processor
def inject_brand():
    return {
        "BRAND_NAME": config_shop_details.brand_name,
    }


@general_bp.route(rule="/")
def index():
    return render_template(
        template_name_or_list="general/index.html",
    )


@general_bp.route(rule="/settings")
def settings():
    return render_template(
        template_name_or_list="general/settings.html",
    )


@general_bp.route(rule="/about")
def about():
    return render_template(
        template_name_or_list="general/about_page.html",
    )


@general_bp.route(rule="/help")
def help_page():
    return render_template(
        template_name_or_list="general/help_page.html",
    )
