# -*- coding=utf-8 -*-

'''多态'''
class Animal:

    def run(self):
        print('Animal is running ...')


class Cat(Animal):

    def run(self):
        print('Cat is running ...')


class Dog(Animal):

    def run(self):
        print('Dog is running ...')

'''
对动态语言来说，不一定需要传入Animal类型，只需要保证传入的对象有一个run()方法就可以了
对静态语言来说，传入的对象必须是Animal类型或者它的子类
'''
class Timer(object):

    def run(self):
        print('Timer is running ...')

def run_polymorphism(Animal):
    Animal.run()


run_polymorphism(Dog())
run_polymorphism(Cat())
run_polymorphism(Timer())