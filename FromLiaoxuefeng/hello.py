# -*- coding:utf8 -*-
import urllib
import urllib.request
url = 'http://reg.haibian.com/login/ajax_login'
#定义请求数据，并且对数据进行赋值
data = {}
data['loginname']='student08@qq.com'
data['password']='96e79218965eb72c92a549dd5a330112'
#对请求数据进行编码
data = urllib.parse.urlencode(data)
#将数据和url进行连接
request=url+'?'+data
#打开请求，获取对象
requestResponce = urllib.request.urlopen(request)
#读取服务端返回的数据
responceStr = requestResponce.read()
#打印数据
responceStr = responceStr.decode('unicode_escape')
print(responceStr)