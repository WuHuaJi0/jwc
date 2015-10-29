import mysql.connector
config={'host':'127.0.0.1',
        'user':'root',
        'password':'',
        'port':3306,
        'database':'test',
        'charset':'utf8'
        }
try:
  	cnn=mysql.connector.connect(**config)
    if cnn:
        print 'yes'
    else:
        print 'no'
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))

finally:
    print 'nihao'