# coding=utf-8
from xml.dom import minidom

# 打开xml文件
dom = minidom.parse('info.xml')

# 得到文档元素对象
root = dom.documentElement

print root.nodeName		# info
print root.nodeValue	# None
print root.nodeType		# 1
print root.ELEMENT_NODE	# 1

# 获取任意标签名
tagname = root.getElementsByTagName('browser')
print tagname[0].tagName 

tagname = root.getElementsByTagName('login')
print tagname[1].tagName 

tagname = root.getElementsByTagName('province')
print tagname[2].tagName 

# 获取标签属性值
logins = root.getElementsByTagName('login')

# 获取login标签的username属性值
username = logins[0].getAttribute("username")
print username

# 获取login标签的password属性值
password = logins[0].getAttribute("password")
print password


# 获取第二个标签的username属性值
username = logins[1].getAttribute("username")
print username

# 获取标签对之间的数据
provinces = dom.getElementsByTagName("province")
citys = dom.getElementsByTagName("city")

# 获取第二个province标签对的值
p2 = provinces[1].firstChild.data
print p2

c1 = citys[0].firstChild.data
print c1
