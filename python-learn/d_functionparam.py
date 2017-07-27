#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,urllib,time,platform

def blink(PIN,dtime):
    for x in range(1,dtime):
        print (PIN,x)
        pass
    pass

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

def xfun():
    pass

# if __name__=='__main__':
#     blink(10,9)

