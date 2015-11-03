#encoding:utf-8
from flask import Flask,render_template,request,url_for,redirect,session,make_response
from flask.ext.bootstrap import Bootstrap
import requests
import auth
from bs4 import BeautifulSoup
import pdb
import urllib
import random

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import Required

# import mysql



application = Flask(__name__)

bootstrap = Bootstrap(application)

application.config['SECRET_KEY'] = 'HELLO'

class UserForm(Form):
    txtUserName = StringField(u'输入学号', validators=[Required()])
    txtUserPassword = PasswordField(u'输入密码', validators=[Required()])
    CheckCode = StringField(u'输入该死的验证码',validators=[Required()])
    submit = SubmitField(u'查询')

@application.route('/')
def index():
    return render_template('index.html')

# 查询成绩
@application.route('/mask',methods=['GET','POST'])
def mask():
    form = UserForm()
    if request.method == 'GET':
        session['cookie'] = None
        session['__VIEWSTATE'] = None
        session['__EVENTVALIDATION'] = None
        session['headers'] = None
        session['randomNum'] = None

        (session['cookie'],session['__VIEWSTATE'],session['__EVENTVALIDATION']) = auth.init()
        session['headers'] = auth.createHeaders(session['cookie'])
        session['randomNum'] = auth.getImage(session['headers'])

    if form.validate_on_submit() and request.method == 'POST':
        username = form.txtUserName.data
        password = form.txtUserPassword.data
        CheckCode = form.CheckCode.data
        loginResult = auth.login(session.get('__VIEWSTATE'),session.get('__EVENTVALIDATION'),session.get('headers'),username,password,CheckCode)

        if loginResult != 'yes':
            return render_template('login_error.html', loginError = loginResult,before='mask')

        (tiaomu2012,tiaomu2013,tiaomu2014,tiaomu2015,userinfo) = auth.getGrade(session['headers'],loginResult)

        return render_template('mask_detail.html',tiaomu2012 = tiaomu2012,tiaomu2013 = tiaomu2013,tiaomu2014 = tiaomu2014,tiaomu2015 = tiaomu2015,userinfo=userinfo)

    return render_template('query.html',form=form,randomNum=str(session['randomNum']))


# 学业预警
@application.route('/course',methods=['GET','POST'])
def course():
    form = UserForm()
    if request.method == 'GET':
        session['cookie'] = None
        session['__VIEWSTATE'] = None
        session['__EVENTVALIDATION'] = None
        session['headers'] = None
        session['randomNum'] = None

        (session['cookie'],session['__VIEWSTATE'],session['__EVENTVALIDATION']) = auth.init()
        session['headers'] = auth.createHeaders(session['cookie'])
        session['randomNum'] = auth.getImage(session['headers'])

    if form.validate_on_submit() and request.method == 'POST':
        username = form.txtUserName.data
        password = form.txtUserPassword.data
        CheckCode = form.CheckCode.data
        loginResult = auth.login(session.get('__VIEWSTATE'),session.get('__EVENTVALIDATION'),session.get('headers'),username,password,CheckCode)

        if loginResult != 'yes':
            return render_template('login_error.html', loginError = loginResult,before='course')

        warnning = auth.warnning(session['headers'],loginResult)

        return render_template('warnningDetail.html',warnning=warnning)

    return render_template('query.html',form=form,randomNum=str(session['randomNum']))


# 培养计划
# @application.route('/planTrain',methods=['GET','POST'])
# def planTrain():
#     form = UserForm()
#     if request.method == 'GET':
#         session['cookie'] = None
#         session['__VIEWSTATE'] = None
#         session['__EVENTVALIDATION'] = None
#         session['headers'] = None
#         session['randomNum'] = None
#
#         (session['cookie'],session['__VIEWSTATE'],session['__EVENTVALIDATION']) = auth.init()
#         session['headers'] = auth.createHeaders(session['cookie'])
#         session['randomNum'] = auth.getImage(session['headers'])
#
#     if form.validate_on_submit() and request.method == 'POST':
#         username = form.txtUserName.data
#         password = form.txtUserPassword.data
#         CheckCode = form.CheckCode.data
#         loginResult = auth.login(session.get('__VIEWSTATE'),session.get('__EVENTVALIDATION'),session.get('headers'),username,password,CheckCode)
#
#         if loginResult != 'yes':
#             return render_template('login_error.html', loginError = loginResult,before='course')
#
#         plan = auth.trainPlan(session['headers'],loginResult)
#
#         return render_template('planTrain.html',plan = plan)
#     # return render_template('query.html',form=form,randomNum=str(session['randomNum']))


@application.route('/studyCompare',methods=['GET','POST'])
def studyCompare():
    form = UserForm()
    if request.method == 'GET':
        session['cookie'] = None
        session['__VIEWSTATE'] = None
        session['__EVENTVALIDATION'] = None
        session['headers'] = None
        session['randomNum'] = None

        (session['cookie'],session['__VIEWSTATE'],session['__EVENTVALIDATION']) = auth.init()
        session['headers'] = auth.createHeaders(session['cookie'])
        session['randomNum'] = auth.getImage(session['headers'])

    if form.validate_on_submit() and request.method == 'POST':
        username = form.txtUserName.data
        password = form.txtUserPassword.data
        CheckCode = form.CheckCode.data
        loginResult = auth.login(session.get('__VIEWSTATE'),session.get('__EVENTVALIDATION'),session.get('headers'),username,password,CheckCode)

        if loginResult != 'yes':
            return render_template('login_error.html', loginError = loginResult,before='course')

        plan = auth.studyCompare(session['headers'],loginResult)

        return render_template('studyCompare.html',plan = plan)

    return render_template('query.html',form=form,randomNum=str(session['randomNum']))


@application.route('/chat',methods=['GET','POST'])
def chat():
    if request.method == 'POST':
        content = request.form.get('content')
        people = request.form.get('people')
        return people
    return render_template('chat.html')


@application.route('/about')
def about():
    return render_template('about.html')

@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@application.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    application.run(debug=True)