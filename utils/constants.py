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

from typing import Final


class CommonMessages:
    TRY_AGAIN: Final = "Please try again"
    SOMETHING_WENT_WRONG: Final = "Something went wrong"
    CONTACT_ADMIN: Final = "Please contact admin"


class AuthMessages:
    LOGIN_SUCCESS: Final = "Login successful"
    LOGIN_FAILED: Final = "Invalid email or password"
    LOGOUT_SUCCESS: Final = "Logged out successfully"


class PermissionMessages:
    ACCESS_DENIED: Final = "You do not have permission"
    LOGIN_REQUIRED: Final = "Please login first"


class ProductMessages:
    OUT_OF_STOCK: Final = "Product is out of stock"
    PRODUCT_NOT_FOUND: Final = "Product not found"


class CartMessages:
    ADDED_TO_CART: Final = "Product added to cart"
    REMOVED_FROM_CART: Final = "Product removed from cart"


class OrderMessages:
    ORDER_SUCCESS: Final = "Order placed successfully"
    PAYMENT_FAILED: Final = "Payment failed"
