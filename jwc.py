#encoding:utf-8
from flask import Flask,render_template,request
from flask.ext.bootstrap import Bootstrap
import requests
import auth

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
    CheckCode = StringField('checkcode',validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = NameForm()
    (cookie,__VIEWSTATE,__EVENTVALIDATION) = auth.init()
    headers = auth.createHeaders(cookie)
    auth.getImage(headers)
    if form.validate_on_submit():
        username = form.txtUserName.data
        password = form.txtUserPassword.data
        CheckCode = form.CheckCode.data
        # auth.login(__VIEWSTATE,__EVENTVALIDATION,headers,username,password,CheckCode)
        return cookie
    # ,headers,username,password,CheckCode,__VIEWSTATE,__EVENTVALIDATION
    return render_template('index.html', form=form)

@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)