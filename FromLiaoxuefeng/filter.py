# -*- coding=utf-8 -*-

'''删掉偶数，保留奇数'''


def is_odd(num):
    return num % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, ])))

'''删除序列中的空字符串'''


def not_empty(s):
    return s and s.strip()  # 移除字符串头尾指定的字符（默认为空格或换行符）或字符序列


print(list(filter(not_empty, ['A', '', None, 'C D', ' M ', '   '])))

'''
求素数
埃氏算法
'''


# 1、构造一个奇数序列
def sequence():
    n = 1
    while True:
        n = n + 2
        yield n


# 2、定义一个筛选函数
def not_divisible(n):
    return lambda x: x % n > 0


# 3、定义一个生成器，不断返回下一个素数
def re_next():
    yield 2
    it = sequence()  # 初始化序列
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)  # 构造新序列



# 4、设置循环条件
print('以下为素数')
for n in re_next():
    if n < 20:
        print('n>',n)
    else:
        break


'''回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数'''


def is_round():
    return lambda x: str(x)[::]==str(x)[:: -1]


def sequence2():
    n = 1
    while True:
        n = n + 1
        yield n


def round():
    it = sequence2()
    yield 1
    while True:
        n = next(it)
        yield n
        it = filter(is_round(), it)


print('以下为回数：')
for n in round():
    if n < 20:
        print(n)
    else:
        break

