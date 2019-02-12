# -*- coding=utf-8 -*-
from functools import reduce

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


'''将str转化为int'''
class strToInt:
    def __init__(self, s):
        self.s = s

    def fn(self, x, y):
        return x * 10 + y

    def char2num(self, single):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[single]

    def get(self):
        return reduce(self.fn, map(self.char2num, self.s))

    # 用lambda函数简化
    def get2(self):
        return reduce(lambda x, y: x * 10 + y, map(self.char2num, self.s))

i = strToInt('1563').get()
print(i)
j = strToInt('48626').get2()
print(j)

'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']
输出：['Adam', 'Lisa', 'Bart']
'''
def name(n):
    return n.title()


print(list(map(name, ['adam', 'LISA', 'barT'])))

print(list(map(lambda x: x.title(), ['adam', 'LISA', 'barT'])))

'''接受一个list并利用reduce()求积'''
def prod(lis):
    return reduce(lambda x, y: x*y , lis)

print(prod([1,2,1,2,3]))

'''利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456'''
class str2float:
    def __init__(self, s):
        self.lis = s.split('.')

    def _char2num(self, single):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[single]

    def _getF(self):
        return reduce(lambda x,y : 10*x+y, map(self._char2num, self.lis[0]))

    def _getE(self):
        return reduce(lambda x,y : 0.1*x+y, map(self._char2num, self.lis[1][::-1]))*0.1

    def get(self):
        return self._getF()+self._getE()


str2float('123.4567').get()

