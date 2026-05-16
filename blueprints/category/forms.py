"""
blueprints/category/forms.py
"""

from flask_wtf import FlaskForm  # type: ignore
from flask_wtf.file import FileAllowed  # type: ignore

from wtforms import (
    FileField,
    StringField,
    SubmitField,
    TextAreaField,
)

from wtforms.validators import (
    DataRequired,
    Length,
    Optional,
)

BOOTSTRAP_FLOATING_FORM_ATTRS: dict[str, str] = {
    "placeholder": " ",
    "class": "form-control",
}


class CategoryAddForm(FlaskForm):

    name = StringField(
        label="Category Name",
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

    # i will later use to select bs icons here
    icon_name = StringField(
        label="Icon Name",
        validators=[
            Optional(),
        ],
        render_kw=BOOTSTRAP_FLOATING_FORM_ATTRS,
    )

    private_note = TextAreaField(
        label="Private Note",
        validators=[
            Optional(),
            Length(max=5000),
        ],
        render_kw={
            **BOOTSTRAP_FLOATING_FORM_ATTRS,
            "rows": 5,
            "placeholder": "Write Private Informations",
        },
    )

    # i will later use to say to give category name and id to select
    parent_id = StringField(
        label="Parent Category ID (i will change this)",
        validators=[
            Optional(),
        ],
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

    submit = SubmitField(
        label="Create Category",
    )
