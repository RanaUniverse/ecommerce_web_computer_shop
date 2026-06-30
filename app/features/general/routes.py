"""
app/features/general/routes.py
Here i will keep the some general routes endpoints

I am using this blueprint for some app related config
"""

import secrets


from flask import (
    Blueprint,
    g,
    render_template,
    Response,
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


@general_bp.before_app_request
def generate_nonce():
    g.nonce = secrets.token_hex(
        nbytes=20,
    )


@general_bp.after_app_request
def modify_headers(response: Response):
    """
    I am using nonce to allow internal css and js
    though i should to use external css and js
    """
    response.headers["Content-Security-Policy"] = (
        f"default-src 'self'; "
        f"script-src 'self' 'nonce-{g.nonce}';"
        f"style-src 'self' 'nonce-{g.nonce}';"
    )

    # This below is for loading correct type of document
    response.headers["X-Content-Type-Options"] = "nosniff"

    response.headers["X-Frame-Options"] = "SAMEORIGIN"

    return response


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
