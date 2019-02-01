# -*- coding:utf-8 -*-
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3308/news_test?charset=utf8'
db = SQLAlchemy(app)

class News(db.Model):
	__tablename__ = 'new_news'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(20), nullable=False)
	content = db.Column(db.String(200), nullable=False)
	types = db.Column(db.String(20), nullable=False)
	images = db.Column(db.String(200), )
	atuthor = db.Column(db.String(10), )
	view_count = db.Column(db.Integer)
	create_at = db.Column(db.DateTime)
	is_valid = db.Column(db.Boolean)

	# def __repr__(self):
	# 	return '<News %r>' & self.title

app = Flask(__name__)

@app.route('/')
def index():
	# 新闻首页
	news_list = News.query.all()
	return render_template('index.html', news_list=news_list)

@app.route('/cat/<name>/')
def cat(name):
	# 新闻类别
	# 查询类别为name的新闻内容
	return render_template('cat.html', name = name)

@app.route('/detail/<int:pk>/')
def detail(pk):
	return render_template('detail.html', pk=pk)


if __name__ == '__main__':
	app.run(debug=True)