#encoding:utf-8
from flask import Flask,render_template,request,url_for,redirect,session,make_response
from flask.ext.bootstrap import Bootstrap
import requests
import auth
from bs4 import BeautifulSoup
import pdb
import urllib
import random
# 导入表单
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import Required
from StringIO import StringIO

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'HELLO'

class UserForm(Form):
    txtUserName = StringField(u'输入学号', validators=[Required()])
    txtUserPassword = PasswordField(u'输入密码', validators=[Required()])
    CheckCode = StringField(u'输入那个蠢蠢的验证码',validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mask',methods=['GET','POST'])
def mask():
    form = UserForm()
    if request.method == 'GET':
        session['cookie'] = None
        session['__VIEWSTATE'] = None
        session['__EVENTVALIDATION'] = None
        session['headers'] = None
        (session['cookie'],session['__VIEWSTATE'],session['__EVENTVALIDATION']) = auth.init()
        session['headers'] = auth.createHeaders(session['cookie'])
        auth.getImage(session['headers'])

    if form.validate_on_submit() and request.method == 'POST':
        username = form.txtUserName.data
        password = form.txtUserPassword.data
        CheckCode = form.CheckCode.data
        # return session['cookie']
        loginResult = auth.login(session.get('__VIEWSTATE'),session.get('__EVENTVALIDATION'),session.get('headers'),username,password,CheckCode)


        if loginResult != 'yes':
            return render_template('login_error.html', loginError = loginResult)


        text = auth.getGrade(session['headers'],loginResult)
        return render_template('mask_detail.html',text = text)

    return render_template('mask.html',form=form,random=str(random.random()))


@app.route('/test')
def test():
    pass

@app.route('/course')
def course():
    return render_template('course.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)