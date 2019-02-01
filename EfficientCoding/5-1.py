# coding=utf-8
# py2
# 读取文本文件
f = open('history.txt','w')
s = u'你好'
f.write(s.encode('gbk'))
f.close()
f = open('history.txt','r')
t = f.read()
print t.decode('gbk')
