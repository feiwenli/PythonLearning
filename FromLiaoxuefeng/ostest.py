import os
print(os.name)	#操作系统类型
#print(os.environ)	#环境变量
print(os.path.abspath('.'))	#查看当前目录的绝对路径
os.path.join('E:\\core\\python\\liao','test_dir')	#创建一个目录
os.mkdir('E:\\core\\python\\liao\\test_dir')
os.rmdir('E:\\core\\python\\liao\\test_dir')
print(os.path.split(r'E:\core\python\liao'))
print(os.path.splitext(r'E:\core\python\liao'))	#直接得到文件的扩展名
t = [x for x in os.listdir('.') if os.path.isdir(x)]
print(t)
p = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(p)