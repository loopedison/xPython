#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import types
import ctypes
import time
import random
import struct

#
def testFile():
    with open('temp.bin','wb') as oFile:
        allbytes=b'\50\51 1234abcdz'
        oFile.write(allbytes)
    with open('temp.bin','rb') as oFile:
        allbytes=oFile.read()
        print(allbytes)
    pass

#
#
if __name__ == "__main__":  
    print('=================encrypt=================')
    testFile()
    pass
