"""
blueprints/__init__.py
Here i will make this as a packages to make some blueprints
This will be good to make many blueprint to module my app
"""

from .auth.routes import auth_bp
from .brand.routes import brand_bp
from .category.routes import category_bp
from .errors.routes import error_bp
from .general.routes import general_bp
from .order.routes import order_bp
from .user.routes import user_bp
from .product.routes import product_bp
from .testing.routes import testing_bp

__all__ = [
    "auth_bp",
    "brand_bp",
    "error_bp",
    "general_bp",
    "user_bp",
    "order_bp",
    "product_bp",
    "category_bp",
    "testing_bp",
]
