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


class LoginForm(FlaskForm):
    """
    I make this class so that i will use this class for
    use in the login form making page it will also validate
    """

    # for now i have only phone no, but for now i am with only phone number
    identifier = StringField(
        label="Phone No",
        validators=[DataRequired(), Length(min=10, max=50)],
        render_kw={
            "placeholder": "Phone Number",
        },
    )

    password = PasswordField(
        label="Enter Your Password",
        validators=[
            DataRequired(),
        ],
        render_kw={
            "placeholder": "Your Password",
        },
    )

    remember = BooleanField(label="Remember Me", default=True)

    submit = SubmitField(label="Login Now")


class RegisterForm(FlaskForm):
    """
    This is for allow to make new user account
    """

    first_name = StringField(
        label="First Name",
        validators=[
            DataRequired(),
            Length(
                min=1,
                max=50,
            ),
        ],
        render_kw={
            "placeholder": "First Name?",
        },
    )

    middle_name = StringField(
        label="Middle Name",
        validators=[
            Optional(),
            Length(max=50),
        ],
        render_kw={
            "placeholder": "Middle Name (Optional)",
        },
    )
    last_name = StringField(
        label="Last Name",
        validators=[
            Optional(),
            Length(max=50),
        ],
        render_kw={
            "placeholder": "Last Name (Optional)",
        },
    )
    phone_no = StringField(
        label="Phone No",
        validators=[
            Optional(),
            Length(min=10, max=15),
        ],
        render_kw={
            "placeholder": "Phone / Telephone No",
        },
    )
    email_id = StringField(
        label="Email Id",
        validators=[
            Optional(),
            Email(),
        ],
        render_kw={"placeholder": "Email Address?"},
    )
    username = StringField(
        label="Username",
        validators=[
            Optional(),
            Length(max=50),
        ],
        render_kw={"placeholder": "Choose a Unique Username"},
    )
    password = PasswordField(
        label="Password",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Your Password"},
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
        render_kw={
            "placeholder": "Enter Password Again",
        },
    )
    # for now remember is no use i just keep
    remember = BooleanField(label="Remember Me", default=True)

    submit = SubmitField(label="Create New Account")
