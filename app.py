from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"

class ImageForm(FlaskForm):
    url = StringField(validators=[InputRequired()], render_kw={"placeholder": "URL"})
    file_name = StringField(validators=[InputRequired()], render_kw={"placeholder": "FILE_NAME"})
    submit = SubmitField("Download")

def download_image(url, file_name):
    r = requests.get(url)
    with open(file_name + '.jpg', 'wb') as f:
        f.write(r.content)



@app.route('/', methods=['GET', 'POST'])
def index():
    form = ImageForm()
    if form.validate_on_submit():
        download_image(form.url.data, form.file_name.data)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)