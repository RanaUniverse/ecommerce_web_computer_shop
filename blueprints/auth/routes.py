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

from flask_login import (  # type: ignore
    login_user,  # type: ignore
    logout_user,
    login_required,  # type: ignore
)

from .forms import LoginForm, RegisterForm

from services.database.operations import (
    add_new_user_row,
    get_user_row_by_phone_no,
)

from services.database.models import UserModel, UserRoleModel

from utils.config import MESSAGE_HELP_CENTER

from utils.constants_messages import AuthMessages, CommonMessages, BS5Alert


from utils.custom_logger import logger

from utils.security import (
    generate_password_hash,
    verify_hashed_password,
)

auth_bp = Blueprint(
    name="auth_bp",
    import_name=__name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/auth/static",
)


@auth_bp.route(
    rule="/login",
    methods=["GET", "POST"],
)
def login():
    form = LoginForm()

    if form.validate_on_submit():  # type: ignore
        phone_no = form.identifier.data or None
        password = form.password.data or None
        remember = form.remember.data
        print(phone_no)
        print(password)
        print(remember)

        if not phone_no or not password:
            # i wish this will not happens because flask-wtf already verify this
            logger.error(
                "on time of login phone or password need to come after validate"
            )
            flash(
                message=AuthMessages.CREADANTIAL_NEED,
                category=BS5Alert.WARNING,
            )
            return redirect(url_for("auth_bp.login"))

        user_obj = get_user_row_by_phone_no(phone_no=phone_no)
        if not user_obj:
            flash(
                message=AuthMessages.ACCOUNT_NOT_FOUND,
                category=BS5Alert.WARNING,
            )
            flash(
                message=CommonMessages.MESSAGE_HELP_CENTER,
                category=BS5Alert.PRIMARY,
            )
            return redirect(url_for("auth_bp.login"))

        # now i will check the password match or not then login
        is_password_correct = verify_hashed_password(
            hashed_password=user_obj.password_hashed,
            password=password,
        )
        if not is_password_correct:
            flash(
                message=AuthMessages.PASSWORD_MISMATCH,
                category=BS5Alert.DANGER,
            )
            return redirect(url_for("auth_bp.login"))

        # it measn password is correct
        # i need to impliment remember or not
        login_user(
            user=user_obj,
            remember=True,
        )
        flash(
            message=AuthMessages.LOGIN_SUCCESS,
            category=BS5Alert.INFO,
        )
        return redirect(url_for("general_bp.index"))

    # i will use flash with categry of bs coor to shows goodly design
    # it means get is come
    return render_template(
        template_name_or_list="auth/login.html",
        form=form,
    )


@auth_bp.route(
    rule="/register",
    methods=["GET", "POST"],
)
def register():
    """
    This is not complete yet this is in demo stat
    here i will add the hash password and then
    otp send to use this two logic i will apply here
    """
    form = RegisterForm()
    if form.validate_on_submit():  # type: ignore
        first_name = form.first_name.data or None
        middle_name = form.middle_name.data or None
        last_name = form.last_name.data or None
        phone_no = form.phone_no.data or None
        email_id = form.email_id.data or None
        password = form.password.data or None

        if not password:
            # i wished this will never run what i think
            logger.error("Something wrong in password become none in register")
            flash(
                message=AuthMessages.PASSWORD_NEED,
                category=BS5Alert.WARNING,
            )
            flash(
                message=MESSAGE_HELP_CENTER,
                category=BS5Alert.PRIMARY,
            )
            return redirect(url_for("auth_bp.register"))

        # from here the account creatin step will start actually
        # i will add otp verification step here in this place mabye
        hashed_password = generate_password_hash(
            password=password,
        )

        new_user_obj = add_new_user_row(
            user_obj=UserModel(
                first_name=first_name or "",
                middle_name=middle_name,
                last_name=last_name,
                phone_no=phone_no,
                email_id=email_id,
                password_hashed=hashed_password,
                user_role_obj=UserRoleModel(),
            )
        )
        # below i need to configure the way so that i can say what problem
        # has occurs like passowrd problem, or username or phone number or
        # email already exists liekt his problem
        if not new_user_obj:
            flash(
                message=CommonMessages.SOMETHING_WENT_WRONG,
                category=BS5Alert.WARNING,
            )
        else:
            # it means user data has been inserted in the table goodly
            login_user(
                new_user_obj,
                remember=True,
            )
            # maybe i will change this  True to condition from the user
            name = f"{new_user_obj.first_name or ''} {new_user_obj.last_name or ''}".strip()

            # actually i will use flask login for session and cookie
            flash(
                message=AuthMessages.REGISTER_SUCCESS,
                category=BS5Alert.INFO,
            )
            flash(
                message=f"{name}, {AuthMessages.LOGIN_SUCCESS}",
                category=BS5Alert.INFO,
            )
            return redirect(
                location=url_for("general_bp.index"),
            )

    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(
                    message=f"{field.upper()} : {error}",
                    category=BS5Alert.DANGER,
                )

    # this level code below will run on the get req
    return render_template(
        template_name_or_list="auth/register.html",
        form=form,
    )


@auth_bp.route(rule="/logout")
@login_required
def logout():
    logout_user()
    flash(
        message=AuthMessages.LOGOUT_SUCCESS,
        category=BS5Alert.SECONDARY,
    )

    return redirect(url_for("general_bp.index"))
