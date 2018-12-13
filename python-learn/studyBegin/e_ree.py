#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

## 由于Python的字符串本身也用\转义，强烈建议使用Python的r前缀，就不用考虑转义的问题了
s1 = 'ABC\\-001'
s2 = r'ABC\-002'
print ("s1:"+s1+'\n'+"s2:"+s2)

## 在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符
## 正则表达式匹配字符串
print (re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print (re.match(r'^\d{3}\-\d{3,8}$', '010 - 12345'))
print (re.match(r'^\d{3}\-\d{3,8}$', s2))

## 正则表达式切割字符串
print (re.split(r'\s+', 'a ab bin ,  c'))
print (re.split(r'[\s\,\;]+', 'a ab, bin;  ;;  c'))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print (m.groups())

## 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。
## 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
## 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
print (re.match(r'^(\d+)(0*)$', '102300').groups())
print (re.match(r'^(\d+?)(0*)$', '102300').groups())

addr1 = 'someone@gmail.com'
print (re.match(r'\w+@\w+.\w+', addr1))