#-*- coding:utf-8 -*-
import MySQLdb

class MysqlSearch(object):
	def __init__(self):
		self.get_conn()

	def get_conn(self):
		# 建立连接
		try:
			self.conn = MySQLdb.connect(
				host='127.0.0.1',
				user='root',
				passwd='',
				port=3308,
				db='wangyinews',
				charset='utf8'
				)
		except MySQLdb.Error as e:
			print('Error:%s' % e)
		
	def close_conn(self):
		try:
			if self.conn:
				self.conn.close()
		except MySQLdb.Error as e:
			print('Error:%s',e)

	def get_one(self):
		# 准备SQL
		sql = "SELECT * FROM `news` WHERE `author`=%s ORDER BY `in_time` DESC;"
		# 找到cursor
		cursor = self.conn.cursor()
		# 执行SQL
		cursor.execute(sql,('LUCY',))
		#print(dir(cursor))
		#print(cursor.description)
		# 拿到结果
		# rest = cursor.fetchone()
		rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
		# 处理数据
		#for x in range(len(rest)):
		#	print rest[x]
		#print(rest['title'])
		# 关闭cursor/连接
		self.conn.close()
		return rest

	def get_more(self, page, page_size):
		# 准备sql
		offset = (page-1)*page_size
		print(offset)
		sql = "SELECT * FROM `news` WHERE `author`=%s ORDER BY `in_time` DESC LIMIT %s, %s;"
		# 找到cursor
		cursor = self.conn.cursor()
		# 执行SQL
		cursor.execute(sql,('JHON', offset, page_size))
		# 拿到结果
		rest = [dict(zip([k[0] for k in cursor.description],row)) 
			for row in cursor.fetchall()]
		return rest

	def add_one(self):
		# 准备SQL
		try:
			sql = (
				"INSERT INTO `news` (`title`, `content`, `tips`, `image`, `author`, `in_time`)" 
				"VALUE (%s, %s, %s, %s, %s, %s);"
				)

			# 提交数据到数据库
			cursor = self.conn.cursor()
			# 执行sql,提交数据到数据库
			cursor.execute(sql,('标题3','新闻内容3','polotical','/static/img/news/01.jpg','jack','2017-12-29 00:00:00'))
			cursor.execute(sql,('标题4','新闻内容4','polotical','/static/img/news/01.jpg','jack','2017-12-29 00:00:00','error'))
			cursor.execute(sql,('标题5','新闻内容5','polotical','/static/img/news/01.jpg','jack','2017-12-29 00:00:00'))

			# 提交事物
			self.conn.commit()
			# 关闭cursor和连接
			cursor.close()
		except :
			print('error')
			self.conn.rollback()	# 如果数据出现错误，则回滚，即一条都不成功
			# self.conn.commit()	# 如果数据出现错误，则只将出错数据之前的未出错数据传入
		self.close_conn() 
		

def main():
	obj = MysqlSearch()
	rest = obj.get_one()
	print(rest['title'])
	# rest = obj.get_more(2,1)
	# for item in rest:
	# 	print(item['title'])
	# obj.add_one()

if __name__ == '__main__':
	main()