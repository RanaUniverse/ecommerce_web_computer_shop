"""
app/features/catalog/forms/brand.py

Brand Creation updateion wtforms will be here
"""

from flask_wtf import FlaskForm  # type: ignore

from wtforms import (
    StringField,
    SubmitField,
)

from wtforms.validators import (
    Optional,
    URL,
)


from .core import BOOTSTRAP_FLOATING_FORM_ATTRS, NameDescriptionMixin


class BrandAddForm(
    NameDescriptionMixin,
    FlaskForm,
):

    website_url = StringField(
        label="Website URL",
        validators=[
            Optional(),
            URL(),
        ],
        render_kw=BOOTSTRAP_FLOATING_FORM_ATTRS,
    )

    logo_filename = StringField(
        label="Logo Filename",
        validators=[
            Optional(),
        ],
        render_kw=BOOTSTRAP_FLOATING_FORM_ATTRS,
    )

    submit = SubmitField(
        label="Create Brand",
    )
