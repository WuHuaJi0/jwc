from flask import Flask,render_template

from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required,Length

app = Flask(__name__)

app.config['SECRET_KEY'] = 'HELLO'


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)