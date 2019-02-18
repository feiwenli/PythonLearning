# -*- coding=utf-8 -*-

def fn(self, name='world'):
    print('Hello, %s.' % name)


# 用type()创建一个函数,以下为三个参数：
# 1、class的名称；
# 2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
h.hello()

