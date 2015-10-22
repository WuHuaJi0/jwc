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
        loginResult = auth.login(session.get('__VIEWSTATE'),session.get('__EVENTVALIDATION'),session.get('headers'),username,password,CheckCode)


        if loginResult != 'yes':
            return render_template('login_error.html', loginError = loginResult)


        text = auth.getGrade(session['headers'],loginResult)
        return render_template('mask_detail.html',text = text)

    return render_template('mask.html',form=form,random=str(random.random()))


@app.route('/course',methods=['GET','POST'])
def course():
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
        loginResult = auth.login(session.get('__VIEWSTATE'),session.get('__EVENTVALIDATION'),session.get('headers'),username,password,CheckCode)

        if loginResult != 'yes':
            return render_template('login_error.html', loginError = loginResult)

        span = auth.warnning(session['headers'],loginResult)
        h3 = span.h3.string

        font = span.find('font')
        fontString = unicode(font)
        fontStringValue = fontString[18:63]

        stringspan = unicode(span)

        xuefen = stringspan[-23:-7]

        return render_template('warnningDetail.html',h3=h3,fontStringValue=fontStringValue, xuefen=xuefen)

    return render_template('course.html',form=form,random=str(random.random()))



@app.route('/about')
def about():
    return render_template('about.html')



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/test')
def test():
    pass


if __name__ == '__main__':
    app.run(debug=True)