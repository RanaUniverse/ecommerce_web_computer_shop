"""
app/features/catalog/forms/category.py

Category making with flask-wtforms will be here so that it will easy
"""

from flask_wtf import FlaskForm  # type: ignore
from flask_wtf.file import FileAllowed  # type: ignore

from wtforms import (
    StringField,
    SubmitField,
    TextAreaField,
)

from wtforms.validators import (
    Length,
    Optional,
)


from .core import (
    BOOTSTRAP_FLOATING_FORM_ATTRS,
    NameDescriptionMixin,
    ThumbnailImageMixin,
)


class CategoryAddForm(
    NameDescriptionMixin,
    ThumbnailImageMixin,
    FlaskForm,
):
    """
    I will make the category validation with its information
    """

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
    # parent_id = StringField(
    #     label="Parent Category ID (i will change this)",
    #     validators=[
    #         Optional(),
    #     ],
    #     render_kw=BOOTSTRAP_FLOATING_FORM_ATTRS,
    # )
    parent_category_name = StringField(
        label="Select Parent Category",
        validators=[
            Optional(),
        ],
        render_kw=BOOTSTRAP_FLOATING_FORM_ATTRS,
    )

    submit = SubmitField(
        label="Create Category",
    )
