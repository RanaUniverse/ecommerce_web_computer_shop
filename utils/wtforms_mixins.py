"""
utils/wtforms_mixins.py
Here i will make some custom wtforms class which will works in other class easily
i will use some classes from here to other flask_wtf forms class
"""

from flask_wtf.file import FileAllowed  # type: ignore

from wtforms import (
    StringField,
    TextAreaField,
    FileField,
)
from wtforms.validators import (
    DataRequired,
    Length,
    Optional,
    URL,
)

from utils.config import ALLOWED_IMAGE_EXTENSIONS

# i use below value for the bs5's input floating thigns
BOOTSTRAP_FLOATING_FORM_ATTRS: dict[str, str] = {
    "placeholder": " ",
    "class": "form-control",
}


class NameDescriptionMixin:

    name = StringField(
        label="Enter The Name",
        validators=[
            DataRequired(),
            Length(min=1, max=100),
        ],
        render_kw=BOOTSTRAP_FLOATING_FORM_ATTRS,
    )

    description = TextAreaField(
        label="Description",
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


class ThumbnailImageMixin:
    """
    i will make this so that image validation will done here
    """

    image_thumbnail = FileField(
        label="Product's Thumbnail",
        validators=[
            Optional(),
            FileAllowed(
                upload_set=ALLOWED_IMAGE_EXTENSIONS,
                message=(
                    f"Invalid image format, please select any "
                    f"{ALLOWED_IMAGE_EXTENSIONS} Image only"
                ),
            ),
        ],
        render_kw={
            "accept": "image/*",
            "class": "form-control form-control-lg",
        },
    )

    thumbnail_alt_text = StringField(
        label="Thumbnail Alt Text",
        validators=[
            Optional(),
            Length(
                max=200,
                message="Alt text must be below 200 characters.",
            ),
        ],
        render_kw=BOOTSTRAP_FLOATING_FORM_ATTRS,
    )

    thumbnail_url = StringField(
        label="Paste Image Link of already uploded image",
        validators=[
            Optional(),
            URL(
                message="The Url You Enter is Invalid, pls upload image instead",
            ),
        ],
        render_kw=BOOTSTRAP_FLOATING_FORM_ATTRS,
    )
