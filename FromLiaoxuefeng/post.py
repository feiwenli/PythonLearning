# -*- coding:utf8 -*-
import urllib
import urllib.request
url = "http://xapi.kybyun.com/user/login"
headers = {}
headers = {
	'Host':'xapi.kybyun.com',
	'Connection':'keep-alive',
	'KY-SCHID':'1044'
}
data = {}
data['appchg']='AppStore'
data['apptype']='21'
data['appver']='2.1.3.1'
data['email']='mushishi01'
data['isbind']='0'
data['passwd']='111111'
data['sysdev']='iPhone 6 Plus'
data['sysver']='9.3'
data['uuid']='6ff7563dbd47c8077905c3920bc0d8b3'
#数据编码及赋值
data = urllib.parse.urlencode(data)
req = urllib.request.Request(url,data,headers)
urllib.request.urlopen(req)
#打开地址并且赋值给变量
responceStr = urllib.request.urlopen(req)
#读取获得的值
responceStr = responceStr.read()
#将获得的结果进行转码
responceStr = responceStr.decode("unicode_escape")
#打印
print(responceStr)