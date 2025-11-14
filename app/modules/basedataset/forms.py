from flask_wtf import FlaskForm
from wtforms import SubmitField


class BasedatasetForm(FlaskForm):
    submit = SubmitField('Save basedataset')
