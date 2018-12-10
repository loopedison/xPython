# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Yummy\A_Python\python-learn\study_vServer\server.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 105)
        Form.setMinimumSize(QtCore.QSize(400, 105))
        Form.setMaximumSize(QtCore.QSize(400, 105))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.toolButton_More = QtWidgets.QToolButton(Form)
        self.toolButton_More.setGeometry(QtCore.QRect(310, 80, 81, 21))
        self.toolButton_More.setFocusPolicy(QtCore.Qt.TabFocus)
        self.toolButton_More.setStyleSheet("background-color: rgb(240, 240, 240);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/Settings.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_More.setIcon(icon1)
        self.toolButton_More.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton_More.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_More.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_More.setObjectName("toolButton_More")
        self.comboBox_List = QtWidgets.QComboBox(Form)
        self.comboBox_List.setGeometry(QtCore.QRect(10, 10, 291, 33))
        self.comboBox_List.setMinimumSize(QtCore.QSize(121, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_List.setFont(font)
        self.comboBox_List.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox_List.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.comboBox_List.setEditable(False)
        self.comboBox_List.setCurrentText("")
        self.comboBox_List.setMaxVisibleItems(5)
        self.comboBox_List.setObjectName("comboBox_List")
        self.label_Status = QtWidgets.QLabel(Form)
        self.label_Status.setGeometry(QtCore.QRect(10, 80, 291, 21))
        self.label_Status.setObjectName("label_Status")
        self.pushButton_Ctrl = QtWidgets.QPushButton(Form)
        self.pushButton_Ctrl.setGeometry(QtCore.QRect(310, 10, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.pushButton_Ctrl.setFont(font)
        self.pushButton_Ctrl.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_Ctrl.setObjectName("pushButton_Ctrl")
        self.label_Online = QtWidgets.QLabel(Form)
        self.label_Online.setGeometry(QtCore.QRect(10, 50, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.label_Online.setFont(font)
        self.label_Online.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.label_Online.setText("")
        self.label_Online.setObjectName("label_Online")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "vServer"))
        self.toolButton_More.setText(_translate("Form", " More"))
        self.label_Status.setText(_translate("Form", "Status：IDLE"))
        self.pushButton_Ctrl.setText(_translate("Form", "Run"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

