#!/usr/bin/python
#_*_ coding: utf-8 _*_

file = open("/sys/class/thermal/thermal_zone0/temp")
temp = float(file.read())/1000
file.close()
print "CPU temperature :%.1f" %temp

