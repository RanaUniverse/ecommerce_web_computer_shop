"""
app/features/catalog/routes/product.py

Product Related routes layer will be written here

Here i will make the product links and how it will work in this place.

I will use to store the images in the static folders
Because the images are meant to shows alwyas easily


works left:
product_id=new_product_obj.id_, # type: ignore
i need to chagne this
"""

from flask import (
    Blueprint,
    flash,
    render_template,
    redirect,
    url_for,
)

from werkzeug.datastructures import FileStorage


from .. import exceptions as exc

from ..forms.product import ProductAddForm

from ..schema.product import ProductCreate

from ..service import brand as brand_ser
from ..service import product as product_ser
from ..service import category as category_ser

from ....shared.config import IMAGE_NOT_FOUND_IMAGE_PATH

from ....shared.utils.constants_messages import (
    BS5Alert,
    ProductMessages,
)

product_bp = Blueprint(
    name="product_bp",
    import_name=__name__,
    template_folder="templates",
)


# i make this because for the things related to this
@product_bp.context_processor
def inject_brand():
    return {
        "IMAGE_NOT_FOUND_IMG": IMAGE_NOT_FOUND_IMAGE_PATH,
    }


@product_bp.route("/view/<string:product_id>")
def product_info(product_id: str):
    """
    This will shows the product information like name
    images and so on for now it will shows the thumbnail image
    and little informaion aobut title, price for public
    """
    obj = product_ser.get_product_details_for_public(
        product_id=product_id,
    )
    if not obj:
        return "Product Not Exists with the id of" "<br>" f"{product_id.upper()}"

    # return f"{obj}"
    return render_template(
        template_name_or_list="product/info.html",
        product_obj=obj,
        product_thumbnail_obj=obj.product_thumbnail_image_obj,
        gallery_images=obj.product_gallery_image_obj,
    )


@product_bp.route(
    rule="/add",
    methods=["GET", "POST"],
)
def add_product():

    form = ProductAddForm()

    existing_brands = brand_ser.get_all_brands_id_name_pair()
    form.brand_id.choices = [("", "Select Brand")] + existing_brands  # type: ignore

    list_of_category = category_ser.get_list_of_all_category_name()

    if form.validate_on_submit():  # type: ignore
        name = form.name.data or ""
        description = form.description.data or None
        category_name = form.category_name.data or None
        brand_id: str | None = form.brand_id.data or None
        quantity = form.quantity.data
        hsn_no = form.hsn_no.data
        price_purchase = form.purchase_price.data
        price_sell = form.sell_price.data
        price_mrp = form.mrp_price.data
        thumbnail_url = form.thumbnail_url.data or None
        alt_text = form.thumbnail_alt_text.data or None
        private_note = form.private_note.data or None

        # here the ignore is ok, as this will validate and convert its data as pydnatic model
        product_create_schema_obj = ProductCreate(
            name=name,
            description=description,
            hsn_no=hsn_no,
            mrp_price=price_mrp,  # type: ignore
            sell_price=price_sell,  # type: ignore
            brand_id=brand_id,
            # the name to id making will in the service layer
            # category_id=category_id,
            quantity=quantity,
            purchase_price=price_purchase,  # type: ignore
            private_note=private_note,
            # creator_id= somethigns_will_do_later_after_role_and_login
        )
        gallery_images: list[FileStorage] = form.gallery_images.data

        try:

            obj = product_ser.create_new_product_row_with_images(
                product_obj=product_create_schema_obj,
                thumbnail_file=form.image_thumbnail.data,
                thumbnail_url=thumbnail_url,
                thumbnail_alt_text=alt_text,
                gallery_images=gallery_images,
                category_name=category_name,
            )
            flash(
                message=ProductMessages.PRODUCT_CREATED,
                category=BS5Alert.SUCCESS,
            )
            return redirect(
                location=url_for(
                    endpoint="product_bp.product_info",
                    product_id=obj.id_,
                ),
            )
            # TODO
            # i will add here extra mechanism so that it will say if thumbnail or gallery
            # images has been saved successfully or not

        # except product_ser.CategoryNotFoundError as e:
        #     flash(
        #         message=e.frontend_error_msg,
        #         category=BS5Alert.WARNING,
        #     )
        #     status_code = e.frontend_status_code

        # except product_ser.BrandNotFoundError as e:
        #     flash(
        #         message=e.frontend_error_msg,
        #         category=BS5Alert.WARNING,
        #     )
        #     status_code = e.frontend_status_code

        # except product_ser.ProductCreationError as e:
        #     flash(
        #         message=e.frontend_error_msg,
        #         category=BS5Alert.WARNING,
        #     )
        #     status_code = e.frontend_status_code

        except (
            exc.CategoryNotFoundError,
            exc.BrandNotFoundError,
            exc.ProductCreationError,
        ) as e:
            flash(
                message=e.frontend_error_msg,
                category=BS5Alert.WARNING,
            )
            status_code = e.frontend_status_code

        except exc.ProductThumbnailSaveError:
            flash(
                message="Product created, but the thumbnail image could not be saved.",
                category=BS5Alert.WARNING,
            )
            status_code = 400

        except exc.ProductGalleryImageSaveError:
            flash(
                message="Product created, but one or more gallery images could not be saved.",
                category=BS5Alert.WARNING,
            )
            status_code = 405

        except Exception:
            flash(
                message="An unexpected error occurred. Please try again later.",
                category=BS5Alert.DANGER,
            )
            status_code = 406

        return (
            render_template(
                "product/add.html",
                form=form,
                items=list_of_category,
            ),
            status_code,
        )

    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(
                    message=f"{field.upper()}: {error}",
                    category=BS5Alert.DANGER,
                )

    return render_template(
        "product/add.html",
        form=form,
        items=list_of_category,
    )
