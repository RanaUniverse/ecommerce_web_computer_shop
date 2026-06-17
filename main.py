"""
main.py
Here this file will my entrypoint
i will try to run this and it will run a basic app for checking
"""

# This upper two line help to stop making the .pyc file to looks clean the repo
import sys

sys.dont_write_bytecode = True

# Now from below i will write my main logic of code


from flask import Flask


from app.shared.config import (
    config_settings,
)

from app.shared.extensions import (
    login_manager,
    bcrypt,
)


from app.features.catalog.routes.brand import brand_bp
from app.features.catalog.routes.category import category_bp
from app.features.catalog.routes.product import product_bp
from app.features.errors.routes import error_bp
from app.features.general.routes import general_bp
from app.features.identity.routes import auth_bp, user_bp
from app.features.ordering.routes import order_bp


def create_app():
    """
    This is for the app instance to return
    this is factory way to do this
    """
    app = Flask(
        __name__,
    )

    app.config["SECRET_KEY"] = config_settings.app_secret_key
    from app.shared.utils.general_utils import posix_to_readable_time

    app.add_template_filter(
        f=posix_to_readable_time,
        name="read_posix_time_fun",
    )

    # if i want to attach same blueprint in differnet url prefix
    # i need to use the different name there
    app.register_blueprint(blueprint=auth_bp)
    app.register_blueprint(blueprint=error_bp)
    app.register_blueprint(blueprint=general_bp)
    app.register_blueprint(blueprint=user_bp)
    app.register_blueprint(blueprint=order_bp)
    app.register_blueprint(blueprint=brand_bp, url_prefix="/brand")
    app.register_blueprint(blueprint=category_bp, url_prefix="/category")
    app.register_blueprint(blueprint=product_bp, url_prefix="/product")

    bcrypt.init_app(  # type: ignore
        app=app,
    )
    login_manager.init_app(  # type: ignore
        app=app,
    )

    return app


def main():
    app = create_app()
    app.run(
        host=config_settings.app_host,
        port=config_settings.app_port,
        debug=config_settings.app_debug,
    )


if __name__ == "__main__":
    # Before run this make sure to run the 'alembic upgrade head'
    main()
