#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module implementing MainClient.
"""

#===============================================================================
import sys
import json
import socket
import time
import threading
import operator

from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QAction, QMenu, QMessageBox
from PyQt5.QtGui import *

from Ui_client import Ui_Dialog

#===============================================================================
class MainClient(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainClient, self).__init__(parent)
        self.setupUi(self)
        self.mainSetup()
    
    def mainSetup(self):
        # running counter
        self.gRunStatus = 0
        # commander list
        self.gRunEnv = {'curGameIndex':'0'}
        self.gCmdList = []
        
        # config toolButton_More
        self.toolButtonMenu = QMenu(self)
        self.shutdowAction = QAction(QIcon('image/shutdown.ico'), 'Shutdown', self)
        self.restartAction = QAction(QIcon('image/restart.ico'),'Restart', self)
        self.AboutAction = QAction(QIcon('image/Star.ico'),'About help', self)
        self.toolButtonMenu.addAction(self.shutdowAction)
        self.toolButtonMenu.addAction(self.restartAction)
        self.toolButtonMenu.addSeparator()
        self.toolButtonMenu.addAction(self.AboutAction)
        self.toolButton_More.setMenu(self.toolButtonMenu)
        self.shutdowAction.triggered.connect(self.on_toolButton_clicked)
        self.restartAction.triggered.connect(self.on_toolButton_clicked)
        self.AboutAction.triggered.connect(self.on_toolButton_clicked)
        
        # load configurations from "config.json"
        self.gConfDict = {}
        with open('config\config.json', 'r+', encoding='utf-8') as confList:
            self.gConfDict = json.load(confList)
        self.gGameList = self.gConfDict['GAMELIST']
        
        # configure combobox
        for game in self.gGameList:
            self.comboBox_List.addItem(game['GameName'])
        
        # Create update timer
        self.updateLoop = QTimer(self)
        self.updateLoop.timeout.connect(self.clientTimerHandle)
        self.updateLoop.start(100)
        
        # Create dictionary
        self.gServerDict = {}
        for xIndex, xServer in enumerate(self.gConfDict['SERVERLIST']):
            self.gServerDict[xServer['ServerName']] = {'Status':'Offline', 'Socket':[]}
            self.listWidget_Links.addItem('%s |%s:%s' %(str(xIndex), xServer['ServerName'].ljust(8, ' '), xServer['ServerIP']))
            self.listWidget_Links.item(xIndex).setBackground(QColor('lightgrey'))
        
        # starting
        self.gRunStatus = 1
        
        # Create TCP client Thread
        self.clientThread = threading.Thread(target=self.clientThreadHandle)
        self.clientThread.setDaemon(True)
        self.clientThread.start()
    
    def clientTimerHandle(self):
        # command handle
        if len(self.gCmdList) > 0:
            newCmd = self.gCmdList.pop(0)
            for xIndex, xServer in enumerate(self.gConfDict['SERVERLIST']):
                if operator.eq(self.gServerDict[xServer['ServerName']]['Status'], 'Online'):
                    # if Online
                    try :
                        # send to server
                        self.gServerDict[xServer['ServerName']]['Socket'].settimeout(5)
                        self.gServerDict[xServer['ServerName']]['Socket'].send(json.dumps(newCmd).encode('utf-8'))
                        self.listWidget_Links.item(xIndex).setText(self.listWidget_Links.item(xIndex).text()[:25]+' | '+newCmd['Option'])
                    except socket.error :
                        # disconnnected
                        self.gServerDict[xServer['ServerName']]['Socket'].close()
                        self.gServerDict[xServer['ServerName']]['Status'] = 'Offline'
                        self.gServerDict[xServer['ServerName']]['Socket'] = []
                    except :
                        pass
                    pass
                pass
            pass
        
        # update
        for xIndex, xServer in enumerate(self.gConfDict['SERVERLIST']):
            if operator.eq(self.gServerDict[xServer['ServerName']]['Status'], 'Online'):
                self.listWidget_Links.item(xIndex).setBackground(QColor('lime'))
            else:
                self.listWidget_Links.item(xIndex).setBackground(QColor('lightgrey'))
        
        pass
    
    def clientThreadHandle(self):
        # Scan servers
        while self.gRunStatus > 0:
            for xIndex, xServer in enumerate(self.gConfDict['SERVERLIST']):
                if operator.eq(self.gServerDict[xServer['ServerName']]['Status'], 'Online'):
                    # if Online
                    try :
                        self.gServerDict[xServer['ServerName']]['Socket'].settimeout(5)
                        self.gServerDict[xServer['ServerName']]['Socket'].send(' '.encode('utf-8')) 
                    except socket.error :
                        print(xServer['ServerName']+' offline!')
                        self.gServerDict[xServer['ServerName']]['Socket'].close()
                        self.gServerDict[xServer['ServerName']]['Status'] = 'Offline'
                        self.gServerDict[xServer['ServerName']]['Socket'] = []
                    except :
                        pass
                    pass
                else:
                    # if Offline
                    try:
                        xSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        xSocket.settimeout(2)
                        xSocket.connect((xServer['ServerIP'], int(self.gConfDict['ServerPort'])))
                        print(xServer['ServerName']+' online!')
                        self.gServerDict[xServer['ServerName']]['Status'] = 'Online'
                        self.gServerDict[xServer['ServerName']]['Socket'] = xSocket
                    except socket.error :
                        print(xServer['ServerName']+' reconnecting...')
                    except :
                        pass
                    pass
            time.sleep(5)
        
        for xIndex, xServer in enumerate(self.gConfDict['SERVERLIST']):
            if operator.eq(self.gServerDict[xServer['ServerName']]['Status'], 'Online'):
                self.gServerDict[xServer['ServerName']]['Socket'].close()
                self.gServerDict[xServer['ServerName']]['Status'] = 'Offline'
                self.gServerDict[xServer['ServerName']]['Socket'] = []
        print('clientThreadHandle exit')
    
    @pyqtSlot()
    def on_pushButton_Ctrl_clicked(self):
        self.gRunEnv['curGameIndex'] = str(self.comboBox_List.currentIndex())
        nCmd = {'Option':'StartGame', 'Args':'0'}
        nCmd['Args'] = self.gRunEnv['curGameIndex']
        self.gCmdList.append(nCmd)
    
    @pyqtSlot()
    def on_pushButton_Ctrl2_clicked(self):
        nCmd = {'Option':'StopGame', 'Args':'0'}
        nCmd['Args'] = self.gRunEnv['curGameIndex']
        self.gCmdList.append(nCmd)
    
    def on_toolButton_clicked(self):
        if self.sender() == self.shutdowAction:
            nCmd = {'Option':'Shutdown', 'Args':' '}
            self.gCmdList.append(nCmd)
        elif self.sender() == self.restartAction:
            nCmd = {'Option':'Restart', 'Args':' '}
            self.gCmdList.append(nCmd)
        elif self.sender() == self.AboutAction:
            QMessageBox.information(self,"About vLauncher", self.tr("Name \t:vLauncher\r\nVersion\t:v0.1.2\r\nAuthor\t:loopedison"))
    
    def closeEvent(self, event):
        self.gRunStatus = -1
        event.accept()

#===============================================================================
if __name__ == "__main__":
    _app = QtWidgets.QApplication(sys.argv)
    _MainServer = MainClient()
    _MainServer.show()
    sys.exit(_app.exec_())
