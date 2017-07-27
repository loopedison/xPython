#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from datetime import datetime, timedelta


## 注意到datetime是模块，datetime模块还包含一个datetime类，
## 通过from datetime import datetime导入的才是datetime这个类。
now = datetime.now()
print (now)
print (now+timedelta(days=5,hours=-1))
print (now.strftime('%a,%b,%d,%H:%M'))
print (datetime.fromtimestamp(1459489200.0))


## collections是Python内建的一个集合模块，提供了许多有用的集合类。

## namedtuple
## namedtuple是一个函数，它用来创建一个自定义的tuple对象，
## 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
from collections import namedtuple
Point = namedtuple('Point', ['x','y'])
pp = Point(12,13)
print (pp.x)
print (isinstance(pp,Point))
print (isinstance(pp,tuple))

## deque
## 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
## 因为list是线性存储，数据量大的时候，插入和删除效率很低。
## deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
## deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，
## 这样就可以非常高效地往头部添加或删除元素。
from collections import deque
qu = deque(['a','ab','ab12'])
print (qu)
qu.append('x0')
qu.appendleft('st')
print (qu)

## defaultdict
## 使用dict时，如果引用的Key不存在，就会抛出KeyError。
## 如果希望key不存在时，返回一个默认值，就可以用defaultdict：
## 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abcd'
print (dd['key1'])
print (dd['key2'])

## OrderedDict
## 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
## 如果要保持Key的顺序，可以用OrderedDict：
## OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
from collections import OrderedDict
dn = dict([('a', 1),('b', 2),('c', 3)])
print (dn)
do = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print (list(do))
do['z'] = 12
do['x'] = 13
do['y'] = 14
print (list(do.keys()))

## Counter
## Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
cc = Counter()
for ch in 'programming':
    cc[ch]=cc[ch]+1
    pass

print (cc)


import struct
k = struct.pack('>I',10123899)
print (k)


