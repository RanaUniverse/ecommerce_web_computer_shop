"""
app/features/catalog/service_product.py

For product related business logic will be kept here
"""

from sqlmodel import Session

from werkzeug.datastructures import FileStorage


from .. import exceptions as exc

from ..operations import brand as brand_ops
from ..operations import category as category_ops
from ..operations import image as image_ops
from ..operations import product as product_ops

from ..models.image import ProductThumbnailImageModel
from ..models.product import ProductModel

from ..schema.product import ProductCreate, ProductOutAdmin, ProductDetailOutPublic

from ....shared.database import engine

from .storage.product import (
    save_product_gallery_images_and_create_rows,
    save_product_thumbnail_and_create_row,
)


def create_new_product_row_with_images(
    product_obj: ProductCreate,
    category_name: str | None,
    thumbnail_file: FileStorage | None,
    thumbnail_url: str | None,
    thumbnail_alt_text: str | None,
    gallery_images: list[FileStorage],
) -> ProductOutAdmin:
    """
    This will do all the operations of insert the product into the table
    save the iamges in ssd and store the informaiotn in the tables

        thumbnail_file: This is image file
        gallery_images: list[FileStorage] = form.gallery_images.data
    """
    with Session(engine) as session:
        # First i will check the Brand Id validation
        if product_obj.brand_id:
            brand_obj = brand_ops.get_one_brand_row_by_id(
                session=session,
                brand_id=product_obj.brand_id,
            )
            if not brand_obj:
                raise exc.BrandNotFoundError(
                    "Brand selected is not found, maybe user  did some js change.",
                )

        # NOw from the category name i will make the id and insert in the schema
        category_id = None
        if category_name:
            category_obj = category_ops.get_one_category_row_by_name(
                session=session,
                name=category_name,
            )
            if not category_obj:
                raise exc.CategoryNotFoundError(
                    f"Category: {category_name} not Exixts.",
                )
            category_id = category_obj.id_

        # i will want to insert the category_id there explicitely
        product_obj.category_id = category_id
        product_model = ProductModel.model_validate(
            obj=product_obj,
            from_attributes=True,
        )

        saved_product = product_ops.add_one_product_row(
            session=session,
            product_obj=product_model,
        )

        if not saved_product:
            raise exc.ProductCreationError(
                "Failed To Create the Product",
            )

        # Now after the product has inserted i want to insert the thumbnail here
        if thumbnail_file and thumbnail_file.filename:

            thumbnail_obj = save_product_thumbnail_and_create_row(
                session=session,
                image_file=thumbnail_file,
                product_id=saved_product.id_,
                alt_text=thumbnail_alt_text,
                creator_id=saved_product.creator_id,
                external_url=thumbnail_url,
            )
            if not thumbnail_obj:
                raise exc.ProductThumbnailSaveError(
                    "Save Thumbnail files got fails",
                )

        elif thumbnail_url:
            thumbnail_obj = image_ops.add_product_thumbnail_by_external_url(
                session=session,
                thumbnail_obj=ProductThumbnailImageModel(
                    external_url=thumbnail_url,
                    alt_text=thumbnail_alt_text,
                    creator_id=product_obj.creator_id,
                    product_id=saved_product.id_,
                ),
            )
            if not thumbnail_obj:
                raise exc.ProductThumbnailSaveError(
                    "Saving thumbnail with url only fails",
                )

        real_gallery_images: list[FileStorage] = []

        for f in gallery_images:
            if f and f.filename:
                real_gallery_images.append(f)

        if real_gallery_images:
            # later i will use product schema out which will have must str not none
            saved_images = save_product_gallery_images_and_create_rows(
                session=session,
                image_files=real_gallery_images,
                product_id=saved_product.id_,
                creator_id=product_obj.creator_id,
            )
            if not saved_images:
                raise exc.ProductGalleryImageSaveError(
                    "Gallery images saving fails",
                )
        out_obj = ProductOutAdmin.model_validate(
            obj=saved_product,
            from_attributes=True,
        )
        return out_obj


def get_product_details_for_admin(
    product_id: str,
) -> ProductOutAdmin | None:
    """
    i will pass product_id and it will give the product informaiton

    Later i will do check if this is admin only then send the details
    """
    with Session(engine) as session:
        model_obj = product_ops.get_one_product_row_by_id(
            session=session,
            product_id=product_id,
        )
        if not model_obj:
            return None
        obj = ProductOutAdmin.model_validate(
            obj=model_obj,
            from_attributes=True,
        )
        return obj


def get_product_details_for_public(
    product_id: str,
) -> ProductDetailOutPublic | None:
    """
    i will pass the product_id it will give me the product_details_out schema so
    that i can shows this to the public for product details page
    """
    with Session(engine) as session:
        model_obj = product_ops.get_one_product_row_by_id(
            session=session,
            product_id=product_id,
        )
        if not model_obj:
            return None
        obj = ProductDetailOutPublic.model_validate(
            obj=model_obj,
            from_attributes=True,
        )
        return obj
