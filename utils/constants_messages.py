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
    # Success messages
    LOGIN_SUCCESS = "Welcome back! You have logged in successfully."
    LOGOUT_SUCCESS = "You have been logged out successfully."
    REGISTER_SUCCESS = "Your account has been created successfully."
    PASSWORD_RESET_SUCCESS = "Your password has been reset successfully."

    # Error messages
    LOGIN_FAILED = "Invalid phone/email or password."
    ACCOUNT_EXISTS = "An account with this phone/email already exists."
    ACCOUNT_NOT_FOUND = "No account found with this email/phone number."
    INVALID_CREDENTIALS = "Incorrect login credentials."
    PASSWORD_MISMATCH = "Passwords do not match."
    PASSWORD_NEED = "You Must need to enter Your Password."
    INVALID_RESET_TOKEN = "Invalid or expired reset link."
    CREADANTIAL_NEED = "Please Enter Email Id / Phone Number and Password"

    # Info messages
    PASSWORD_RESET_SENT = "Password reset instructions have been sent to your email."
    EMAIL_VERIFICATION_SENT = "Verification email sent successfully."

    # Warning messages
    LOGIN_REQUIRED = "Please log in to continue."
    SESSION_EXPIRED = "Your session has expired. Please log in again."


class CommonMessages:
    MESSAGE_HELP_CENTER = "If the problem continues, please contact the Help Center."
    TRY_AGAIN = "Please Try Again"
    SOMETHING_WENT_WRONG = "Something Went Wrong"
    CONTACT_ADMIN = "Please Contact Admin"
    OPERATION_SUCCESS = "Operation Completed Successfully"
    INVALID_REQUEST = "Invalid Request"
    UNAUTHORIZED_ACCESS = "Unauthorized Access"


class PermissionMessages:
    ACCESS_DENIED = "You do not have permission to access this resource"
    LOGIN_REQUIRED = "Please login first"
    ADMIN_ONLY = "This action is allowed for admin only"
    FORBIDDEN = "You are not allowed to perform this action"


class ProductMessages:
    PRODUCT_NOT_FOUND = "Product not found"
    PRODUCT_CREATED = "Product Created successfully"
    PRODUCT_UPDATED = "Product updated successfully"
    PRODUCT_DELETED = "Product deleted successfully"
    INVALID_PRODUCT = "Invalid product details"
    OUT_OF_STOCK = "This product is out of stock"


class ProductCategoryMessages:
    CATEGORY_CREATED = "Category created successfully"
    CATEGORY_UPDATED = "Category updated successfully"
    CATEGORY_DELETED = "Category deleted successfully"

    CATEGORY_NOT_FOUND = "Category not found"
    CATEGORY_ALREADY_EXISTS = "Category already exists"

    INVALID_CATEGORY = "Invalid category details"
    CATEGORY_HAS_PRODUCTS = (
        "This category cannot be deleted because it contains products"
    )

    CATEGORY_STATUS_UPDATED = "Category status updated successfully"


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
