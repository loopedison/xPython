#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
from time import ctime

UdpSock=socket(AF_INET,SOCK_DGRAM)                          #参数SOCK_DGRAM对应的是UDP协议                    
UdpSock.bind(('127.0.0.1',9399))

while True:
    #与TCP的区别。因为不需要事先建立链接，因此需要获取客户端的地址，并随时按照地址发送消息
    data,addr=UdpSock.recvfrom(1024)
    #向客户端发送消息
    msg=('Data:['+data.decode('UTF-8')+'],'+'Addr:['+str(addr)+'],'+'Time:['+ctime()+']')
    UdpSock.sendto(msg.encode('UTF-8'),addr)
UdpSock.close()
