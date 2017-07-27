#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################  
#  
# XXTEA encryption arithmetic library.  
#  
# Copyright (C) 2005-2008 loopedison <www.jishivr.cn>  
# Version: 1.1  
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
__version__ = "v1.1"

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
_ENARRAY = 4

#==============================================================================
#
def encrypt(iFilePath, oFilePath):
    ## ==========================
    with open(iFilePath,'rb') as iFile:
        # read file
        rData = iFile.read()
    ## ==========================
    # 
    if _DEBUG_EN: print('rdata:\t%i\t%i\t%i' %(len(rData), rData[0], rData[-1]))
    ## ==========================
    # resize data
    sData = rData
    for i in range((4-(len(rData)&0x3))&0x3):
        sData += b'\0'
    
    # make buffer to store message
    msg = list(struct.unpack('<%ii' %(len(sData)//4), sData))
    if _DEBUG_EN: print('msg:\t%i\t%i\t%i' %(len(msg), msg[0], msg[-1]))
    
    ## ==========================
    # make keys
    pKey = (ctypes.c_int * _KEYWORDLEN)()
    for i in range(_KEYWORDLEN): pKey[i] = _KEYWORD[i]
    
    ## ==========================
    # make argv
    pMsg = (ctypes.c_int * _ENARRAY)()
    
    ## ==========================
    # encrypt
    for i in range(_ENARRAY-1):
        pMsg[0+i] = msg[len(msg)-_ENARRAY+1+i]
    for i in range(len(msg)-_ENARRAY+1):
        for j in range(_ENARRAY-1): pMsg[_ENARRAY-1-j] = pMsg[_ENARRAY-2-j]
        pMsg[0] = msg[len(msg)-_ENARRAY-i]
        lib.btea(pMsg, _ENARRAY, pKey)
        msg[len(msg)-1-i] = pMsg[_ENARRAY-1]
    for i in range(_ENARRAY-1):
        msg[i] = pMsg[i]
    
    ## ==========================
    # write file
    wData = struct.pack('<%ii' %(len(msg)), *msg)
    if _DEBUG_EN: print('wdata:\t%i\t%i\t%i' %(len(wData), wData[0], wData[-1]))
    with open(oFilePath,'wb') as oFile:
        oFile.write(wData)
    
    ## ==========================
    return True
    
#==============================================================================
#
def decrypt(iFilePath, oFilePath):
    ## ==========================
    with open(iFilePath,'rb') as iFile:
        # read file
        rData = iFile.read()
    ## ==========================
    # 
    if _DEBUG_EN: print('rdata:\t%i\t%i\t%i' %(len(rData), rData[0], rData[-1]))
    ## ==========================
    # resize data
    sData = rData
    for i in range((4-(len(rData)&0x3))&0x3):
        sData += b'\0'
    
    # make buffer to store message
    msg = list(struct.unpack('<%ii' %(len(sData)//4), sData))
    if _DEBUG_EN: print('msg:\t%i\t%i\t%i' %(len(msg), msg[0], msg[-1]))
    
    ## ==========================
    # make keys
    pKey = (ctypes.c_int * _KEYWORDLEN)()
    for i in range(_KEYWORDLEN): pKey[i] = _KEYWORD[i]
    
    ## ==========================
    # make argv
    pMsg = (ctypes.c_int * _ENARRAY)()
    
    ## ==========================
    # decrypt
    for i in range(_ENARRAY-1):
        pMsg[1+i] = msg[0+i]
    for i in range(len(msg)-_ENARRAY+1):
        for j in range(_ENARRAY-1): pMsg[0+j] = pMsg[1+j]
        pMsg[_ENARRAY-1] = msg[_ENARRAY-1+i]
        lib.btea(pMsg, -1*_ENARRAY, pKey)
        msg[i] = pMsg[0]
    for i in range(_ENARRAY-1):
        msg[len(msg)-_ENARRAY+1+i] = pMsg[1+i]
    
    ## ==========================
    # write file
    wData = struct.pack('<%ii' %(len(msg)), *msg)
    if _DEBUG_EN: print('wdata:\t%i\t%i\t%i' %(len(wData), wData[0], wData[-1]))
    with open(oFilePath,'wb') as oFile:
        oFile.write(wData)
    
    ## ==========================
    return True

#==============================================================================
#
def compare(iFilePath_1, iFilePath_2):
    with open(iFilePath_1, 'rb') as file1, open(iFilePath_2, 'rb') as file2:
        cnt = 0
        aa = file1.read()
        bb = file2.read()
        for i in range(min(len(aa),len(bb))):
            if aa[i] != bb[i]:
                cnt += 1
        print(cnt)
        return(cnt)
#

#==============================================================================
#
if __name__ == "__main__":  
    print('=================encrypt=================')
    encrypt('vehicle.bin', 'vehicle_encrypt.bin')
    print('=================decrypt=================')
    decrypt('vehicle_encrypt.bin', 'vehicle_decrypt.bin')
    print('=================finished================')
    compare('vehicle.bin','vehicle_decrypt.bin')
    pass

#
#==============================================================================
#