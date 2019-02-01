# -*- coding=utf-8 -*-

import urllib2
import cookielib
import bs4

print bs4

url = "http://www.baidu.com"

print "the first method"
response1 = urllib2.urlopen(url)
print response1.getcode()   # 状态码,看看请求是否成功
print len(response1.read())

print "the second method"
request = urllib2.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print "the third method"
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(request)
print response3.getcode()
print cj
print response3.read()      # 打印网页内容
