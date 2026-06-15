"""
app/features/catalog/exceptions.py
Here i will write my custom exception for the catgalog
so that i can use those easily here in my routes and in the service
"""


class CategoryNotFoundError(Exception):
    # this came when user give wrong info
    frontend_status_code = 422
    frontend_error_msg = (
        "The selected category does not exist. Please choose a valid category."
    )


class BrandNotFoundError(Exception):
    # this came when user give wrong info
    frontend_status_code = 422
    frontend_error_msg = (
        "The selected brand does not exist. Please choose a valid brand."
    )


class ProductCreationError(Exception):
    # this is when server side issue like storage problem or db problem
    # which cause this issue in the service
    frontend_status_code = 500
    frontend_error_msg = (
        "Faild to create the product, due to technical issue "
        "in backend, pls try again else contact admin / developer"
    )


class ProductThumbnailSaveError(Exception):
    pass


class ProductGalleryImageSaveError(Exception):
    pass
