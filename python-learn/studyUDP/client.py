#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
from time import ctime

addr = ('127.0.0.1',9399)    # 元祖形式
udpClient = socket(AF_INET,SOCK_DGRAM) #创建客户端

while True:
    data = input('>>>>> ')
    data = data.encode('UTF-8')
    udpClient.sendto(data,addr)             # 发送数据
    data,addr = udpClient.recvfrom(1024)    # 接收数据和返回地址
    print('\r\nRecv:\t',data.decode(encoding="utf-8"),'\r\nFrom:\t',addr)
udpClient.close()
