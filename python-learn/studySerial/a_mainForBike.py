#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
串口使用助手
'''

import tkinter
import tkinter.messagebox
import time
import datetime
import random
import _thread
import threading
import serial
import serial.tools.list_ports
import binascii
import ctypes
import logging

'''
版本更新情况

'''
__author__ = "loop"
__version__ = "v1.0"

##
class Application(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.grid(sticky="wesn")
        self.master.title('System Test')
        # app.master.geometry("400x300")
        self.master.resizable(width = False, height = False)
        self.master.iconbitmap('./ico/bitico.ico')
        self.createWidgets()
        self.after(10, _thread.start_new_thread, self.update, ())
        pass
        
    def createWidgets(self):
        #############################################
        # Create Frame_1,Frame_2
        self.frameMenu = tkinter.Frame(self)
        self.frameMenu.grid(row=0, column=0, sticky="wesn")
        self.frameMain = tkinter.Frame(self)
        self.frameMain.grid(row=1, column=0, sticky="wesn")
        self.frameStatus = tkinter.Frame(self)
        self.frameStatus.grid(row=2, column=0, sticky="wesn")
        
        
        #############################################
        # Create Frame_1,Frame_2
        self.frameLeft = tkinter.Frame(self.frameMain)
        self.frameLeft.grid(row=0, column=0, sticky="wesn")
        self.frameRight = tkinter.Frame(self.frameMain)
        self.frameRight.grid(row=0, column=1, sticky="wesn")
        
        
        #############################################
        # File Button
        self.fileButton = tkinter.Button(self.frameMenu, text='File', command=self.fileButtonFunction, compound="left", bitmap="error", width=50)
        self.fileButton.grid(row=0, column=0, sticky="wesn")
        # Edit Button
        self.editButton = tkinter.Button(self.frameMenu, text='Edit', command=self.editButtonFunction, compound="left", bitmap="error", width=50)
        self.editButton.grid(row=0, column=1, sticky="wesn")
        # Help Button
        self.helpButton = tkinter.Button(self.frameMenu, text='Help', command=self.helpButtonFunction, compound="left", bitmap="error", width=50)
        self.helpButton.grid(row=0, column=2, sticky="wesn")
        
        
        #############################################
        # port
        self.portViewLabel = tkinter.Label(self.frameLeft, text='Port:', width=10)
        self.portViewLabel.grid(row=0, column=0, sticky="w")
        self.portValueEntry = tkinter.Entry(self.frameLeft, width=10)
        self.portValueEntry.insert(0,'COM5')
        self.portValueEntry.grid(row=0, column=1, sticky="wesn")
        
        # baudrate
        self.baudrateViewLabel = tkinter.Label(self.frameLeft, text='Baudrate:', width=10)
        self.baudrateViewLabel.grid(row=1, column=0, sticky="w")
        self.baudrateValueEntry = tkinter.Entry(self.frameLeft, width=10)
        self.baudrateValueEntry.insert(0,'115200')
        self.baudrateValueEntry.grid(row=1, column=1, sticky="wesn")
        
        # parity
        self.parityViewLabel = tkinter.Label(self.frameLeft, text='Parity:', width=10)
        self.parityViewLabel.grid(row=2, column=0, sticky="w")
        self.parityValueEntry = tkinter.Entry(self.frameLeft, width=10)
        self.parityValueEntry.insert(0,'N')
        self.parityValueEntry.grid(row=2, column=1, sticky="wesn")
        
        # bytesize
        self.bytesizeViewLabel = tkinter.Label(self.frameLeft, text='Bytesize:', width=10)
        self.bytesizeViewLabel.grid(row=3, column=0, sticky="w")
        self.bytesizeValueEntry = tkinter.Entry(self.frameLeft, width=10)
        self.bytesizeValueEntry.insert(0,'8')
        self.bytesizeValueEntry.grid(row=3, column=1, sticky="wesn")
        
        # stopbits
        self.stopbitsViewLabel = tkinter.Label(self.frameLeft, text='Stopbits:', width=10)
        self.stopbitsViewLabel.grid(row=4, column=0, sticky="w")
        self.stopbitsValueEntry = tkinter.Entry(self.frameLeft, width=10)
        self.stopbitsValueEntry.insert(0,'1')
        self.stopbitsValueEntry.grid(row=4, column=1, sticky="wesn")
        
        # ctrlSerialButton
        self.ctrlSerialButton = tkinter.Button(self.frameLeft, text='Open', bg='Green', command=self.strlSerialFunction)
        self.ctrlSerialButton.grid(row=5, column=0, rowspan=1, columnspan=3, sticky="wesn")
        
        #############################################
        # receive data
        self.receiveViewLabel = tkinter.Label(self.frameRight, text='Receive:', width=10)
        self.receiveViewLabel.grid(row=1, column=0, sticky="w")
        self.receiveValue = tkinter.StringVar()
        self.receiveValueLabel = tkinter.Label(self.frameRight, fg='Blue', bg='Gray', textvariable=self.receiveValue,width=30)
        self.receiveValueLabel.grid(row=1, column=1, sticky="w")
        
        # Angle.X
        self.angleXViewLabel = tkinter.Label(self.frameRight, text='Angle.X:', width=10)
        self.angleXViewLabel.grid(row=2, column=0, sticky="w")
        self.angleXValue = tkinter.StringVar()
        self.angleXValueLabel = tkinter.Label(self.frameRight, fg='Blue', bg='Gray', textvariable=self.angleXValue,width=30)
        self.angleXValueLabel.grid(row=2, column=1, sticky="w")
        
        # Angle.Y
        self.angleYViewLabel = tkinter.Label(self.frameRight, text='Angle.Y:', width=10)
        self.angleYViewLabel.grid(row=3, column=0, sticky="w")
        self.angleYValue = tkinter.StringVar()
        self.angleYValueLabel = tkinter.Label(self.frameRight, fg='Blue', bg='Gray', textvariable=self.angleYValue,width=30)
        self.angleYValueLabel.grid(row=3, column=1, sticky="w")
        
        # Angle.Z
        self.angleZViewLabel = tkinter.Label(self.frameRight, text='Angle.Z:', width=10)
        self.angleZViewLabel.grid(row=4, column=0, sticky="w")
        self.angleZValue = tkinter.StringVar()
        self.angleZValueLabel = tkinter.Label(self.frameRight, fg='Blue', bg='Gray', textvariable=self.angleZValue,width=30)
        self.angleZValueLabel.grid(row=4, column=1, sticky="w")
        
        
        #############################################
        # Timestamp
        self.timeValue = tkinter.StringVar()
        self.timeValueLabel = tkinter.Label(self.frameStatus, textvariable=self.timeValue,width=20)
        self.timeValueLabel.grid(row=0, column=0, sticky="wesn")
        
        # Status
        self.statusValue = tkinter.StringVar()
        self.statusValueLabel = tkinter.Label(self.frameStatus, textvariable=self.statusValue)
        self.statusValueLabel.grid(row=0, column=1, columnspan=2, sticky="wesn")
        
        
        pass
        
    def update(self):
        # Recode
        self.timeNow = time.time()
        self.timeLast = time.time()
        
        # Serial
        self.serialStatus = False
        self.serialData = b''
        self.updateSerialThread = None
        self.serial = None
        
        
        while True:
            time.sleep(0.02)
            # Timestamp
            self.timeValue.set('[%s]' %(time.strftime("%Y-%m-%d %H:%M:%S")))
            self.statusValue.set(':[%s]' %'success')
            
            pass
        pass
        
    def fileButtonFunction(self):
        tkinter.messagebox.showinfo('file', 'author:[%s], version:[%s]' %(__author__, __version__))
        pass
        
    def editButtonFunction(self):
        tkinter.messagebox.showinfo('edit', 'author:[%s], version:[%s]' %(__author__, __version__))
        pass
        
    def helpButtonFunction(self):
        tkinter.messagebox.showinfo('Helper', 'author:[%s], version:[%s]' %(__author__, __version__))
        pass
        
    def strlSerialFunction(self):
        if self.ctrlSerialButton['text'] == 'Open':
            # get serial port setting
            self.serial = serial.Serial()
            self.serial.port = self.portValueEntry.get()
            self.serial.baudrate = self.baudrateValueEntry.get()
            self.serial.parity = self.parityValueEntry.get()
            self.serial.bytesize = int(self.bytesizeValueEntry.get())
            self.serial.stopbits = int(self.stopbitsValueEntry.get())
            self.serial.timeout = 2
            #
            # print(self.serial.port)
            # print(self.serial.baudrate)
            # open serial port
            try:
                self.serial.open()
                if self.serial.isOpen():
                    self.serialStatus = True
            except Exception as e:
                self.serialStatus = False
                logging.error(e)
            #
            # print(self.serial)
            # print(self.serialStatus)
            if self.serialStatus == True:
                # start receive thread
                self.updateSerialThread = threading.Thread(target=self.updateSerial)
                self.updateSerialThread.setDaemon(True)
                self.updateSerialThread.start()
                # configure button
                self.ctrlSerialButton.configure(bg='Red')
                self.ctrlSerialButton.configure(text='Close')
                pass
            pass
        else:
            try:
                self.serialStatus = False
                self.updateSerialThread.join()
                if self.serial.isOpen():
                    self.serial.close()
            except Exception as e:
                logging.error(e)
            # configure button
            self.ctrlSerialButton.configure(bg='Green')
            self.ctrlSerialButton.configure(text='Open')
            pass
        pass
        
    def updateSerial(self):
        while self.serialStatus == True:
            time.sleep(0.001)
            n = self.serial.inWaiting()
            if n >= 10:
                self.serialData = self.serial.read(1)
                if self.serialData[0] != 0x10:
                    continue
                self.serialData += self.serial.read(1)
                self.serialData += self.serial.read(1)
                if self.serialData[2] != 0x05:
                    continue
                
                # Datas
                self.serialData += self.serial.read(7)
                # self.serial.write(self.serialData)
                
                # Decode
                vbyte=binascii.b2a_hex(self.serialData[4:2:-1])
                value=int(bytes(vbyte).decode('ascii'), 16)
                self.angleValueX=ctypes.c_int16(value).value
                
                vbyte=binascii.b2a_hex(self.serialData[6:4:-1])
                value=int(bytes(vbyte).decode('ascii'), 16)
                self.angleValueY=ctypes.c_int16(value).value
                
                vbyte=binascii.b2a_hex(self.serialData[7:6:-1])
                value=int(bytes(vbyte).decode('ascii'), 16)
                self.angleValueZ=ctypes.c_int16(value).value
                
                # Display
                xdata = binascii.b2a_hex(self.serialData)
                self.receiveValue.set(bytes(xdata).decode('ascii').upper())
                value=self.angleValueX
                self.angleXValue.set("%.2f" %value)
                value=self.angleValueY
                self.angleYValue.set("%.2f" %value)
                value=self.angleValueZ
                self.angleZValue.set("%.2f" %value)
            pass
        pass
        
##
class mSerial:
    def set(self,port,baudrate):
        pass
##


def mainTest():
    root = tkinter.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__=="__main__":
    mainTest();

###########################################################

