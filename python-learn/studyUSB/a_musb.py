#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
基本的通信可以
设备chid，0483 5750
'''

import usb.core
import usb.util
import sys
import time
import array

print('*************************************************')
print(dir(usb))
print('')
print(dir(usb.core))
print('')
print(dir(usb.util))
print('')
print('*************************************************')
dev =  usb.core.find(idVendor= 0x0483, idProduct= 0x5750)
print(type(dev))
print(dev)
# exit()
ep3 = dev[0][(0,0)][0].bEndpointAddress
size3 = dev[0][(0,0)][0].wMaxPacketSize
print('>>',ep3,size3)
ep3 = dev[0][(0,0)][1].bEndpointAddress
size3 = dev[0][(0,0)][1].wMaxPacketSize
print('>>',ep3,size3)

print('*************************************************')
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]
ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT
)
wdata='WANTFORGETTXT'
print ('The length of data(write USB) is:', wdata)
dev.write(ep,wdata)

sendlist=[0x01,0x02,0x03,0x04]
wdata = array.array('B',sendlist)
dev.write(ep,wdata)

time.sleep(0.1)
# exit()
print('*************************************************')
ep_read = usb.util.find_descriptor(
    intf,
    # match the first IN endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_IN
)
data = ep_read.read(4)
datalist = data.tolist()
print(data)
print(datalist)
# usb.core.close()
# dev.reset()

print('*************************************************')
