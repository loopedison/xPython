#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from math import sqrt
import functools
from functools import reduce


# 函数式编程
print ('==============================')
# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

def adds(x, y, f):
    return f(x) + f(y)
print (adds(5,6,abs))

def same(x,*fs):
    s=[f(x) for f in fs]
    return s
print(same(2,sqrt,abs))

# Python内建了map()和reduce()函数。
print ('==============================')
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def fun(x):
    return pow(x,3)
print (list(map(fun, (1,2,3,4,5,5))))
print (list(map(str, [12,0,-5,-0.001])))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，效果如下
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def func(x,y):
    return (x*10 + y)
print (reduce(func,[1,2,3,4,5]))

def char2num(s):
    return ({'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s])

def str2int(s):
    return (reduce(lambda x,y: x*10+y, map(char2num,s)))

sst = '567890'
print (sst, '==>>', str2int(sst))


def normalize(name):
    return (name[0].upper()+name[1:].lower())
sL1 = ['aDd','LIsa','APPLE','n']
sL2 = list(map(normalize,sL1))
print (sL1,'=>>=',sL2)

def prod(x,y):
    return(x*y)
sT1 = [2,4,6,8,10]
sT2 = reduce(prod,sT1)
print (sT1,'=>>=',sT2)

def mults(x):
    return (pow(x,3))
def pows(l):
    return (sum(map(mults,l)))
sR1 = [1,2,3,4,5,6,7,8,9]
sR2 = pows(sR1)
print (sR1,'=>>=',sR2)


print ('==============================')
def str2float(s):
    ss = s.split('.')                     
    return int(ss[0])+int(ss[1])/ (10 ** (len(s) - s.find(".") - 1))
print (str2float('56789.1278'))

# 幂函数 x**n ==>> x^n
print ('8^3','=>>=',8**3)

# Python内建的filter()函数用于过滤序列
print ('==============================')
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def isodd(n):
    return (n%2 == 1)
sE1 = [1,2,4,5,-5,0]
sE2 = list(filter(isodd,sE1))
print (sE1,'=>>=',sE2)

def isempty(s):
    return (s and s.strip())
sW1 = ['A','',None,'  ','    *']
sW2 = list(filter(isempty,sW1))
print (sW1,'=>>=',sW2)

# 生成器，3开始的奇数
def _odd_iterm():
    n = 1
    while True:
        n = n+2
        yield n

def _not_divisible(n):
    return (lambda x: x%n>0)

def primes():
    yield 2
    it = _odd_iterm()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

for n in primes():
    if n < 50:
        print(n)
    else:
        break

# 排序算法，Python内置的sorted()函数
print ('==============================')
# 无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
print (sorted([9,12,53,-9,3,-50]))
print (sorted([9,12,53,-9,3,-50],key=abs))

print (sorted(['bob','Apple','12','-9','Pool','girl']))
print (sorted(['bob','Apple','12','-9','Pool','girl'],key=str.lower,reverse=True))

# 一组tuple表示学生名字和成绩
sTu = [('Boob',67),('Apple',98),('Jessie',45),('Tom',99)]
def by_name(t):
    return (t[0])
def by_score(t):
    return (t[1])
sTu1 = sorted(sTu,key=by_name)
sTu2 = sorted(sTu,key=by_score,reverse=True)
print (sTu1)
print (sTu2)

# operator.itemgetter函数可以实现多维排序
from operator import itemgetter
sTu3 = sorted(sTu,key=itemgetter(0),reverse=True)
print (sTu3)

def itemg(args):
    return lambda x: x[args]



# 函数作为返回值
print ('==============================')
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print (f1(),f2(),f3())


# 匿名函数
# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
print ('==============================')
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
# lambda x: x * x  等效于
# def f(x):
#     return x * x

print (list(map(lambda x: pow(x,4), [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# 装饰器Decorator
print ('==============================')

def log(fc):
    @functools.wraps(fc)
    def wrapper(*args, **kw):
        print('call %s():' % fc.__name__)
        return fc(*args, **kw)
    return wrapper
@log
def fc(s):
    print (s)

fc('Transylvania')


# 偏函数 partial
print ('==============================')
# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int_2 = functools.partial(int,base=2)
print (int_2('10001010'))

max_2 = functools.partial(max,10)
print (max_2(3,5))
# 实际是把10这个参数作为*args的一部分，自动添加到最左端，效果等效于
# args = (10,3,5)
# max(*args)


