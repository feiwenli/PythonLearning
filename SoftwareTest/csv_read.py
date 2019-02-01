# coding=utf-8
import csv

# 读取本地csv文件
date = csv.reader(open('info.csv','r'))

for user in date:
	print user[1]
