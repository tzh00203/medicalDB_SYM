# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medicalSYM_register_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import login


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(1300, 1000)
        Register.setMinimumSize(QtCore.QSize(1300, 1000))
        Register.setMaximumSize(QtCore.QSize(1300, 1000))
        Register.setStyleSheet("*{\n"
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
"")
        self.frame = QtWidgets.QFrame(Register)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(120, 170, 971, 591))
        self.frame.setAccessibleName("")
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 70, 201, 61))
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
        self.pushButton.setGeometry(QtCore.QRect(510, 470, 441, 71))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(40, 170, 431, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 270, 431, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 161, 61))
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
        self.label_3.setGeometry(QtCore.QRect(40, 220, 161, 61))
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
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(510, 20, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("*{\n"
"    color:white;\n"
"    font-size:24px;\n"
"    background:transparent;\n"
"}\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(510, 70, 431, 41))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(510, 120, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("*{\n"
"    color:white;\n"
"    font-size:24px;\n"
"    background:transparent;\n"
"}\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 320, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("*{\n"
"    color:white;\n"
"    font-size:24px;\n"
"    background:transparent;\n"
"}\n"
"")
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 370, 431, 41))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 420, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("*{\n"
"    color:white;\n"
"    font-size:24px;\n"
"    background:transparent;\n"
"}\n"
"")
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(40, 470, 431, 41))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(510, 220, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("*{\n"
"    color:white;\n"
"    font-size:24px;\n"
"    background:transparent;\n"
"}\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(510, 320, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("*{\n"
"    color:white;\n"
"    font-size:24px;\n"
"    background:transparent;\n"
"}\n"
"")
        self.label_9.setObjectName("label_9")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(510, 190, 115, 19))
        self.radioButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton.setStyleSheet("color:#717072;")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(630, 190, 115, 19))
        self.radioButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_2.setStyleSheet("color:#717072;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(510, 270, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.dateEdit.setFont(font)
        self.dateEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.dateEdit.setStyleSheet("color: rgb(113, 112, 114);\n"
"background:transparent;\n"
"border:none;")
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2002, 2, 2), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setObjectName("dateEdit")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(510, 370, 431, 61))
        self.comboBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox.setAccessibleName("")
        self.comboBox.setStyleSheet("color: rgb(113, 112, 114);\n"
"background:transparent;")
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 30, 61, 28))
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"    \n"
"    background-color: rgba(0,0,0,0);\n"
"    font-size:21px;\n"
"    border:none;\n"
"    color:#717072;\n"
"    border-bottom:1px solid #717072;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.toolButton = QtWidgets.QToolButton(Register)
        self.toolButton.setGeometry(QtCore.QRect(310, 110, 121, 121))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UIresource/icon_login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(35, 35))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(Register)
        self.toolButton_2.setGeometry(QtCore.QRect(1120, 50, 61, 51))
        self.toolButton_2.setStyleSheet("background-color: transparent;")
        self.toolButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/background/icon_exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_2.setObjectName("toolButton_2")
        self.widget = QtWidgets.QWidget(Register)
        self.widget.setGeometry(QtCore.QRect(30, 40, 1151, 841))
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.frame.raise_()
        self.toolButton.raise_()
        self.toolButton_2.raise_()

        self.retranslateUi(Register)
        self.toolButton_2.clicked.connect(Register.close)
        self.pushButton_2.clicked.connect(Register.register2login)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Form"))
        self.label.setText(_translate("Register", "USER REGISTER"))
        self.pushButton.setText(_translate("Register", "Register"))
        self.lineEdit.setPlaceholderText(_translate("Register", "Please enter account number"))
        self.lineEdit_2.setPlaceholderText(_translate("Register", "Please enter your password"))
        self.label_2.setText(_translate("Register", "Username"))
        self.label_3.setText(_translate("Register", "Password"))
        self.label_4.setText(_translate("Register", "Name"))
        self.lineEdit_3.setPlaceholderText(_translate("Register", "Please enter your real name"))
        self.label_5.setText(_translate("Register", "Gender"))
        self.label_6.setText(_translate("Register", "Telephone"))
        self.lineEdit_5.setPlaceholderText(_translate("Register", "Please enter your phone number"))
        self.label_7.setText(_translate("Register", "Email"))
        self.lineEdit_6.setPlaceholderText(_translate("Register", "Please enter your email address"))
        self.label_8.setText(_translate("Register", "Data of birth"))
        self.label_9.setText(_translate("Register", "Position in the hospital"))
        self.radioButton.setText(_translate("Register", "Female"))
        self.radioButton_2.setText(_translate("Register", "Male"))
        self.dateEdit.setDisplayFormat(_translate("Register", "yyyy-M-d"))
        self.comboBox.setItemText(0, _translate("Register", "None"))
        self.comboBox.setItemText(1, _translate("Register", "Work-service personnel"))
        self.comboBox.setItemText(2, _translate("Register", "Professional staff"))
        self.comboBox.setItemText(3, _translate("Register", "Administrative staff"))
        self.pushButton_2.setText(_translate("Register", "BACK"))

