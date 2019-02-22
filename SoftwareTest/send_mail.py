# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header 

# 发送邮箱服务器
smtpserver = 'smtp.163.com'
# 发送邮箱用户/密码
user = 'lfw_dar@163.com'
password = ''
#
sender = 'lfw_dar@163.com'
#
receiver = '2583637045@qq.com'
# 发送邮件主题
subject = 'Python email test'

# 编写HTML类型邮件正文
msg = MIMEText('<html><h1>您好！</h1></html>','html','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = Header(user)

# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
