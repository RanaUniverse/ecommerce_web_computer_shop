"""
blueprints/auth/forms.py
Here i will make the forms related for login and register
so that i can use the csrf token validation and safe my user privacy
"""

from flask_wtf import FlaskForm  # type: ignore

from wtforms import (
    BooleanField,
    PasswordField,
    StringField,
    SubmitField,
)

from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Optional,
)

# i need to make sure this dict value not got change by external force
# i use this becuase bs5 need a placholder to shows goodly desing in bootstrap
DEFAULT_PLACEHOLDER: dict[str, str] = {
    "placeholder": " ",
}


class LoginForm(FlaskForm):
    """
    I make this class so that i will use this class for
    use in the login form making page it will also validate
    """

    # for now i have only phone no, but for now i am with only phone number
    identifier = StringField(
        label="Phone No",
        validators=[DataRequired(), Length(min=10, max=50)],
        render_kw=DEFAULT_PLACEHOLDER,
    )

    password = PasswordField(
        label="Enter Your Password",
        validators=[
            DataRequired(),
        ],
        render_kw=DEFAULT_PLACEHOLDER,
    )

    remember = BooleanField(label="Remember Me", default=True)

    submit = SubmitField(label="Login Now")


class RegisterForm(FlaskForm):
    """
    This is for allow to make new user account
    for bootstrap the placeholder need but it will not shows to user
    """

    # i need to make sure this dict value not got change by external force
    DEFAULT_PLACEHOLDER: dict[str, str] = {
        "placeholder": " ",
    }

    first_name = StringField(
        label="First Name",
        validators=[
            DataRequired(),
            Length(
                min=1,
                max=50,
            ),
        ],
        render_kw=DEFAULT_PLACEHOLDER,
    )

    middle_name = StringField(
        label="Middle Name",
        validators=[
            Optional(),
            Length(max=50),
        ],
        # below is the example if i will want to pass extra things
        render_kw={
            **DEFAULT_PLACEHOLDER,
        },
    )
    last_name = StringField(
        label="Last Name",
        validators=[
            Optional(),
            Length(max=50),
        ],
        render_kw=DEFAULT_PLACEHOLDER,
    )
    phone_no = StringField(
        label="Phone No",
        validators=[
            Optional(),
            Length(min=10, max=15),
        ],
        render_kw=DEFAULT_PLACEHOLDER,
    )
    email_id = StringField(
        label="Email Id",
        validators=[
            Optional(),
            Email(),
        ],
        render_kw=DEFAULT_PLACEHOLDER,
    )
    username = StringField(
        label="Username",
        validators=[
            Optional(),
            Length(max=50),
        ],
        render_kw=DEFAULT_PLACEHOLDER,
    )
    password = PasswordField(
        label="Password",
        validators=[DataRequired()],
        render_kw=DEFAULT_PLACEHOLDER,
    )
    confirm_password = PasswordField(
        label="Confirm Password",
        validators=[
            DataRequired(),
            EqualTo(
                fieldname="password",
                message="Please enter the same password",
            ),
        ],
        render_kw=DEFAULT_PLACEHOLDER,
    )
    # for now remember is no use i just keep
    remember = BooleanField(
        label="Remember Me",
        default=True,
    )

    submit = SubmitField(
        label="Create New Account",
    )
