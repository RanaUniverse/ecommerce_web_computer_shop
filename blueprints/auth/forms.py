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
    Length,
)


class LoginForm(FlaskForm):
    """
    I make this class so that i will use this class for
    use in the login form making page it will also validate
    """

    identifier = StringField(
        label="Email Id or Phone No",
        validators=[DataRequired(), Length(min=10, max=50)],
        render_kw={
            "placeholder": "Email or Phone Number",
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
