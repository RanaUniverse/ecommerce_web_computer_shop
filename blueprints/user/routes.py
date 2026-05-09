"""
blueprints/user/routes.py
Here i will make the routes related to the
maybe user profile  images and so on
user settings like this
"""

from flask import Blueprint, render_template

user_bp = Blueprint(
    name="user_bp",
    import_name=__name__,
    template_folder="templates",
)


@user_bp.route(rule="/profile")
def profile():
    """
    When user will want to see his profile things this
    will run it will allow user to chang edit his thigns
    """
    return render_template(
        template_name_or_list="user/profile.html",
    )
