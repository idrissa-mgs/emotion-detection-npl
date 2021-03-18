from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class EmotionForm(FlaskForm):
    TextAreaField = StringField("Hi, tell me how do you feel ?", validators=[DataRequired()])
    
    submit = SubmitField("Get the emotion")
