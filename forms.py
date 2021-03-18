from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class EmotionForm(FlaskForm):
    text_sentiment = StringField("Hi, tell me how do you feel ?", validators=[DataRequired()])
    
    submit = SubmitField("Get the emotion")