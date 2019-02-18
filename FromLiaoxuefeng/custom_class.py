# -*- coding=utf-8 -*-

'''定制类'''


class Teacher:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'teacher\'s name is %s' % self.name


print(Teacher('Leon'))

'''把类变成迭代对象'''


class Fib:
    def __init__(self):
        self.a, self.b = 0, 1

    # 返回迭代对象
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a


for x in Fib():
    print(x)

'''实现List相似功能'''


class Fib2:
    # 可通过下标访问元素
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        # n是切片
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f2 = Fib2()
print(f2[23])
print(f2[1:13])

'''动态返回一个属性'''


class Chain(object):
    '''动态返回URL'''

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        if path == 'user':
            return lambda x: Chain('%s/%s' % (self._path, x))
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.users.timeline.list)  # /status/user/timeline/list

print(Chain().users.user('Jone').kk)  # /users/Jone/kk

'''直接对实例进行调用'''


class TestCallable(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s' % self.name)


t = TestCallable('Mac')
t() # My name is Mac
