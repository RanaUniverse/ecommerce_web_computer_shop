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
    get_one_category_row_by_name,
    get_all_category_names,
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
    list_of_category = get_all_category_names()
    if form.validate_on_submit():  # type: ignore
        name = form.name.data
        description = form.description.data
        category_name = form.category_name.data
        # i will add brand id later in this product table
        brand_id = form.brand_id.data  # type: ignore
        quantity = form.quantity.data
        # i will add hsn no later in my product table
        hsn_no = form.hsn_no.data  # type: ignore
        price_purchase = form.purchase_price.data
        price_sell = form.sell_price.data
        price_mrp = form.mrp_price.data

        if not category_name:
            category_id = None
        else:
            category_obj = get_one_category_row_by_name(category_name)
            if not category_obj:
                category_id = None
                flash(
                    message="You Entered a Wrong Category Name",
                    category="warning",
                )
                return render_template(
                    "product/add.html",
                    form=form,
                    items=list_of_category,
                )

            else:
                category_id = category_obj.id_

        # the decimal and float problem i need to solve later in postgres change to decimal
        new_product_obj = add_one_product_row(
            product_obj=ProductModel(
                name=name or "",
                description=description,
                quantity=quantity or 0,
                mrp_price=price_mrp or None,  # type: ignore
                purchase_price=price_purchase or None,  # type: ignore
                sell_price=price_sell or None,  # type: ignore
                category_id=category_id,
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

    else:
        print("FORM NOT VALID")
        print(form.errors)

    return render_template(
        "product/add.html",
        form=form,
        items=list_of_category,
    )
