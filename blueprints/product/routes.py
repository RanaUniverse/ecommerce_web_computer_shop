"""
blueprints/product/routes.py
Here i will make the product links and how it will work in this place.
"""

from flask import Blueprint, render_template

product_bp = Blueprint(
    name="product_bp",
    import_name=__name__,
    template_folder="templates",
)


@product_bp.route("/product/<string:product_id>")
def product_info(product_id: str):
    """
    This will shows the product information like name
    images and so on
    """

    image_folder = f"uploads/products/{product_id}"
    images = [
        f"{image_folder}/1.png",
        f"{image_folder}/2.png",
        f"{image_folder}/3.png",
        f"{image_folder}/4.png",
        f"{image_folder}/5.png",
        f"{image_folder}/6.png",
        f"{image_folder}/7.png",
        f"{image_folder}/8.png",
        f"{image_folder}/9.png",
    ]

    product = {
        "id": product_id,
        "name": f"Product {product_id}",
        "description": "This is a demo product",
    }
    return render_template(
        "product/info.html",
        product=product,
        images=images,
    )
