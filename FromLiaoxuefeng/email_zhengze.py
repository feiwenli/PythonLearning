#正则表达式验证邮箱的正确性
import re

email = 'some.one@163.com'
is_email = re.compile(r'^([0-9a-zA-Z]+|[0-9a-zA-Z]+.[0-9a-zA-Z]+)@(gmail|microsoft|163|139)+.com$')
if is_email.match(email):
	print('your email is right. the name is',is_email.match(email).group(1))
else :
	print("there is something wrong with the email you typed yet")

m = re.match(r'(\d{3})-(\d{3,8})','010-123456')
print(m.group(2))