# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Yummy\A_Python\python-learn\study_vLauncher\client.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 175)
        Dialog.setMinimumSize(QtCore.QSize(400, 150))
        Dialog.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/vLauncher.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label_Status = QtWidgets.QLabel(Dialog)
        self.label_Status.setGeometry(QtCore.QRect(10, 150, 291, 21))
        self.label_Status.setObjectName("label_Status")
        self.pushButton_Ctrl = QtWidgets.QPushButton(Dialog)
        self.pushButton_Ctrl.setGeometry(QtCore.QRect(310, 10, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.pushButton_Ctrl.setFont(font)
        self.pushButton_Ctrl.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_Ctrl.setObjectName("pushButton_Ctrl")
        self.comboBox_List = QtWidgets.QComboBox(Dialog)
        self.comboBox_List.setGeometry(QtCore.QRect(10, 10, 291, 33))
        self.comboBox_List.setMinimumSize(QtCore.QSize(121, 33))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.comboBox_List.setFont(font)
        self.comboBox_List.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox_List.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.comboBox_List.setEditable(False)
        self.comboBox_List.setCurrentText("")
        self.comboBox_List.setMaxVisibleItems(5)
        self.comboBox_List.setObjectName("comboBox_List")
        self.listWidget_Links = QtWidgets.QListWidget(Dialog)
        self.listWidget_Links.setGeometry(QtCore.QRect(10, 50, 291, 91))
        self.listWidget_Links.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget_Links.setObjectName("listWidget_Links")
        self.pushButton_Ctrl2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_Ctrl2.setGeometry(QtCore.QRect(310, 80, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.pushButton_Ctrl2.setFont(font)
        self.pushButton_Ctrl2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_Ctrl2.setObjectName("pushButton_Ctrl2")
        self.toolButton_More = QtWidgets.QToolButton(Dialog)
        self.toolButton_More.setGeometry(QtCore.QRect(310, 150, 81, 21))
        self.toolButton_More.setFocusPolicy(QtCore.Qt.TabFocus)
        self.toolButton_More.setStyleSheet("background-color: rgb(240, 240, 240);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/Settings.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_More.setIcon(icon1)
        self.toolButton_More.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton_More.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_More.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_More.setObjectName("toolButton_More")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboBox_List, self.pushButton_Ctrl)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "vLauncher"))
        self.label_Status.setText(_translate("Dialog", "Status：IDLE"))
        self.pushButton_Ctrl.setText(_translate("Dialog", "Run"))
        self.pushButton_Ctrl2.setText(_translate("Dialog", "Stop"))
        self.toolButton_More.setText(_translate("Dialog", " More"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

