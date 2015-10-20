#encoding:utf-8
from flask import Flask,render_template,request,url_for,redirect,session
from flask.ext.bootstrap import Bootstrap
import requests
import auth
import pdb
import urllib

# 导入表单
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField,PasswordField
# from wtforms.fields.simple import StringField,SubmitField,PasswordField
from wtforms.validators import Required
# from wtforms.ext.i18n.form import Form
from StringIO import StringIO


app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'HELLO'



class UserForm(Form):
    txtUserName = StringField(u'输入学号', validators=[Required()])
    txtUserPassword = PasswordField(u'输入密码', validators=[Required()])
    CheckCode = StringField(u'输入验证码',validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mask',methods=['GET','POST'])
def mask():
    form = UserForm()
    if request.method == 'GET':
        if not session['flag']:
            (cookie,__VIEWSTATE,__EVENTVALIDATION) = auth.init()
            headers = auth.createHeaders(cookie)
            auth.getImage(headers)
            session['flag'] = True
            return __VIEWSTATE

    # if form.validate_on_submit():
    #     username = form.txtUserName.data
    #     password = form.txtUserPassword.data
    #     CheckCode = form.CheckCode.data
    #     return __VIEWSTATE
        # auth.login(__VIEWSTATE,__EVENTVALIDATION,headers,username,password,CheckCode)
        # auth.getGrade(headers)
        # return redirect(url_for('mask'))

    return render_template('mask.html',form=form,__VIEWSTATE=__VIEWSTATE)


@app.route('/test')
def test():
    return request.method

@app.route('/course')
def course():
    return render_template('course.html')

@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)