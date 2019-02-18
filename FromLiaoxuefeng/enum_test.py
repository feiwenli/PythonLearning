# -*- coding=utf-8 -*-
from enum import Enum, unique

'''枚举类'''

Month = Enum('Month000', ('Jan', 'Feb'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
    # Jan => Month000.Jan , 1

# value属性时自动赋给成员的int常量，默认从1开始计数

# 检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 访问
print(Weekday.Sun)
print(Weekday['Tue'])
print(Weekday(1))


class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('test pass')
else:
    print('test fail')




