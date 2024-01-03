from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms import StringField
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("Submit")


