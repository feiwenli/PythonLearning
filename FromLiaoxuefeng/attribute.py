# -*- coding=utf-8 -*-

class Student:

    '''类属性'''
    count = 0

    '''限制实例的属性'''
    # __slots__ = ('age', 'score', 'name')

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

'''动态绑定实例属性'''
s = Student('Lucy')
print('实例属性count：',s.count) # 3
s.count = 999
print('实例属性count：',s.count)  # 999,实例属性的优先级比类属性的优先级高，所以会屏蔽掉类属性count
print('类属性count：',Student.count)    # 3,类属性任然存在

# 删除实例属性
del s.count
print('实例属性count：',s.count) # 3

