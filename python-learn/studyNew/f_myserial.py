#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'loop'

import serial
from time import sleep

serialPort = serial.Serial()
serialPort.port = 'com7'
serialPort.baudrate = 115200
serialPort.timeout = 1
serialPort.open()
sleep(1)
n=serialPort.inWaiting()
print('has data:%s' %(n))
print(serialPort.read(n))
serialPort.close()
