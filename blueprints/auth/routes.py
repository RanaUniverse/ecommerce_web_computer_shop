"""
blueprints/auth/routes.py
Here i will write authentication related thigns
like login out register and so on like this
"""

from flask import (
    Blueprint,
    render_template,
)

auth_bp = Blueprint(
    name="auth_bp",
    import_name=__name__,
    template_folder="templates",
)


@auth_bp.route("/login")
def login_page():
    return render_template(
        template_name_or_list="auth/login.html",
    )


@auth_bp.route("/register")
def register_page():
    return render_template(
        template_name_or_list="auth/register.html",
    )
