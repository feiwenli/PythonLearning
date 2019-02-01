#!/usr/bin/env python3
#-*- coding = utf-8 -*-
#如何为元组中的每一个元素命名，提高可读性
#方案2
from collections import namedtuple
Student = namedtuple("student",['name','age','sex','email'])
s = Student('Jim',16,'male','jimeeee@gmail.com')
print(s)
print(s.name,s.age)
print(isinstance(s,tuple))