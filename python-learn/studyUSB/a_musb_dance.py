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

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print(dir(usb))
print('==============================')
print(dir(usb.core))
print('==============================')
print(dir(usb.util))
print('==============================')
# print(usb.core.show_devices())
# exit()
for printer in usb.core.find(find_all=True):#, bDeviceClass=7
    print (printer)
# exit()

print('##############################')
# dev =  usb.core.find(idVendor= 0x0483, idProduct= 0x5740)
dev =  usb.core.find(idVendor= 0x2563, idProduct= 0x0568)
print(type(dev))
print(dev)
# exit()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(dev[0][(0,0)][0])     #endpoint
# ep0 = dev[0][(0,0)][0].bEndpointAddress
# size0 = dev[0][(0,0)][0].wMaxPacketSize
# exit()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# Find active configuration, and interface
activeConfig = dev.get_active_configuration()
activeInterface = activeConfig[(0,0)]

print('>>>>>Write OUT endpoint')
# Match the first OUT endpoint
ep_out = usb.util.find_descriptor(
    activeInterface,
    custom_match = lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT
)

# Write test data to device
if ep_out != None :
    wdata='WANTFORGETTXT'
    dev.write(ep_out, wdata)
    print('Success to write :', wdata)
    # Or
    wdata = array.array('B', [0x01,0x02,0x03,0x04])
    dev.write(ep_out, wdata)
    print('Success to write :', wdata)

# time.sleep(0.1)
# exit()

print('>>>>>Read IN endpoint')
# Match the first IN endpoint
ep_in = usb.util.find_descriptor(
    activeInterface,
    custom_match = lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_IN
)

# Read test data from device
if ep_in != None :
    counter = 0
    while counter < 1000:
        time.sleep(0.01)
        counter += 1
        data = ep_in.read(4)
        datalist = data.tolist()
        print(datalist)

##

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('end')
