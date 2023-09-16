from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"

class ImageForm(FlaskForm):
    url = StringField(validators=[InputRequired()], render_kw={"placeholder": "URL"})
    file_name = StringField(validators=[InputRequired()], render_kw={"placeholder": "FILE_NAME"})
    submit = SubmitField("Download")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ImageForm()
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)