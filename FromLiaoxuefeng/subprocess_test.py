# -*- coding=utf-8 -*-
import subprocess

# 如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

# 当于在命令行执行命令nslookup
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
print('Exit code:', p.returncode)
