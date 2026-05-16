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


from utils.config import (
    HOST_ADDRESS,
    PORT_INT,
    DEBUG_BOOL,
    SECRET_KEY,
)
from blueprints import (
    auth_bp,
    category_bp,
    error_bp,
    general_bp,
    order_bp,
    user_bp,
    product_bp,
)
from services.extensions import (
    bcrypt,
    login_manager,
)


def create_app():
    """
    This is for the app instance to return
    this is factory way to do this
    """
    app = Flask(
        __name__,
    )

    app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(blueprint=auth_bp)
    app.register_blueprint(blueprint=error_bp)
    app.register_blueprint(blueprint=general_bp)
    app.register_blueprint(blueprint=user_bp)
    app.register_blueprint(blueprint=order_bp)
    app.register_blueprint(blueprint=product_bp)
    # if i want to attach same blueprint in differnet url prefix
    # i need to use the different name there
    app.register_blueprint(
        blueprint=category_bp,
        url_prefix="/category",
    )

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
        host=HOST_ADDRESS,
        port=PORT_INT,
        debug=DEBUG_BOOL,
    )


if __name__ == "__main__":
    # Before run this make sure to run the 'alembic upgrade head'
    main()
