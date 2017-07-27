#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import types
import ctypes
import struct
import time
import datetime
import random
import tkinter
import tkinter.messagebox
import tkinter.filedialog
import _thread
import threading
import binascii
import logging

import xxtea

#==============================================================================
# Version
__author__ = "loop"
__version__ = "v2.0"

#==============================================================================
# 
class Application(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.grid(sticky="wesn")
        self.master.title('System Test')
        # app.master.geometry("400x300")
        self.master.resizable(width = False, height = False)
        self.master.iconbitmap('../ico/bitico.ico')
        self.createWidgets()
        self.initPrivateVar()
        self.after(10, _thread.start_new_thread, self.update, ())
        pass
        
        
    def createWidgets(self):
        #############################################
        # Create Frame_Menu, Frame_Main, Frame_Status
        self.frameMenu = tkinter.Frame(self)
        self.frameMenu.grid(row=0, column=0, sticky="wesn")
        self.frameMain = tkinter.Frame(self)
        self.frameMain.grid(row=1, column=0, sticky="wesn")
        self.frameStatus = tkinter.Frame(self)
        self.frameStatus.grid(row=2, column=0, sticky="wesn")
        
        
        #############################################
        # Create Frame_1,Frame_2 on Frame_Main
        self.frameLeft = tkinter.Frame(self.frameMain)
        self.frameLeft.grid(row=0, column=0, sticky="wesn")
        self.frameRight = tkinter.Frame(self.frameMain)
        self.frameRight.grid(row=0, column=1, sticky="wesn")
        
        
        #############################################
        # File Button
        self.fileButton = tkinter.Button(self.frameMenu, text='File', command=self.fileButtonCallBack, compound="left", bitmap="error", width=50)
        self.fileButton.grid(row=0, column=0, sticky="wesn")
        # Edit Button
        self.editButton = tkinter.Button(self.frameMenu, text='Edit', command=self.editButtonCallBack, compound="left", bitmap="error", width=50)
        self.editButton.grid(row=0, column=1, sticky="wesn")
        # Tool Button
        self.toolButton = tkinter.Button(self.frameMenu, text='Tool', command=self.toolButtonCallBack, compound="left", bitmap="error", width=50)
        self.toolButton.grid(row=0, column=2, sticky="wesn")
        # Help Button
        self.helpButton = tkinter.Button(self.frameMenu, text='Help', command=self.helpButtonCallBack, compound="left", bitmap="error", width=50)
        self.helpButton.grid(row=0, column=3, sticky="wesn")
        
        
        #############################################
        # Input File
        self.inFileViewLabel = tkinter.Label(self.frameLeft, text='Input:', width=10)
        self.inFileViewLabel.grid(row=0, column=0, sticky="w")
        self.inFileValueEntry = tkinter.Entry(self.frameLeft, width=30)
        self.inFileValueEntry.grid(row=0, column=1, sticky="wesn")
        
        # Output File
        self.outFileViewLabel = tkinter.Label(self.frameLeft, text='Output:', width=10)
        self.outFileViewLabel.grid(row=1, column=0, sticky="w")
        self.outFileValueEntry = tkinter.Entry(self.frameLeft, width=30)
        self.outFileValueEntry.grid(row=1, column=1, sticky="wesn")
        
        # choose input
        self.inFileButton = tkinter.Button(self.frameLeft, text='Choose', command=self.infileButtonCallBack)
        self.inFileButton.grid(row=0, column=2, sticky="wesn")
        
        # choose output
        self.outFileButton = tkinter.Button(self.frameLeft, text='Choose', command=self.outfileButtonCallBack)
        self.outFileButton.grid(row=1, column=2, sticky="wesn")
        
        # encryptButton
        self.encryptButton = tkinter.Button(self.frameLeft, text='encrypt', command=self.encryptButtonCallBack)
        self.encryptButton.grid(row=0, column=3, rowspan=2, columnspan=1, sticky="wesn")
        
        
        #############################################
        # Status
        self.statusValue = tkinter.StringVar()
        self.statusValue.set('[%s]' %('Ready'))
        self.statusValueLabel = tkinter.Label(self.frameStatus, textvariable=self.statusValue)
        self.statusValueLabel.grid(row=0, column=0,sticky="w")
        
        
    def initPrivateVar(self):
        # file
        self.inFilePath = None
        self.outFilePath = None
        
        pass
        
    def update(self):
        self.after(1000, _thread.start_new_thread, self.update, ())
        
    def fileButtonCallBack(self):
        tkinter.messagebox.showinfo('file', 'author:[%s], version:[%s]' %(__author__, __version__))
        pass
        
    def editButtonCallBack(self):
        tkinter.messagebox.showinfo('edit', 'author:[%s], version:[%s]' %(__author__, __version__))
        pass
        
    def toolButtonCallBack(self):
        tkinter.messagebox.showinfo('tool', 'author:[%s], version:[%s]' %(__author__, __version__))
        pass
        
    def helpButtonCallBack(self):
        tkinter.messagebox.showinfo('Helper', 'author:\t[%s]\nversion:\t[%s]\n' %(__author__, __version__))
        pass
        
    def infileButtonCallBack(self):
        tPath = tkinter.filedialog.askopenfilename(initialdir = self.inFileValueEntry.get())
        if tPath != '':
            self.inFilePath = tPath
            self.inFileValueEntry.insert(0, self.inFilePath)
            self.statusValue.set('[%s]' %('Choose inFile Success!'))
        else:
            self.statusValue.set('[%s]' %('Choose inFile Canceled!'))
        pass
    def outfileButtonCallBack(self):
        tPath = tkinter.filedialog.askopenfilename(initialdir = self.outFileValueEntry.get())
        if tPath != '':
            self.outFilePath = tPath
            self.outFileValueEntry.insert(0, self.outFilePath)
            self.statusValue.set('[%s]' %('Choose outFile Success!'))
        else:
            self.statusValue.set('[%s]' %('Choose outFile Canceled!'))
        pass
    def encryptButtonCallBack(self):
        if self.inFilePath != None and self.inFilePath != '' and self.outFilePath != None and self.outFilePath != '':
            xxtea.encrypt(self.inFilePath, self.outFilePath)
            self.statusValue.set('[%s]' %('encrypt inFile => outFile Success!'))
        else:
            self.statusValue.set('[%s]' %('File Failed!'))
        pass
#

# Main
if __name__=="__main__":
    root = tkinter.Tk()
    app = Application(master=root)
    app.mainloop()
#
#==============================================================================
#