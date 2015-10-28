# -*- coding:utf-8 -*-
import requests
from StringIO import StringIO
import urllib
from bs4 import BeautifulSoup
from PIL import Image
import random

ctgu_request = requests.session()

def init():
    initHeaders = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Origin':'http://210.42.38.26:84',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Host':'210.42.38.26:84',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Upgrade-Insecure-Requests':1,
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    }

    url = "http://210.42.38.26:84/jwc_glxt/"
    r = requests.get(url)
    page = r.text

    cookie = str(r.cookies['ASP.NET_SessionId'])
    soup = BeautifulSoup(page)
    __VIEWSTATE = str(soup.find(attrs={'name':'__VIEWSTATE'})['value'])
    __EVENTVALIDATION = str(soup.find(attrs={'name':'__EVENTVALIDATION'})['value'])

    return (cookie,__VIEWSTATE,__EVENTVALIDATION)


def createHeaders(cookie):
    headers = {
        'Cookie':'ASP.NET_SessionId='+cookie,
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Origin':'http://210.42.38.26:84',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Cache-Control':'no-store',
        'Connection':'keep-alive',
        'Host':'210.42.38.26:84',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests':1,
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Referer': 'http://210.42.38.26:84/jwc_glxt/Login.aspx?xttc=1'
    }
    return headers

# 获取验证码
def getImage(headers):
    randomNum = random.randint(1,1000)
    url = "http://210.42.38.26:84/jwc_glxt/ValidateCode.aspx"
    r = ctgu_request.get(url,headers = headers)
    i = Image.open(StringIO(r.content)).save('static/img/code'+str(randomNum)+'.jpg')
    return randomNum


def login(__VIEWSTATE,__EVENTVALIDATION,headers,username,password,CheckCode):
    form = {
        '__VIEWSTATE':__VIEWSTATE,
        'txtUserName':username,
        'btnLogin.x': 0,
        'btnLogin.y': 0,
        'txtPassword':password,
        'CheckCode':CheckCode,
        '__EVENTVALIDATION':__EVENTVALIDATION
    }
    data = urllib.urlencode(form)
    login_url = "http://210.42.38.26:84/jwc_glxt/Login.aspx?xttc=1"
    result = ctgu_request.post(login_url,headers=headers,data=data)
    page = BeautifulSoup(result.text)
    lblMsg = page.find(attrs={'id':'lblMsg'})
    if hasattr(lblMsg,'string'):
        return lblMsg.string
    else:
        return 'yes'

# 获取成绩
def getGrade(headers,loginResult):
    if loginResult == 'yes':
        try:
            Grade_url = 'http://210.42.38.26:84/jwc_glxt/Student_Score/Score_Query.aspx'
            result  = ctgu_request.get(Grade_url,headers=headers)
            if result:
                soup = BeautifulSoup(result.text)
                tr_title = soup.find(attrs={'class':'HeaderStyle'})
                tr_chengji  = tr_title.find_next_siblings()
                return tr_chengji
            else:
                return 'error'
        except:
            return u"查询出错"
        finally:
            logOut(headers)
    else:
        return loginResult

# 获取总学分
def warnning(headers,loginResult):
    if loginResult == 'yes':
        try:
            warningUrl = 'http://210.42.38.26:84/jwc_glxt/Plan_To_Study/Study_Warnning.aspx'
            result  = ctgu_request.get(warningUrl,headers=headers)
            if result:
                soup = BeautifulSoup(result.text)

                span = soup.find(attrs={'id':'ctl00_MainContentPlaceHolder_Label1'})

                return span
            else:
                return 'error'
        except:
            return u"查询出错"
        finally:
            logOut(headers)
    else:
        return loginResult


# 培养计划
def trainPlan(headers,loginResult):
    if loginResult == 'yes':
        try:
            planUrl = 'http://210.42.38.26:84/jwc_glxt/Plan_Train/PlanTrain_Query.aspx'
            result  = ctgu_request.get(planUrl,headers=headers)
            if result:
                soup = BeautifulSoup(result.text)
                tr_title = soup.find(attrs={'class':'HeaderStyle'})
                plan = tr_title.find_next_siblings()
                return plan
            else:
                return 'error'
        except:
            return u"查询出错"
        finally:
            logOut(headers)
    else:
        return loginResult

# 学业对比：
def studyCompare(headers,loginResult):
    if loginResult == 'yes':
        try:
            planUrl = 'http://210.42.38.26:84/jwc_glxt/Plan_To_Study/PlanToStudy_Query.aspx'
            result  = ctgu_request.get(planUrl,headers=headers)
            if result:
                soup = BeautifulSoup(result.text)
                tr_title = soup.find(attrs={'class':'HeaderStyle'})
                plan = tr_title.find_next_siblings()
                return plan
            else:
                return 'error'
        except:
            return u"查询出错"
        finally:
            logOut(headers)
    else:
        return loginResult


def logOut(headers):
    logOut_url = 'http://210.42.38.26:84/jwc_glxt/Login.aspx?xttc=1'
    page = ctgu_request.get(logOut_url,headers=headers).text

