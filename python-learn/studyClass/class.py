#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import types
from com.student import Student

# 数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。
print ('>>>====================================<<<')
jack = Student('Michael Jackson',90)
jack.print_self()

robert = Student('Robert Downey Jr',79)
robert.print_self()

# 强制访问内部数据，不推荐
# print (jack._Student__name)


# 继承与多态
print ('>>>====================================<<<')
# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)


# 获取对象信息
print ('>>>====================================<<<')
# 使用type()判断对象类型
# 适用于基本类型
# a实例 -> class类型 -> type类型
print (type(None))                  # 指向NoneType类型
print (type(('1','2',32,-5)))       # 指向tuple类型
print (type({'1':31, '2':32,}))     # 指向dict类型
print (type(abs))                   # 指向builtin_function_or_method类型
print (type(Student))               # 指向type类型
print (type(jack))                  # 指向Student类型

print (type(123) == int)
print (type('string') == str)
print (type(abs) == types.BuiltinFunctionType)

# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
print('jack is student ?', isinstance(jack, Student))


# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print ('>>>====================================<<<')
# print (dir('ABCD'))                 # 实例
print (dir(jack))                   # 实例
# print (dir(Dog))                    # 类型
# print (dir(types))                  # 
# print (dir(type))                   # 

print ('>>>====================================<<<')
# 配合 getattr()、setattr()以及 hasattr()，我们可以直接操作一个对象的状态
class TestObject(object):
    """docstring for TestObject"""
    def __init__(self, arg):
        super(TestObject, self).__init__()
        self.arg = arg
        
tobj = TestObject('test')
if hasattr(tobj, 'arg'):
    print ('has attr \'arg\' =', tobj.arg)
if hasattr(tobj, 'name'):
    print ('has attr \'name\' =',tobj.name)
else:
    setattr(tobj,'name','test_name')
    print ('create attr \'name\'=',getattr(tobj,'name'))

print ('>>>====================================<<<')
# 在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，
# 因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

