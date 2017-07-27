#!/usr/bin/env python
# -*- coding: utf-8 -*-


print ('==============================')
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print (L[0][0])
print (L[-1][-1])
print (L[1][3])
print ('==============================')
for i in L:
    print (i)

print ('==============================')
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print (d)
print(d['Michael'])
if 'Thomas' in d:
    print (d[Thomas])
else:
    print ('!!!!!!!!!!!!')
d.pop('Michael')
for i in d:
    print (i,'=',d[i])
c = {'John':'2000p','Michael_0':'uiii',}
d.update(c)
d['John']=1000
print (d)


print ('==============================')
s1 =set([1,1,2,2,3,3])
print(s1)
s2 =set([2,3,4])
print(s1 & s2)
print(s1 | s2)


# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:
print ('==============================')
age = int(input('Input your age: '))
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# 函数调用
print ('==============================')
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print('2^2=', power (2))
print('2^3=', power(2,3))

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print ('2->5=', calc([2,3,4,5]))
print ('2->4=', calc((2,3,4)))

def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print ('2+3+4+5=', calc2(2,3,4,5))

#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1,2,3,4]
print ('nums=', calc2(*nums))

#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    if 'city' in kw:    # 有city参数
        print ('have city')
        pass
    if 'job' in kw:     # 有job参数
        print ('have job')
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person ('Michael', 12, city=None, home='America')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])


#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
#由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。
def person2(name, age, *, city, job='IT-Engineer'):
    print(name, age, city, job)
#person2('Jack', 24, 'Beijing', 'Engineer')
person2('Jack', 24, job='Engineer', city='Beijing')
person2('John', 100, city='Beijing')

# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用，除了可变参数无法和命名关键字参数混合。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。

print ('==============================')
def fun1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def fun2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

fun1 (1,2)
fun1 (1,2,3)
fun1 (1,2,3,'a','b','c')
fun1 (1,2,3,'a','b','c',x=99,y='loop')
fun2 (1,2,d='3009',ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
fun1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
fun2(*args, **kw)

#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。



print ('==============================')
sL=[x*2+1 for x in range(50)]
print (sL)

# 取一个list或tuple的部分元素是非常常见的操作。
print ('==============================')
sl=list(range(1,100,2))
print (sl)
print (sl[0:5]);    # 取前5个值
print (sl[:10]);    # 取前10个，起始=0可以不写
print (sl[-3:]);    # 取末尾3个
print (sl[::5]);    # 每5个取1个
print (sl[:]);      # 全部
# tuple也是一种list，唯一区别是tuple不可变。
# 因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print ((0,1,2,3,4,5,6)[:3]);    # 取tuple的前3个

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
# 因此，字符串也可以用切片操作，只是操作结果仍是字符串
print ('ABCDEFG'[-3:])

# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
print ('==============================')

# Python的for循环抽象程度要高于Java的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
ad={'d':21,'b':22,'c':23,'a':24}
for nn in ad:
    print ('[',nn,']','=',ad[nn])
for k,v in ad.items():
    print ('<',k,'>=<',v,'>')


# 字符串也是可迭代对象
for nn in 'AbCdEfGhIjKl':
    print (nn)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
from collections import Iterable
print (isinstance('qwertyuiop',Iterable))

ak = ['qwe','qw','e','1',234]
for i,value in enumerate(ak):
    print (i,value)

# 列表生成式
print ([x*x for x in range(1,20,2)])

# 两层循环
print ([m + n for m in 'ABC' for n in 'XYZ'])

import os
print ([d for d in os.listdir('.')])

pl = ['Hello','World','Apple']
print ([s.lower() for s in pl])

print ('==============================')
# 所以，如果列表元素可以按照某种算法推算出来，
# 那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
Ls = [x * x for x in range(10)]
Gs = (x * x for x in range(10))
for n in Gs:
    print (n)

# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

fb = fib(5);
print ('>>>>>>>')
print (fb)
# 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def oood ():
    print ('step1')
    yield (1)
    print ('step2')
    yield (3)
    print ('step3')
    yield (5)

od = oood()
print (next(od))
print (next(od))
print (next(od))
# print (next(od))


print ('==============================')
def triangles():
    L = []
    while True:
        L.append(1)
        temp = L[:]
        for i,value in enumerate(temp):
            if i!=0 and i!=len(temp)-1:
                L[i] = temp[i-1]+temp[i]
        yield L
ii = 0
for nn in triangles():
    print (nn)
    ii = ii+1
    if ii>10:
        break

# 迭代器
print ('==============================')
# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否是Iterable对象
from collections import Iterable
from collections import Iterator
print ('[]==>', isinstance([], Iterable))
print ('{}==>', isinstance({}, Iterable))
print ('abcde==>', isinstance('abcde', Iterable))
print ('xforx==>', isinstance((s for x in range(10)), Iterable))
print ('10==>', isinstance(10, Iterable))

print ('[]=..=>', isinstance([], Iterator))
print ('{}=..=>', isinstance({}, Iterator))
print ('abcde=..=>', isinstance('abcde', Iterator))
print ('xforx=..=>', isinstance((s for x in range(10)), Iterator))
print ('10=..=>', isinstance(10, Iterator))

