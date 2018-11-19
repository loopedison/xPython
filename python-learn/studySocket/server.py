#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket

class NetServer(object):
  def tcpServer(self):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 9528))       # 绑定同一个域名下的所有机器
    sock.listen(5)
    
    while True:
        clientSock, (remoteHost, remotePort) = sock.accept()
        print("[%s:%s] connect" % (remoteHost, remotePort))     # 接收客户端的ip, port

        revcData = clientSock.recv(1024)
        sendDataLen = clientSock.send(("this is send  data from server").encode('utf-8'))
        print ("revcData: ", revcData)
        print ("sendDataLen: ", sendDataLen)

        clientSock.close()

if __name__ == "__main__":
  netServer = NetServer()
  netServer.tcpServer()
