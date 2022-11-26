from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ToolForm(FlaskForm):
    message = TextAreaField('Type here!', render_kw={"rows": 18, "cols": 150}, validators=[DataRequired()])
    submit = SubmitField('Submit')

