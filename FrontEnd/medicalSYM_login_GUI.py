# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medicalSYM_login_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(1300, 1000)
        Login.setMinimumSize(QtCore.QSize(1300, 1000))
        Login.setMaximumSize(QtCore.QSize(1300, 1000))
        Login.setStyleSheet("*{\n"
"    font-family:Microsoft Sans Serif;\n"
"    font-size:24px;\n"
"}\n"
"\n"
"#widget{\n"
"    border-radius:15px;\n"
"    background-image: url(:/background/login_0.jpg);\n"
"}\n"
"\n"
"QFrame{\n"
"    background:rgba(0,0,0,0.8);\n"
"    border-radius:15px;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"    background:red;\n"
"    border-radius:60px;\n"
"}\n"
"\n"
"QToolButton{\n"
"    background:red;\n"
"    border-radius:60px;\n"
"}\n"
"QPushButton{\n"
"    color:white;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    border-radius:15px;\n"
"    background:#ff696b;\n"
"}\n"
"QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:#717072;\n"
"    border-bottom:1px solid #717072;\n"
"}\n"
"#pushButton_2{\n"
"    \n"
"    background-color: rgba(0,0,0,0);\n"
"    font-size:21px;\n"
"    border:none;\n"
"    color:#717072;\n"
"    border-bottom:1px solid #717072;\n"
"}")
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(120, 170, 501, 591))
        self.frame.setAccessibleName("")
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 80, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("*{\n"
"    color:white;\n"
"    font-size:24px;\n"
"    background:transparent;\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 480, 441, 71))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(40, 210, 431, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 340, 431, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("*{\n"
"    color:white;\n"
"    font-size:24px;\n"
"    background:transparent;\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 290, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("*{\n"
"    color:white;\n"
"    font-size:24px;\n"
"    background:transparent;\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 420, 201, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.toolButton = QtWidgets.QToolButton(Login)
        self.toolButton.setGeometry(QtCore.QRect(310, 110, 121, 121))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UIresource/icon_login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(35, 35))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(Login)
        self.toolButton_2.setGeometry(QtCore.QRect(1120, 50, 61, 51))
        self.toolButton_2.setStyleSheet("background-color: transparent;")
        self.toolButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/background/icon_exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_2.setObjectName("toolButton_2")
        self.widget = QtWidgets.QWidget(Login)
        self.widget.setGeometry(QtCore.QRect(30, 40, 1151, 841))
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.frame.raise_()
        self.toolButton.raise_()
        self.toolButton_2.raise_()

        self.retranslateUi(Login)
        self.toolButton_2.clicked.connect(Login.close)
        self.pushButton_2.clicked.connect(Login.login2register)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.label.setText(_translate("Login", "WELCOME TO MDS！\n"
"      LOGIN HERE"))
        self.pushButton.setText(_translate("Login", "Login"))
        self.label_2.setText(_translate("Login", "Username"))
        self.label_3.setText(_translate("Login", "Password"))
        self.pushButton_2.setText(_translate("Login", "Register An Account "))
import login_rc