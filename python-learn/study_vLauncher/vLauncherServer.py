#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module implementing MainServer.
"""

#===============================================================================
import os
import sys
import json
import socket
import subprocess
import threading
import operator

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog, QAction, QMenu, QMessageBox, QSystemTrayIcon
from PyQt5.QtGui import *

from Ui_server import Ui_Dialog

#===============================================================================
class MainServer(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainServer, self).__init__(parent)
        self.setupUi(self)
        self.mainSetup()
    
    def mainSetup(self):
        # WorkPath
        self.gWorkPath = os.getcwd()
        print('WorkPath:%s' %(self.gWorkPath))
        
        # commander list
        self.gRunEnv = {'curGameIndex':'0', 'curGameStatus':'IDLE'}
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
        
        # add minimumHINT and closeHINT
        self.setWindowFlags(Qt.Widget)
        
        # support system Tray
        self.sysTrayIcon = QSystemTrayIcon()
        self.sysTrayIcon.setIcon(QIcon("image/vLauncher.ico"))
        self.sysTrayIconMenu=QMenu()
        self.sysTrayIconMenu.addAction(QAction('Show', self, triggered=self.showNormal))
        self.sysTrayIconMenu.addAction(QAction('Exit', self, triggered=self.mainExit))
        self.sysTrayIcon.setContextMenu(self.sysTrayIconMenu)
        self.sysTrayIcon.setToolTip('vLauncher Server')
        
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
        self.updateLoop.timeout.connect(self.serverTimerHandle)
        self.updateLoop.start(100)
        
        self.serverThreadList = {'ServCnt':0, 'ServAddr':[]}
        
        # Create TCP server Thread
        self.serverThread = threading.Thread(target=self.serverThreadHandle)
        self.serverThread.setDaemon(True)
        self.serverThread.start()
    
    def serverTimerHandle(self):
        # command handle
        if len(self.gCmdList) > 0:
            newCmd = self.gCmdList.pop(0)
            if newCmd['Option'] == 'Shutdown':
                try:
                    # shutdown
                    os.system("shutdown -s -t 0")
                except Exception:
                    pass
            elif newCmd['Option'] == 'Restart':
                try:
                    # shutdown
                    os.system("shutdown -r -t 0")
                except Exception:
                    pass
            elif newCmd['Option'] == 'StartGame':
                if self.gRunEnv['curGameStatus'] == 'IDLE':
                    self.gRunEnv['curGameIndex'] = newCmd['Args']
                    try:
                        # Start application current
                        # Change current path, then process, return at last
                        os.chdir(os.path.split(self.gGameList[int(self.gRunEnv['curGameIndex'])]['GamePath'])[0])
                        subprocess.Popen(os.path.split(self.gGameList[int(self.gRunEnv['curGameIndex'])]['GamePath'])[1])
                        self.gRunEnv['curGameStatus'] = 'RUNNING'
                        self.label_Status.setText("Status：[%s] Running!" %(self.gGameList[int(self.gRunEnv['curGameIndex'])]['GameName']))
                        self.pushButton_Ctrl.setText("Stop")
                        self.pushButton_Ctrl.setStyleSheet("background-color: rgb(255, 0, 0);")
                    except Exception:
                        self.label_Status.setText("Status：[%s] Open Failed!" %(self.gGameList[int(self.gRunEnv['curGameIndex'])]['GameName']))
                    # Return to workpath
                    os.chdir(self.gWorkPath)
                    pass
            elif newCmd['Option'] == 'StopGame':
                if self.gRunEnv['curGameStatus'] == 'RUNNING':
                    try:
                        # Stop application current
                        os.system("taskkill /F /T /IM %s" %(os.path.splitext(os.path.split(self.gGameList[int(self.gRunEnv['curGameIndex'])]['GamePath'])[1])[0]+'*'))
                        self.gRunEnv['curGameStatus'] = 'IDLE'
                        self.label_Status.setText("Status：[%s] finished!" %(self.gGameList[int(self.gRunEnv['curGameIndex'])]['GameName']))
                        self.pushButton_Ctrl.setText("Run")
                        self.pushButton_Ctrl.setStyleSheet("background-color: rgb(0, 255, 0);")
                    except Exception:
                        self.label_Status.setText("Status：[%s] Close Failed!" %(self.gGameList[int(self.gRunEnv['curGameIndex'])]['GameName']))
                    pass
        
        # update online status
        if self.serverThreadList['ServCnt'] != len(self.serverThreadList['ServAddr']):
            self.serverThreadList['ServCnt'] = len(self.serverThreadList['ServAddr'])
            if self.serverThreadList['ServCnt'] > 0:
                self.label_Online.setStyleSheet("background-color: rgb(0, 255, 0);")
                self.label_Online.setText('Online[%2d]=>(%s:%s)' %(self.serverThreadList['ServCnt'], self.serverThreadList['ServAddr'][-1][0], self.serverThreadList['ServAddr'][-1][1]))
            else:
                self.label_Online.setStyleSheet("background-color: rgb(211, 211, 211);")
                self.label_Online.setText('Offline!')
    
    def serverGetHostIP(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip
    
    def serverThreadHandle(self):
        # configure TCP server
        self.serverIP = self.gConfDict.get('LocalIP', self.serverGetHostIP())
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serverSocket.bind((self.serverIP, int(self.gConfDict['ServerPort'])))
        self.serverSocket.listen(5)
        # self.serverSocket.setblocking(False)   #none-Blocking
        # waiting service with thread
        try:
            while True:
                newSocket,destAddr = self.serverSocket.accept()
                conn = threading.Thread(target=self.serverThreadDealClient, args=(newSocket,destAddr))
                conn.setDaemon(True)
                conn.start()
        finally:
            self.serverSocket.close()
    
    def serverThreadDealClient(self, newSocket, destAddr):
        self.serverThreadList['ServAddr'].append(destAddr)  #=====list=====
        print('[%s] connected!'%(str(destAddr)))
        while True:
            try:
                recvData = newSocket.recv(1024)
                if len(recvData) > 0:
                    print('recv:[%s]:[%s]'%(str(destAddr), recvData))
                    try:
                        newCmd = json.loads(recvData.decode('utf-8'))
                        if operator.eq(newCmd['Option'], "Shutdown"):
                            self.gCmdList.append(newCmd)
                            pass
                        elif operator.eq(newCmd['Option'], "Restart"):
                            self.gCmdList.append(newCmd)
                            pass
                        elif operator.eq(newCmd['Option'], "StartGame"):
                            self.gRunEnv['curGameIndex'] = newCmd['Args']
                            newCmd['Args'] = self.gRunEnv['curGameIndex']
                            self.gCmdList.append(newCmd)
                        elif operator.eq(newCmd['Option'], "StopGame"):
                            self.gCmdList.append(newCmd)
                    except :
                        pass
                else:
                    break
            except :
                break
        newSocket.close()
        print('[%s] disconnected!'%(str(destAddr)))
        self.serverThreadList['ServAddr'].remove(destAddr)  #=====list=====
    
    def mainExit(self):
        self.hide()
        self.sysTrayIcon.setVisible(False)
        QtWidgets.QApplication.instance().quit()
    
    @pyqtSlot()
    def on_pushButton_Ctrl_clicked(self):
        if self.pushButton_Ctrl.text() == 'Run':
            nCmd = {'Option':'StartGame', 'Args':'0'}
            nCmd['Args'] = str(self.comboBox_List.currentIndex())
        else:
            nCmd = {'Option':'StopGame', 'Args':'0'}
        self.gCmdList.append(nCmd)
    
    @pyqtSlot()
    def on_toolButton_clicked(self):
        if self.sender() == self.shutdowAction:
            nCmd = {'Option':'Shutdown', 'Args':' '}
            self.gCmdList.append(nCmd)
        elif self.sender() == self.restartAction:
            nCmd = {'Option':'Restart', 'Args':' '}
            self.gCmdList.append(nCmd)
        elif self.sender() == self.AboutAction:
            QMessageBox.information(self,"About vLauncher", self.tr("Name \t:vLauncher\r\nVersion\t:v0.1.2\r\nAuthor\t:loopedison"))
    
    @pyqtSlot()
    def closeEvent(self, event):
        event.ignore()
        self.hide()
    
#===============================================================================
if __name__ == "__main__":
    _app = QtWidgets.QApplication(sys.argv)
    _MainServer = MainServer()
    _MainServer.show()
    sys.exit(_app.exec_())
