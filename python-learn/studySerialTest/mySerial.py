#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading
import serial
import logging

__author__ = "loopedison"
__version__ = "v0.1"

# ==============================================================================
class Application(object):
    def __init__(self):
        # serial config
        self.serial = serial.Serial()
        self.serial.port = 'COM6'
        self.serial.baudrate = '9600'
        self.serial.parity = 'N'
        self.serial.bytesize = 8
        self.serial.stopbits = 1
        self.serial.timeout = 2
        # server thread
        self.storageServerThread = threading.Thread(target=self.StorageServerHandle)
        self.storageServerThread.setDaemon(True)
        self.storageServerThread.start()
        pass
    
    def StorageServerHandle(self):
        while True:
            time.sleep(0.001)
            if self.serial.isOpen():
                n = self.serial.inWaiting()
                if n != 0:
                    tmpData = self.serial.read(n)
                    print('recv{'+tmpData.decode('utf-8')+'}')
            pass
        pass
    
    def Run(self):
        while True:
            print('============================================================')
            print('!open    ==> open '+self.serial.port)
            print('!close   ==> close serial')
            print('!quit    ==> exit')
            print('message  ==> send [message] to COM')
            self.inputCmd = input('> ')
            print('==============================')
            if self.inputCmd != '':
                if self.inputCmd[0] == '!':
                    if self.inputCmd[1:].upper() == 'OPEN':
                        print('open ... ', end='')
                        try:
                            if not self.serial.isOpen():
                                self.serial.open()
                                print('ok')
                        except Exception as e:
                            logging.error(e)
                    elif self.inputCmd[1:].upper() == 'CLOSE':
                        print('close ... ', end='')
                        try:
                            if self.serial.isOpen():
                                self.serial.close()
                                print('ok')
                        except Exception as e:
                            logging.error(e)
                    if self.inputCmd[1:].upper() == 'QUIT':
                        print('quit ...')
                        break
                else:
                    if self.serial.isOpen():
                        print('sending ['+self.inputCmd+']')
                        self.serial.write(self.inputCmd.encode('utf-8'))
                    else:
                        print('please open COM')
            pass
        pass

##
if __name__=="__main__":
    app=Application()
    app.Run()
