#!/usr/bin/python
#_*_ coding: utf-8 _*_

import RPi.GPIO as GPIO
import time

def blink(pin,cnt,*,freq=1):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin,GPIO.OUT)
	for x in range(1,cnt):
		GPIO.output(pin,GPIO.LOW)
		time.sleep(freq)
		GPIO.output(pin,GPIO.HIGH)
		time.sleep(freq)
		pass
	GPIO.cleanup()
	pass

if __name__ == '__main__':
	blink(40,20,freq=0.2)

