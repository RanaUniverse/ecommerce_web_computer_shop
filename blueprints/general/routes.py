"""
blueprints/general/routes.py
Here i will make the code for handle general
things of the endpoints
"""

from flask import (
    Blueprint,
    render_template,
)

general_bp = Blueprint(
    name="general_bp",
    import_name=__name__,
    template_folder="templates",
)


@general_bp.route(rule="/")
def index():
    return render_template(
        template_name_or_list="general/index.html",
    )
