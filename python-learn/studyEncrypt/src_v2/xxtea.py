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
        sData += b'\xff'
    for i in range(_ENARRAY-int(len(sData)//4)%_ENARRAY):
        sData += b'\xff\xff\xff\xff'
    # make buffer to store message
    msg = list(struct.unpack('<%ii' %(len(sData)//4), sData))
    if _DEBUG_EN: print('msg:\t%i\t%i\t%i' %(len(msg), msg[0], msg[-1]))
    
    ## ==========================
    # make keys
    pKey = (ctypes.c_int * _KEYWORDLEN)()
    for i in range(_KEYWORDLEN): pKey[i] = _KEYWORD[i]
    if _DEBUG_EN: print('pKey:\t%i\t%i\t%i' %(len(pKey), pKey[0], pKey[-1]))
    
    ## ==========================
    # make argv
    pMsg = (ctypes.c_int * _ENARRAY)()
    
    ## ==========================
    # encrypt
    for i in range(int(len(msg)//_ENARRAY)):
        for j in range(_ENARRAY):
            pMsg[j] = msg[i*_ENARRAY+j]
        lib.btea(pMsg, _ENARRAY, pKey)
        for j in range(_ENARRAY):
            msg[i*_ENARRAY+j] = pMsg[j]
    
    if _DEBUG_EN:
        print('msg_En:\t%i\t%i\t%i' %(len(msg), msg[0], msg[-1]))
        xmsg = msg[:]
        for i in range(int(len(xmsg)//_ENARRAY)):
            for j in range(_ENARRAY):
                pMsg[j] = xmsg[i*_ENARRAY+j]
            lib.btea(pMsg, -1*_ENARRAY, pKey)
            for j in range(_ENARRAY):
                xmsg[i*_ENARRAY+j] = pMsg[j]
        print('msg_De:\t%i\t%i\t%i' %(len(xmsg), xmsg[0], xmsg[-1]))
    
    
    ## ==========================
    # file info
    fInfo = [0XFFFFFFFF for i in range(_FILEINFOSIZE)]
    fInfo[0] = 0XAA000100
    fInfo[1] = int(len(msg))
    
    pInfo = (ctypes.c_int * _FILEINFOSIZE)()
    for i in range(_FILEINFOSIZE):
        pInfo[i] = fInfo[i]
    lib.btea(pInfo, _FILEINFOSIZE, pKey)
    for i in range(_FILEINFOSIZE):
        fInfo[i] = pInfo[i]
    
    ## ==========================
    # write file
    if _DEBUG_EN: print('fInfo:\t%i\t%i\t%i' %(len(fInfo), fInfo[0], fInfo[-1]))
    wInfo = struct.pack('<%ii' %(len(fInfo)), *fInfo)
    if _DEBUG_EN: print('wInfo:\t%i\t%i\t%i' %(len(wInfo), wInfo[0], wInfo[-1]))
    if _DEBUG_EN: print('msg_En:\t%i\t%i\t%i' %(len(msg), msg[0], msg[-1]))
    wData = struct.pack('<%ii' %(len(msg)), *msg)
    if _DEBUG_EN: print('wdata:\t%i\t%i\t%i' %(len(wData), wData[0], wData[-1]))
    with open(oFilePath,'wb') as oFile:
        oFile.write(wInfo)
        oFile.write(wData)
    
    ## ==========================
    return True
    
#==============================================================================
#
def decrypt(iFilePath, oFilePath):
    return False
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