"""
blueprints/auth/routes.py
Here i will write authentication related thigns
like login out register and so on like this
"""

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    url_for,
)


from .forms import LoginForm, RegisterForm

from services.database.controllers import add_new_user_row
from services.database.models import UserModel

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


@auth_bp.route(
    rule="/register",
    methods=["GET", "POST"],
)
def register_page():
    """
    This is not complete yet this is in demo stat
    here i will add the hash password and then
    otp send to use this two logic i will apply here
    """
    form = RegisterForm()
    if form.validate_on_submit():  # type: ignore
        first_name = form.first_name.data
        middle_name = form.middle_name.data
        last_name = form.last_name.data
        phone_no = form.phone_no.data
        email_id = form.email_id.data
        username = form.username.data
        password = form.password.data

        # i will add hash and salt to the password here
        # by calling another fun in reality
        hashed_password = f"{password}"

        user_add = add_new_user_row(
            user_obj=UserModel(
                first_name=first_name or "",
                middle_name=middle_name,
                last_name=last_name,
                phone_no=phone_no,
                email_id=email_id,
                username=username,
                password_hashed=hashed_password,
            )
        )
        if not user_add:
            flash(
                message="Somethings went wrong pls try again",
                category="error",
            )
        else:
            # actually i will use flask login for session and cookie
            flash(
                message="🎉 Account Register Successful 🎉",
                category="success",
            )
            return redirect(
                location=url_for("general_bp.index"),
            )

    else:
        # here the field is the name in the form's class i made so i use _
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{field.upper()} : {error}", "danger")

    return render_template(
        template_name_or_list="auth/register.html",
        form=form,
    )
