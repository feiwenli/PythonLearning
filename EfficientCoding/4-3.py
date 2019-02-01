#如何调整字符串的格式
#2016-05-25 ==> 05/23/2016
import re

log = open('test.log').read()
print(re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log))
print('-'*60)
print(re.sub('(\d{2}):(\d{2}):(\d{2})','time that you can\'t see',log))
print('-'*60) 
print( re.sub("(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})","\g<month>/\g<day>/\g<year>",log ))
#大写的P！！！！！！