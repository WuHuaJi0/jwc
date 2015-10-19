#encoding:utf-8
from flask import Flask,render_template,request
from flask.ext.bootstrap import Bootstrap
# import auth

# 导入表单
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import Required


app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'HELLO'



class NameForm(Form):
    txtUserName = StringField('What is your name?', validators=[Required()])
    txtUserPassword = PasswordField('What is your password?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        username = form.txtUserName.data
        txtUserPassword = form.txtUserPassword.data

    return render_template('index.html', form=form)



@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)