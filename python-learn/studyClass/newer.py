#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import types
import logging
from enum import Enum, unique

# 枚举类
# 每个常量都是class的一个唯一实例
print ('>>>====================================<<<')

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print (name, '=>', member, ',', member.value)

# 如需精确控制枚举类型，可以从Enum派生自定义类
# 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
@unique
class Week(Enum):
    """docstring for Week"""
    # def __init__(self, arg):
    #     super(Week, self).__init__()
    #     self.arg = arg
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6    

day_1 = Week.Mon
print (day_1)
print (Week.Mon)
print (Week['Mon'] == day_1)
print (Week(1) == day_1)
for name, member in Week.__members__.items():
    print (name, '=>', member)

print ('>>>====================================<<<')

# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
try:
    print ('try...')
    r = 10 / 0
    # r = 10 / 2
    print ('result:', r)
    print (type(r))
except ZeroDivisionError as e:
    print ('except:', e)
finally:
    print ('finally...')
print ('...END')

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。
# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
# 好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。
def foo(s):
    n = int(s)
    assert n!=0, 'n is zero'
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print ('Error:', e)
        # raise
        # bar('0')
        # logging.exception(e)
    finally:
        print ('finally')
main()

print ('...END')
# 如果断言失败，assert语句本身就会抛出AssertionError
# 程序中如果到处充斥着assert，和print()相比也好不到哪去。
# 不过，启动Python解释器时可以用-O参数来关闭assert
print ('>>>====================================<<<')

# 调试方法
# 方法1，就是用print()把可能有问题的变量打印出来看看
# 方法2，用断言（assert）来替代print
# 方法3，把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件
# 方法4，第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。
# 方法5，pdb.set_trace()内断点
# 方法6，高级的IDE断点调试
