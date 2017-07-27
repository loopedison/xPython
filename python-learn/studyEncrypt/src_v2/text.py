#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################  
#  
# XXTEA encryption arithmetic library.  
#  
# Copyright (C) 2005-2008 loopedison <www.jishivr.cn>  
# Version: 2.0  
# LastModified: Oct 12, 2016 
# 

import os
import sys
import types
import ctypes
import time
import random
import struct

#==============================================================================
# Version
__author__ = "loopedison"
__version__ = "v2.0"

#==============================================================================
# load c/c++ dll
lib = ctypes.cdll.LoadLibrary("./xxtea.dll")
# # for test dll
# lib.HelloWorld()

# DEBUG
_DEBUG_EN = True

# KEYWORD
# WWW.JISHIVR.CN WITH MD5
_KEYWORD = [0XE9F78F0B,0X43F215FD,0X77E68673,0XD86C3B82]
_KEYWORDLEN = 4
# ENCRYPT ARRAY
_ENARRAY = 8
_FILEINFOSIZE = 8

#==============================================================================
#
## ==========================
# make keys
pKey = (ctypes.c_int * _KEYWORDLEN)()
for i in range(_KEYWORDLEN): pKey[i] = _KEYWORD[i]

fInfo = [0XFFFFFFFF for i in range(_FILEINFOSIZE)]
fInfo[0] = 0XAA010000
fInfo[1] = 956197601
fInfo[2] = 1109
print(fInfo)

pInfo = (ctypes.c_int * _FILEINFOSIZE)()
for i in range(_FILEINFOSIZE):
    pInfo[i] = fInfo[i]
lib.btea(pInfo, _FILEINFOSIZE, pKey)
for i in range(_FILEINFOSIZE):
    fInfo[i] = pInfo[i]
print(fInfo)

lib.btea(pInfo, -1*_FILEINFOSIZE, pKey)
for i in range(_FILEINFOSIZE):
    fInfo[i] = pInfo[i]
print(fInfo)

for i in range(_FILEINFOSIZE):
    pInfo[i] = fInfo[i]

lib.btea(pInfo, _FILEINFOSIZE, pKey)
for i in range(_FILEINFOSIZE):
    fInfo[i] = pInfo[i]
print(fInfo)

#==============================================================================
#
if __name__ == "__main__":  
    print('=================encrypt=================')
    pass

#
#==============================================================================
#