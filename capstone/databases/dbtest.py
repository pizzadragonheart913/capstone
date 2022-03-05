import pymysql

conn = pymysql.connect(host = 'localhost', user = 'root', password='101010',db='encore', charset='utf8')

cur = conn.cursor()
