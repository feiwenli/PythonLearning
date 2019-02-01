# -*- coding:utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:@localhost:3308/news_test?charset=utf8', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
# 在还没有engine时
# Session = sessionmaker()
# 等有engine只后
# Session.configure(bind=engine)

class News(Base):
	__tablename__ = 'news'

	id = Column(Integer, primary_key=True)
	title = Column(String(20), nullable=False)
	content = Column(String(200), nullable=False)
	types = Column(String(20), nullable=False)
	images = Column(String(200), )
	atuthor = Column(String(10), )
	view_count = Column(Integer)
	create_at = Column(DateTime)
	is_valid = Column(Boolean)

class OrmTest(object):

	def __init__(self):
		self.session = Session()

	def add_one(self):

		new_obj = News(
			title='title',
			content='content',
			types='1',
			)
		self.session.add(new_obj)

		self.session.commit()
		return new_obj

	def add_more(self):
		self.session.add_all([
		    News(title='aaa', content='aaaaaaaaaa',types='a'),
	     	News(title='bbb', content='bbbbbbbbbb',types='b'),
	     	News(title='ccc', content='cccccccccc',types='c')])
		self.session.commit()

	def get_one(self):
		# 查询一条数据
		return self.session.query(News).get(1)

	def get_more(self):
		return self.session.query(News).filter_by(is_valid=True)

	def update_data(self, pk):
		# 修改多条数据
		data_list = self.session.query(News).filter_by(is_valid=True)
		for item in data_list:
			item.is_valid = 0
			self.session.add(item)
		self.session.commit()
		# 修改单条数据
		# new_obj = self.session.query(News).get(pk)
		# if new_obj:
		# 	new_obj.is_valid = 0
		# 	self.session.add(new_obj)
		# 	self.session.commit()
		# 	return True
		# return False

	def delete_data(self, pk):
		new_obj = self.session.query(News).get(pk)
		self.session.delete(new_obj)
		self.session.commit()

def main():
	obj = OrmTest()
	# rest = obj.add_one()
	# print(rest.id)
	# 
	# obj.add_more()
	# 
	# rest = obj.get_one()
	# if rest:
	# 	print('ID:{0}=>{1}'.format(rest.id, rest.title))
	# else:
	# 	print('Not exit.')
	# 	
	# rests = obj.get_more()
	# if rests:
	# 	for rest in rests:
	# 		print('ID:{0}=>{1}'.format(rest.id, rest.title))
	# else:
	# 	print('Not exit.')
	# 	
	# print(obj.update_data(3))
	# 
	obj.delete_data(1)


if __name__=='__main__':
	main()

