"""
app/features/general/routes.py
Here i will keep the some general routes endpoints
"""

from flask import (
    Blueprint,
    render_template,
    request,
    make_response,
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


# from flask.wrappers import Response
from flask import Response

# upper both is refereing to same thigns same class


@general_bp.after_app_request
def add_security_headers(response: Response):
    response.headers["X-Test"] = "Rana Universe"
    response.headers["X-url"] = "https://Rana.Rana49.online"
    response.headers["Content-Security-Policy"] = (
        "script-src 'self' 'nonce-abc';"
        "style-src 'self';"
        "img-src 'self' "
        "https://avatars.githubusercontent.com;"
    )

    print("code:", response.status_code)
    print(response)
    for key, value in response.headers.items():
        print(f"{key}: {value}")
    return response


@general_bp.route(rule="/")
def index():
    print("HEADERS WILL PRINT")
    print(request.headers)
    print("HEADERS HAS BEEN PRINTED")

    return render_template(
        template_name_or_list="general/index.html",
    )
    # response = make_response(
    #     render_template(
    #         template_name_or_list="general/index.html",
    #     )
    # )
    # response.headers["X-Test"] = "Rana Universe"
    # response.headers["Content-Security-Policy"] = "default-src 'self'"
    # print(type(response))
    # return response


@general_bp.route(rule="/settings")
def settings():
    return render_template(
        template_name_or_list="general/settings.html",
    )


@general_bp.route(rule="/about")
def about():
    print(request.headers)

    return render_template(
        template_name_or_list="general/about_page.html",
    )


@general_bp.route(rule="/help")
def help_page():
    return render_template(
        template_name_or_list="general/help_page.html",
    )
