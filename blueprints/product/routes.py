"""
blueprints/product/routes.py
Here i will make the product links and how it will work in this place.

I will use to store the images in the static folders
Because the images are meant to shows alwyas easily


works left:
product_id=new_product_obj.id_, # type: ignore
i need to chagne this
"""

from flask import (
    Blueprint,
    render_template,
    flash,
    url_for,
    redirect,
)

from werkzeug.datastructures import FileStorage


from .forms import ProductAddForm


from services.database.controllers import (
    add_one_product_row,
    get_one_category_row_by_name,
    get_all_category_names,
    get_all_brands_id_name,
    get_one_brand_row_by_id,
)

from services.database.models import (
    ProductModel,
)

from services.storage import save_product_thumbnail_and_create_row

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
    form.brand_id.choices = [("", "Select Brand")] + get_all_brands_id_name()  # type: ignore
    list_of_category = get_all_category_names()

    if form.validate_on_submit():  # type: ignore
        name = form.name.data
        description = form.description.data
        category_name = form.category_name.data
        # i will add brand id later in this product table
        brand_id = form.brand_id.data  # type: ignore
        quantity = form.quantity.data
        hsn_no = form.hsn_no.data
        price_purchase = form.purchase_price.data
        price_sell = form.sell_price.data
        price_mrp = form.mrp_price.data
        alt_text = form.thumbnail_alt_text.data

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

        if not brand_id:
            brand_obj = None
        else:
            brand_obj = get_one_brand_row_by_id(brand_id)

            if not brand_obj:
                flash(
                    message="You Selected Invalid Brand",
                    category="warning",
                )

                return render_template(
                    "product/add.html",
                    form=form,
                    items=list_of_category,
                )

        # the decimal and float problem i need to solve later in postgres change to decimal
        new_product_obj = add_one_product_row(
            product_obj=ProductModel(
                name=name or "",
                description=description,
                quantity=quantity or 0,
                hsn_no=hsn_no,
                mrp_price=price_mrp or None,  # type: ignore
                purchase_price=price_purchase or None,  # type: ignore
                sell_price=price_sell or None,  # type: ignore
                category_id=category_id,
                brand_obj=brand_obj,
            )
        )

        if not new_product_obj:
            flash(
                message="Somethign is wrong",
                category="error",
            )
            return redirect(url_for("product_bp.add_product"))

        # this else part comes means the product creation has successfull
        # else:
        message = "Product created successfully"
        message_category = "success"

        # this time i will need to create the folder to insert the image
        thumbnail_file: FileStorage = form.image_thumbnail.data
        if thumbnail_file.filename:
            saved_img_path = save_product_thumbnail_and_create_row(
                image_file=thumbnail_file,
                product_id=new_product_obj.id_,  # type: ignore
                alt_text=alt_text,
            )

            if saved_img_path:
                message += " and thumbnail image saved successfully."

            else:
                # i wish this should never run as image save should go right
                message += (
                    ", but thumbnail image could not be saved. " "Please contact admin."
                )
                message_category = "warning"

        flash(
            message=message,
            category=message_category,
        )

        # for now it send to this page, later i need to make this page good upper fun
        return redirect(
            url_for(
                endpoint="product_bp.product_info",
                product_id=new_product_obj.id_,
            ),
        )

    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{field.upper()}: {error}", "danger")

    return render_template(
        "product/add.html",
        form=form,
        items=list_of_category,
    )
