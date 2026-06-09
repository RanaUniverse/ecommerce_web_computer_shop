"""
app/features/catalog/operations/image.py

"""

"""
services/database/product_image_data/operation.py
Here i will make the table of the product_image and then
i will insert the row of image location and data
"""

from typing import TypedDict


from sqlmodel import Session, select


from ..models.image import ProductGalleryImageModel, ProductThumbnailImageModel

from ....shared.utils.custom_logger import logger


# i have defined thsi in another module i need to refactor this later
class GalleryImageRecord(TypedDict):
    image_path: str
    order: int


def add_one_product_image_row(
    session: Session,
    product_image_obj: ProductGalleryImageModel,
) -> ProductGalleryImageModel | None:

    try:
        session.add(product_image_obj)
        session.commit()
        session.refresh(product_image_obj)

        return product_image_obj

    except Exception as e:
        logger.error(f"Failed to save product image: {e}")
        return None


def add_product_thumbnail_image_row(
    session: Session,
    thumbnail_obj: ProductThumbnailImageModel,
) -> ProductThumbnailImageModel | None:
    """
    It will try to insert the thumbnail_img obj into its row
    """
    try:
        session.add(thumbnail_obj)
        session.commit()
        session.refresh(thumbnail_obj)
        return thumbnail_obj

    except Exception as e:
        logger.error(f"Failed to save into thumbnail image row in db, {e}")
        return None


def product_thumbnail_img_row(
    session: Session,
    product_id: str,
) -> ProductGalleryImageModel | None:
    """
    Before calling this i need to make sure product_id
    is present so that it will not cause issue of not found
    """
    statement = select(ProductGalleryImageModel).where(
        ProductGalleryImageModel.product_id == product_id
    )
    obj = session.exec(statement).first()
    return obj


# TODO i will make this take the image schema not the things like this
def add_product_thumbnail_by_external_url(
    session: Session,
    thumbnail_obj: ProductThumbnailImageModel,
) -> ProductThumbnailImageModel | None:
    """
    External Url and Alt Text
    This two is only necessary to work with this
    """
    try:
        session.add(thumbnail_obj)
        session.commit()
        session.refresh(thumbnail_obj)
        return thumbnail_obj

    except Exception as e:
        logger.warning(
            msg=f"Inserting product's thumbnail's external url got fails, {e}",
        )
        return None


def add_product_gallery_image_rows(
    session: Session,
    image_records: list[GalleryImageRecord],
    product_id: str,
    creator_id: str | None = None,
) -> list[ProductGalleryImageModel] | None:
    """
    The order is in the int part of the image_records so i will use this.
    later i will add alt text and external link using a schema obj
    int-> it will say how many images has been inserted in the db table
    """
    gallery_objs: list[ProductGalleryImageModel] = []

    for one_image in image_records:
        obj = ProductGalleryImageModel(
            filepath=one_image.get("image_path"),
            display_order=one_image.get("order"),
            product_id=product_id,
            creator_id=creator_id,
        )
        gallery_objs.append(obj)

    try:
        session.add_all(gallery_objs)
        session.commit()

        for obj in gallery_objs:
            session.refresh(obj)

        # print(gallery_objs)
        # for _ in gallery_objs:
        #     print(_)

        return gallery_objs

    except Exception as e:
        logger.error(f"Failed to save into thumbnail image row in db, {e}")
        return None
