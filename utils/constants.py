"""
utils/constants.py

This file contains reusable constant values used throughout the project.

Keeping constants in one place helps:
- avoid typing mistakes
- improve code readability
- make updates easier later

The constants are organized into classes so they can be accessed
cleanly from other parts of the application.
"""


class AuthMessages:
    LOGIN_SUCCESS = "Login successful"
    LOGIN_FAILED = "Invalid email or password"
    LOGOUT_SUCCESS = "Logged out successfully"
    ACCOUNT_CREATED = "Account created successfully"
    ACCOUNT_EXISTS = "Account already exists"
    PASSWORD_RESET_SENT = "Password reset link sent to your email"
    PASSWORD_RESET_SUCCESS = "Password reset successful"


class CommonMessages:
    TRY_AGAIN = "Please try again"
    SOMETHING_WENT_WRONG = "Something went wrong"
    CONTACT_ADMIN = "Please contact admin"
    OPERATION_SUCCESS = "Operation completed successfully"
    INVALID_REQUEST = "Invalid request"
    UNAUTHORIZED_ACCESS = "Unauthorized access"


class PermissionMessages:
    ACCESS_DENIED = "You do not have permission to access this resource"
    LOGIN_REQUIRED = "Please login first"
    ADMIN_ONLY = "This action is allowed for admin only"
    FORBIDDEN = "You are not allowed to perform this action"


class ProductMessages:
    PRODUCT_NOT_FOUND = "Product not found"
    PRODUCT_ADDED = "Product added successfully"
    PRODUCT_UPDATED = "Product updated successfully"
    PRODUCT_DELETED = "Product deleted successfully"
    INVALID_PRODUCT = "Invalid product details"
    OUT_OF_STOCK = "This product is out of stock"


class CartMessages:
    ADDED_TO_CART = "Product added to cart"
    REMOVED_FROM_CART = "Product removed from cart"
    CART_EMPTY = "Your cart is empty"
    CART_UPDATED = "Cart updated successfully"
    ITEM_NOT_IN_CART = "Item not found in cart"


class OrderMessages:
    ORDER_SUCCESS = "Order placed successfully"
    ORDER_FAILED = "Failed to place order"
    PAYMENT_FAILED = "Payment failed"
    PAYMENT_SUCCESS = "Payment successful"
    ORDER_CANCELLED = "Order cancelled successfully"
    ORDER_NOT_FOUND = "Order not found"
    ORDER_ALREADY_PROCESSED = "Order already processed"


class BS5Alert:
    """
    This will contains the key value so that i will use this
    https://getbootstrap.com/docs/5.3/components/alerts/
    """

    PRIMARY = "primary"
    SECONDARY = "secondary"
    SUCCESS = "success"
    DANGER = "danger"
    WARNING = "warning"
    INFO = "info"
    LIGHT = "light"
    DARK = "dark"
