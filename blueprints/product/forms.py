"""
blueprints/product/forms.py
Hee i will write the code logic for product insertion form
i will use flask form with wtform for against the csrf toke.
"""

from flask_wtf import (  # type: ignore
    FlaskForm,
)

from wtforms import (
    DecimalField,
    FileField,
    IntegerField,
    MultipleFileField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)

from flask_wtf.file import FileAllowed  # type: ignore

from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange,
    Optional,
)

BOOTSTRAP_FLOATING_FORM_ATTRS: dict[str, str] = {
    "placeholder": " ",
    "class": "form-control",
}


class ProductAddForm(FlaskForm):
    """
    This is for showing the user the page to take product information
    and product images and so on
    """

    name = StringField(
        label="Product Name",
        validators=[
            DataRequired(),
            Length(min=3, max=200),
        ],
        render_kw=BOOTSTRAP_FLOATING_FORM_ATTRS,
    )

    description = TextAreaField(
        label="Product Description",
        validators=[
            Optional(),
            Length(max=5000),
        ],
        render_kw={
            **BOOTSTRAP_FLOATING_FORM_ATTRS,
            "rows": 5,
            "placeholder": "Enter Your Product's Details...",
        },
    )

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

    category_id = SelectField(
        label="Select The Category",
        # i will basically take this from db
        choices=[
            ("aaabbbccc", "Computer"),
            ("bbbcccddd", "Laptop"),
            ("cccdddeee", "Server"),
        ],
        render_kw={
            **BOOTSTRAP_FLOATING_FORM_ATTRS,
            "class": "form-select",
        },
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

    image_thumbnail = FileField(
        label="Product's Thumbnail",
        validators=[
            Optional(),
            FileAllowed(
                upload_set=[
                    "jpg",
                    "jpeg",
                    "png",
                    "webp",
                ],
                message="Please Select Images Only",
            ),
        ],
        render_kw={
            "accept": "image/*",
            "class": "form-control form-control-lg",
        },
    )

    # i have this this in the table yet i will do this
    brand_id = SelectField(
        label="Brand of Product",
        validators=[
            Optional(),
            Length(max=100),
        ],
        choices=[
            ("aaabbbccc", "Dell"),
            ("bbbcccddd", "HP India"),
            ("cccdddeee", "Rana"),
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
