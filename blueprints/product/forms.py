"""
blueprints/product/forms.py
Hee i will write the code logic for product insertion form
i will use flask form with wtform for against the csrf toke.
"""

from typing import Any

from flask_wtf import (  # type: ignore
    FlaskForm,
)

from wtforms import (
    DecimalField,
    IntegerField,
    MultipleFileField,
    SelectField,
    StringField,
    SubmitField,
)

from flask_wtf.file import FileAllowed  # type: ignore

from wtforms.validators import (
    Length,
    NumberRange,
    Optional,
)

from utils.wtforms_mixins import (
    BOOTSTRAP_FLOATING_FORM_ATTRS,
    NameDescriptionMixin,
    ThumbnailImageMixin,
)


class ProductAddForm(
    NameDescriptionMixin,
    ThumbnailImageMixin,
    FlaskForm,
):
    """
    This is for showing the user the page to take product information
    and product images and so on
    """

    hsn_no = IntegerField(
        label="HSN No.",
        validators=[
            Optional(),
            NumberRange(
                min=100000,
                max=99999999,
                message="HSN Number must contain 6 to 8 digits...",
            ),
        ],
        render_kw=BOOTSTRAP_FLOATING_FORM_ATTRS,
    )

    # category_id = SelectField(
    #     label="Select The Category",
    #     # i will basically take this from db
    #     choices=[
    #         ("aaabbbccc", "Computer"),
    #         ("bbbcccddd", "Laptop"),
    #         ("cccdddeee", "Server"),
    #     ],
    #     render_kw={
    #         **BOOTSTRAP_FLOATING_FORM_ATTRS,
    #         "class": "form-select",
    #     },
    # )

    category_name = StringField(
        label="Select Category",
        validators=[
            Optional(),
        ],
        render_kw=BOOTSTRAP_FLOATING_FORM_ATTRS,
    )

    quantity = IntegerField(
        label="Quantity",
        validators=[
            Optional(),
            NumberRange(min=0),
        ],
        render_kw=BOOTSTRAP_FLOATING_FORM_ATTRS,
    )

    purchase_price = DecimalField(
        label="Purchase Price",
        validators=[
            Optional(),
            NumberRange(min=0),
        ],
        places=2,
        render_kw=BOOTSTRAP_FLOATING_FORM_ATTRS,
    )

    sell_price = DecimalField(
        label="Sell Price",
        validators=[
            Optional(),
            NumberRange(min=0),
        ],
        places=2,
        render_kw=BOOTSTRAP_FLOATING_FORM_ATTRS,
    )

    mrp_price = DecimalField(
        label="MRP Price",
        validators=[Optional()],
        places=2,
        render_kw=BOOTSTRAP_FLOATING_FORM_ATTRS,
    )

    # i have this this in the table yet i will do this
    brand_id = SelectField(
        label="Brand of Product",
        validators=[
            Optional(),
            Length(max=100),
        ],
        choices=[
            ("xxx", "Select Brand"),
        ],
        render_kw={
            **BOOTSTRAP_FLOATING_FORM_ATTRS,
            "class": "form-select",
        },
    )

    # i have not implimentate yet this
    gallery_images = MultipleFileField(
        label="Product's Gallery Images",
        validators=[
            Optional(),
        ],
        render_kw={
            "accept": "image/*",
            "class": "form-control",
            "multiple": True,
        },
    )

    # below here i will add a idea of upload many images
    submit = SubmitField(
        label="Create Product",
    )

    # This below i make from the docs of custom validation
    # https://wtforms.readthedocs.io/en/2.3.x/validators/#custom-validators
    def validate(self, extra_validators: Any = None):

        is_valid = super().validate(extra_validators=extra_validators)

        if not is_valid:
            return False

        uploaded_image = self.image_thumbnail.data
        image_url = self.thumbnail_url.data

        has_uploaded_image = bool(uploaded_image and uploaded_image.filename)

        has_image_url = bool(image_url and image_url.strip())

        if has_uploaded_image and has_image_url:
            message = (
                "Please use ONLY ONE option: "
                "either upload an image OR provide an image URL."
            )
            # self.image_thumbnail.errors.append(message)
            self.thumbnail_url.errors.append(message)  # type: ignore

            return False

        return True
