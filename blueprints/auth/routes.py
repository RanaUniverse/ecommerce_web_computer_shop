"""
blueprints/auth/routes.py
Here i will write authentication related thigns
like login out register and so on like this
"""

from flask import (
    Blueprint,
    flash,
    render_template,
)


from .forms import LoginForm

auth_bp = Blueprint(
    name="auth_bp",
    import_name=__name__,
    template_folder="templates",
)


@auth_bp.route(
    rule="/login",
    methods=["GET", "POST"],
)
def login():
    form = LoginForm()
    # i will use flash with categry of bs coor to shows goodly design
    flash(
        message="Kindly enter your ID and password to proceed.",
        category="primary",
    )
    return render_template(
        template_name_or_list="auth/login.html",
        form=form,
    )


@auth_bp.route("/register")
def register_page():
    return render_template(
        template_name_or_list="auth/register.html",
    )
