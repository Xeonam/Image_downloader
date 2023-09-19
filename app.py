from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
import requests
from pathfinder import get_folder_path, get_os
import re

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"


class ImageForm(FlaskForm):
    url = StringField(validators=[InputRequired()],
                      render_kw={"placeholder": "URL"})
    file_name = StringField(validators=[InputRequired()], render_kw={
                            "placeholder": "FILE_NAME"})
    submit = SubmitField("Download")


def valid_url(url):
    pattern = r'^https?://.*\.(jpg|jpeg|png|gif|JPG|JPEG|PNG|GIF)$'
    return re.match(pattern, url)


def download_image(url, file_name):
    r = requests.get(url)
    operating_system = get_os()
    if operating_system == "Linux":
        path = get_folder_path() + '/' + file_name + '.jpg'
    else:
        path = get_folder_path() + '\\' + file_name + '.jpg'
    with open(path, 'wb') as f:
        f.write(r.content)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ImageForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            if valid_url(form.url.data):
                download_image(form.url.data, form.file_name.data)
                flash("The image has been downloaded!")
            else:
                flash("The URL you provided is wrong!")
        return redirect(url_for('index'))

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)