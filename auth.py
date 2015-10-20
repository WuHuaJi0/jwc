# -*- coding:utf-8 -*-
import requests
from StringIO import StringIO
import urllib
from bs4 import BeautifulSoup
from PIL import Image

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

    r = ctgu_request.get(url)
    page = r.text
    cookie = r.cookies['ASP.NET_SessionId']
    soup = BeautifulSoup(page)
    __VIEWSTATE = soup.find(attrs={'name':'__VIEWSTATE'})['value']
    __EVENTVALIDATION = soup.find(attrs={'name':'__EVENTVALIDATION'})['value']

    return (cookie,__VIEWSTATE,__EVENTVALIDATION)


def createHeaders(cookie):
    headers = {
        'Cookie':'ASP.NET_SessionId='+cookie,
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
        'Referer': 'http://210.42.38.26:84/jwc_glxt/Login.aspx?xttc=1'
    }
    return headers



def getImage(headers):
    url = "http://210.42.38.26:84/jwc_glxt/ValidateCode.aspx"
    r = ctgu_request.get(url,headers = headers)
    i = Image.open(StringIO(r.content)).save('static/img/code.jpg')


def login(__VIEWSTATE,__EVENTVALIDATION,headers,username,password,CheckCode):
    form = {
        '__VIEWSTATE':__VIEWSTATE,
        'txtUserName':username    ,
        'btnLogin.x': 0,
        'btnLogin.y': 0,
        'txtPassword':password,
        'CheckCode':CheckCode,
        '__EVENTVALIDATION':__EVENTVALIDATION
    }
    data = urllib.urlencode(form)
    login_url = "http://210.42.38.26:84/jwc_glxt/Login.aspx?xttc=1"
    result = ctgu_request.post(login_url,headers=headers,data=data)


def getGrade(headers):

    Grade_url = 'http://210.42.38.26:84/jwc_glxt/Student_Score/Score_Query.aspx'
    result  = ctgu_request.get(Grade_url,headers=headers)
    if result:
        soup = BeautifulSoup(result.text)
        tr_title = soup.find(attrs={'class':'HeaderStyle'})
        # print tr_title

        tr_chengji = tr_title.find_next_siblings()

        for child in tr_chengji[0].children:
            print child
    else:
        print 'error'

def logOut(headers):
    logOut_url = 'http://210.42.38.26:84/jwc_glxt/Login.aspx?xttc=1'
    page = ctgu_request.get(logOut_url,headers=headers).text


# def start():
#     (cookie,__VIEWSTATE,__EVENTVALIDATION) = init()
#     headers = createHeaders(cookie)
#     getImage(headers)
#     login(__VIEWSTATE,__EVENTVALIDATION,headers)
#     try:
#         getGrade(headers)
#     except:
#         pass
#     finally:
#         logOut(headers)

# if __name__ == '__main__':
#     (cookie,__VIEWSTATE,__EVENTVALIDATION) = init()
#     headers = createHeaders(cookie)
#     getImage(headers)