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


class AuthMessages:
    LOGIN_SUCCESS: Final = "Login successful"
    LOGIN_FAILED: Final = "Invalid email or password"
    LOGOUT_SUCCESS: Final = "Logged out successfully"
    ACCOUNT_CREATED: Final = "Account created successfully"
    ACCOUNT_EXISTS: Final = "Account already exists"
    PASSWORD_RESET_SENT: Final = "Password reset link sent to your email"
    PASSWORD_RESET_SUCCESS: Final = "Password reset successful"


class CommonMessages:
    TRY_AGAIN: Final = "Please try again"
    SOMETHING_WENT_WRONG: Final = "Something went wrong"
    CONTACT_ADMIN: Final = "Please contact admin"
    OPERATION_SUCCESS: Final = "Operation completed successfully"
    INVALID_REQUEST: Final = "Invalid request"
    UNAUTHORIZED_ACCESS: Final = "Unauthorized access"


class PermissionMessages:
    ACCESS_DENIED: Final = "You do not have permission to access this resource"
    LOGIN_REQUIRED: Final = "Please login first"
    ADMIN_ONLY: Final = "This action is allowed for admin only"
    FORBIDDEN: Final = "You are not allowed to perform this action"


class ProductMessages:
    PRODUCT_NOT_FOUND: Final = "Product not found"
    PRODUCT_ADDED: Final = "Product added successfully"
    PRODUCT_UPDATED: Final = "Product updated successfully"
    PRODUCT_DELETED: Final = "Product deleted successfully"
    INVALID_PRODUCT: Final = "Invalid product details"
    OUT_OF_STOCK: Final = "This product is out of stock"


class CartMessages:
    ADDED_TO_CART: Final = "Product added to cart"
    REMOVED_FROM_CART: Final = "Product removed from cart"
    CART_EMPTY: Final = "Your cart is empty"
    CART_UPDATED: Final = "Cart updated successfully"
    ITEM_NOT_IN_CART: Final = "Item not found in cart"


class OrderMessages:
    ORDER_SUCCESS: Final = "Order placed successfully"
    ORDER_FAILED: Final = "Failed to place order"
    PAYMENT_FAILED: Final = "Payment failed"
    PAYMENT_SUCCESS: Final = "Payment successful"
    ORDER_CANCELLED: Final = "Order cancelled successfully"
    ORDER_NOT_FOUND: Final = "Order not found"
    ORDER_ALREADY_PROCESSED: Final = "Order already processed"
