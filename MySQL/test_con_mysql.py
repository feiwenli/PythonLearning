#-*- coding:utf-8 -*-
import MySQLdb
# 建立连接
try:
	conn = MySQLdb.connect(
		host='127.0.0.1',
		user='root',
		passwd='',
		port=3308,
		db='wangyinews',
		charset='utf8'
		)
except MySQLdb.Error as e:
	print('Error:%s' % e)
# 获取数据

cursor = conn.cursor()
cursor.execute('SELECT * FROM `news` WHERE 1;')
rest = cursor.fetchone()
print(rest)

# 关闭连接
conn.close()
''''''