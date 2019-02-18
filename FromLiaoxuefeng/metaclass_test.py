# -*- coding=utf-8 -*-

'''先定义metaclass，就可以创建类，最后创建实例。'''


# metaclass是类的模板，所以必须从type类型派生



class ListMetaclass(type):
    '''
    接收参数：
    1、当前准备创建的类的对象；
    2、类的名字；
    3、类继承的父类集合；
    4、类的方法集合；
    '''

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
print(L)
