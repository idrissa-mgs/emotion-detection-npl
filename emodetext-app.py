from flask import render_template,Flask ,url_for, flash, redirect, request
from forms import EmotionForm
from emo_detext import predict_emo
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/emodetext', methods=['GET', 'POST'])
def emodetext():
    form = EmotionForm()
    if form.validate_on_submit():
        text = form.text_sentiment.data
        emotion = predict_emo([text])
        return render_template("emotion.html", form= form , emotion = emotion)

    return render_template("emodetext.html", form = form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


