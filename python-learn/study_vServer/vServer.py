#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module implementing vServer.
"""

# ==============================================================================
import os
import sys
import time
import json
import socket
import threading

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QAction, QMenu, QMessageBox, QSystemTrayIcon
from PyQt5.QtGui import *

from Ui_server import Ui_Form


# ==============================================================================
class vServer(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(vServer, self).__init__(parent)
        self.setupUi(self)
        self.setupMain()

    def setupMain(self):
        # configure list
        self.serverConfig = {'WorkPath': os.getcwd(), 'ServerStatus': True,
                             'ConfigDict': {}, 'Client': [], 'Task': [],
                             'CurTask': {'curStatus': 'IDLE', 'curIndex': '0'}}

        # load configurations from "config.json"
        with open('config.json', 'r+', encoding='utf-8') as confList:
            self.serverConfig['ConfigDict'] = json.load(confList)

        # config toolButton_More
        self.tool_menu = QMenu(self)
        self.tool_menu.addAction(QAction(QIcon('image/shutdown.ico'), 'Shutdown', self, triggered=self.on_toolButton_clicked_shut))
        self.tool_menu.addAction(QAction(QIcon('image/restart.ico'), 'Restart', self, triggered=self.on_toolButton_clicked_reset))
        self.tool_menu.addSeparator()
        self.tool_menu.addAction(QAction(QIcon('image/Star.ico'), 'About&Help', self, triggered=self.on_toolButton_clicked_about))
        self.toolButton_More.setMenu(self.tool_menu)

        # support system Tray
        self.sysTrayIcon = QSystemTrayIcon(QIcon("image/logo.ico"))
        self.sysTrayIconMenu = QMenu()
        self.sysTrayIconMenu.addAction(QAction('Show', self, triggered=self.showNormal))
        self.sysTrayIconMenu.addAction(QAction('Exit', self, triggered=self.serverExit))
        self.sysTrayIcon.setContextMenu(self.sysTrayIconMenu)
        self.sysTrayIcon.setToolTip('vServer')

        # configure combobox
        for game in self.serverConfig['ConfigDict']['GAMELIST']:
            self.comboBox_List.addItem(game['GameName'])

        # Create TCP server Thread
        self.serverThread = threading.Thread(target=self.serverThreadHandle)
        self.serverThread.setDaemon(True)
        self.serverThread.start()

    def serverThreadHandle(self):
        print('Server:\tStarting ...')
        # configure TCP server
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serverSocket.bind((self.serverConfig['ConfigDict'].get('LocalIP', ''), int(self.serverConfig['ConfigDict'].get('ServerPort', '9527'))))
        self.serverSocket.listen(10)
        self.serverSocket.setblocking(False)
        xClientCnt = 1  # record client num for UI
        xClientStatus = True  # conn
        # server loop
        while self.serverConfig['ServerStatus'] == True:
            # waiting for connections
            try:
                clientSocket, clientAddr = self.serverSocket.accept()
            except:
                pass
            else:
                print('Server:\t<%s> connected!' % (str(clientAddr)))
                clientSocket.setblocking(False)
                self.serverConfig['Client'].append((clientSocket, clientAddr))
            # receive message from client
            for sck, addr in self.serverConfig['Client']:
                xClientStatus = True
                try:
                    xMsg = sck.recv(1024)
                except ConnectionResetError:
                    xClientStatus = False
                except:
                    pass
                else:
                    print('Server:\t<%s>:<%s>' % (str(addr), xMsg))
                    if len(xMsg) > 0:
                        self.serverConfig['Task'].append((sck, xMsg.decode('utf-8')))
                    else:
                        xClientStatus = False
                # if disconnect
                if xClientStatus == False:
                    print('Server:\t<%s> disconnected!' % (str(addr)))
                    sck.close()
                    self.serverConfig['Client'].remove((sck, addr))

            # handle task
            if len(self.serverConfig['Task']) > 0:
                xSender, xMessage = self.serverConfig['Task'].pop(0)
                try:
                    xTask = json.loads(xMessage)
                    # Analysize message
                    if 'Option' in xTask.keys():
                        xArgs = xTask['Option'].split()
                        print('Option:\t<%s>' % (xArgs))
                        if xArgs[0].upper() == "StartGame".upper():
                            print('StartGame')
                        elif xArgs[0].upper() == "StopGame".upper():
                            print('StopGame')
                except:
                    pass
            # update online status
            if xClientCnt != len(self.serverConfig['Client']):
                xClientCnt = len(self.serverConfig['Client'])
                if xClientCnt > 0:
                    self.label_Online.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.label_Online.setText('Connection[%2d]:(%s:%s)' % (len(self.serverConfig['Client']), self.serverConfig['Client'][-1][1][0], self.serverConfig['Client'][-1][1][1]))
                else:
                    self.label_Online.setStyleSheet("background-color: rgb(211, 211, 211);")
                    self.label_Online.setText('Connection[%2d]' % (0))
        print('Server:\tExiting ...')
        for sck, addr in self.serverConfig['Client']: sck.close()
        self.serverSocket.close()

    @pyqtSlot()
    def serverExit(self):
        if self.serverThread.isAlive():
            self.serverConfig['ServerStatus'] = False
        self.serverThread.join()
        self.hide()
        self.sysTrayIcon.setVisible(False)
        QtWidgets.QApplication.instance().quit()

    @pyqtSlot()
    def on_pushButton_Ctrl_clicked(self):
        if self.pushButton_Ctrl.text() == 'Run':
            self.serverConfig['Task'].append((0, json.dumps({'Option': 'StartGame -n %d' % self.comboBox_List.currentIndex()})))
        else:
            self.serverConfig['Task'].append((0, json.dumps({'Option': 'StopGame'})))

    @pyqtSlot()
    def on_toolButton_clicked_shut(self):
        self.serverConfig['Task'].append((0, json.dumps({'Option': 'Shutdown'})))

    def on_toolButton_clicked_reset(self):
        self.serverConfig['Task'].append((0, json.dumps({'Option': 'Restart'})))

    def on_toolButton_clicked_about(self):
        QMessageBox.information(self, "About vServer", self.tr("Name \t:vServer\r\nVersion\t:v0.1.0\r\nAuthor\t:loopedison"))

    @pyqtSlot()
    def closeEvent(self, event):
        event.ignore()
        self.hide()

# ==============================================================================
if __name__ == "__main__":
    _app = QtWidgets.QApplication(sys.argv)
    _vServer = vServer()
    _vServer.show()
    sys.exit(_app.exec_())