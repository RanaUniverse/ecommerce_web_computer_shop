"""
app/shared/extensions.py
Here i will make flask-extension related things in this place

Warning
Warning
Warning
Warning
Warning
Warning
Warning
I need to solve this by import the fun which will send user_id
"""

from flask_bcrypt import Bcrypt  # type: ignore

from flask_login import LoginManager  # type: ignore

from .database.operations import get_user_row_by_user_id

bcrypt = Bcrypt()


login_manager = LoginManager()


@login_manager.user_loader  # type: ignore
def load_user_from_session(user_id: str):
    """
    I will pass the user_id as string value and this will
    return the user_obj or none
    """
    return get_user_row_by_user_id(
        user_id=user_id,
    )
