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


from utils.config import HOST_ADDRESS, PORT_INT, DEBUG_BOOL
from blueprints import (
    auth_bp,
    error_bp,
    general_bp,
)

app = Flask(__name__)


app.register_blueprint(blueprint=auth_bp)
app.register_blueprint(blueprint=error_bp)
app.register_blueprint(blueprint=general_bp)


if __name__ == "__main__":
    print(app.url_map)
    app.run(
        host=HOST_ADDRESS,
        port=PORT_INT,
        debug=DEBUG_BOOL,
    )
