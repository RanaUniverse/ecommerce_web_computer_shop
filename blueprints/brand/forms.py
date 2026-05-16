"""
blueprints/brand/forms.py
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

from utils.wtforms_mixins import (
    BOOTSTRAP_FLOATING_FORM_ATTRS,
    NameDescriptionMixin,
)


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
