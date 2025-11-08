from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class CartCreateDatasetForm(FlaskForm):
    name = StringField(
        "Dataset Name",
        validators=[DataRequired(message="Dataset name is required"), Length(max=150)],
        render_kw={"placeholder": "Enter dataset name"}
    )
    description = TextAreaField(
        "Description",
        validators=[Length(max=1000)],
        render_kw={"placeholder": "Enter dataset description (optional)"}
    )
    submit = SubmitField("Create My Dataset")
