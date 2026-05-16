"""
blueprints/product/routes.py
Here i will make the product links and how it will work in this place.

I will use to store the images in the static folders
Because the images are meant to shows alwyas easily
"""

from flask import (
    Blueprint,
    render_template,
    flash,
    url_for,
    redirect,
)

from .forms import ProductAddForm


from services.database.controllers import (
    add_one_product_row,
)
from services.database.models import (
    ProductModel,
)

product_bp = Blueprint(
    name="product_bp",
    import_name=__name__,
    template_folder="templates",
)


@product_bp.route("/<string:product_id>")
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


@product_bp.route(
    rule="/add",
    methods=["GET", "POST"],
)
def add_product():

    form = ProductAddForm()

    if form.validate_on_submit():  # type: ignore
        name = form.name.data
        description = form.description.data
        category_id = form.category_id.data
        brand_id = form.brand_id.data
        quantity = form.quantity.data
        hsn_no = form.hsn_no.data
        price_purchase = form.purchase_price.data
        price_sell = form.sell_price.data
        price_mrp = form.mrp_price.data

        print("NAME:", name, type(name))
        print("DESCRIPTION:", description, type(description))
        print("CATEGORY ID:", category_id, type(category_id))  # type: ignore
        print("BRAND ID:", brand_id, type(brand_id))  # type: ignore this is because this is a dropdown
        print("QUANTITY:", quantity, type(quantity))
        print("HSN NO:", hsn_no, type(hsn_no))
        print("PURCHASE PRICE:", price_purchase, type(price_purchase))
        print("SELL PRICE:", price_sell, type(price_sell))
        print("MRP PRICE:", price_mrp, type(price_mrp))

        # the decimal and float problem i need to solve later in postgres change to decimal
        new_product_obj = add_one_product_row(
            product_obj=ProductModel(
                name=name or "",
                description=description,
                quantity=quantity or 0,
                mrp_price=price_mrp or None,  # type: ignore
                purchase_price=price_purchase or None,  # type: ignore
                sell_price=price_sell or None,  # type: ignore
            )
        )

        if not new_product_obj:
            flash(
                message="Somethign is wrong",
                category="error",
            )
            return redirect(url_for("product_bp.add_product"))
        else:
            flash(
                message="Created product",
                category="success",
            )
            # for now it send to this page, later i need to make this page good upper fun
            return redirect(
                url_for(
                    endpoint="product_bp.product_info",
                    product_id=new_product_obj.id_,
                ),
            )

    return render_template(
        "product/add.html",
        form=form,
    )
