#json模块的dumps()和loads()函数是定义得非常好的接口的典范
import json

class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score

def student2dict(std):
	return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob',20,88)
print(json.dumps(s,default = student2dict))
#把任意class的实例变为dict
print(json.dumps(s,default = lambda obj : obj.__dict__))

#把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
#然后，我们传入的object_hook函数负责把dict转换为Student实例

def dict2student(d):
		return Student(d['name'],d['age'],d['score'])

json_str = '{"age":20 ,"score":88,"name":"Alice"}'
print(json.loads(json_str,object_hook = dict2student))