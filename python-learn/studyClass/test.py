#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import types

# 数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。
print ('>>>====================================<<<')
class Classmates(object):
    """docstring for Classmates"""
    def __init__(self, arg):
        super(Classmates, self).__init__()
        self.arg = arg

Tom = Classmates(1)
print (dir(Tom))
print ('>>>===============<<<')

# 给实例添加 room 属性
# 类的其他实例无效
Tom.room = 102
print ('Add attr : room:', Tom.room)

# 给实例添加 set_age 方法
# 类的其他实例无效
from types import MethodType
def set_age(self, age):
    self.age = age
Tom.set_age = MethodType(set_age, Tom)

Tom.set_age(25)
print ('Add func: ',Tom.age)

print ('>>>===============<<<')
print (dir(Tom))


print ('>>>====================================<<<')
# 给类添加 set_id 方法
# 类的所有实例有效
def set_id(self, id):
    self.id = id
Classmates.set_id = MethodType(set_id, Classmates)

s1 = Classmates(1)
s2 = Classmates(2)
s1.set_id(1001)
print (Classmates.id)
s2.set_id(1002)
print (Classmates.id)

print ('>>>====================================<<<')
# 使用 __slots__ 限制实例的属性
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class phone(object):
    """docstring for phone"""
    __slots__ = ('id', 'name')
    def __init__(self, id):
        super(phone, self).__init__()
        self.id = id
class iphone(phone):
    """docstring for iphone"""
    pass

ph = phone(1)
# setattr(ph, 'age', 12)
iph = iphone(2)
setattr(iph, 'age', 12)

print ('__slots__')


# 使用@property限制属性参数的读写
print ('>>>====================================<<<')

class Student(object):
    # 限制性写
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # 限制性写
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # 只读属性
    @property
    def age(self):
        return 2015 - self._birth

st1 = Student()
st1.score = 60
st1.birth = 1990
print ('score =', st1.score)
print ('age =',st1.age)
# ValueError: score must between 0 ~ 100!
#st1.score = 9999

print ('>>>====================================<<<')
# 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现。
# 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass



