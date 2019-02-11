# -*- coding=utf-8 -*-

'''闭包'''
def lazy_sum(*args):

    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f1 = lazy_sum(1,3,5,9)
f2 = lazy_sum(1,3,5,9)

print(f1 == f2)     # False
# f1() f2() 调用结果互不影响
# 返回的函数并没有立刻执行，而是直到调用了f1()才执行

def count():
    fs = []
    # 参数绑定循环变量里面的值
    def g(i):
        k = i
        return k*k
    for i in range(1,4):
        def f():
            return g(i)
        fs.append(f)
    return fs

'''利用闭包返回一个计数器函数，每次调用它返回递增整数'''

def counter():

    x = [0]
    print('闭包外--')
    def cc():
        print('闭包内--')
        x[0] = x[0] + 1
        return x[0]

    return cc

f1 = counter()
print(f1())


