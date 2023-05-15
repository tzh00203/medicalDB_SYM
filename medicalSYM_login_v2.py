from medicalSYM_finallogin_GUI import *
from login_user import *
from create_newuser import *
from medicalSYM_function_v1 import *


class MyWindow_login(QMainWindow, Ui_Login):
    def __init__(self, page):
        super(MyWindow_login, self).__init__(None)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 窗口置顶，无边框
        self.setupUi(self)
        self.add_shadow()  # 界面边框阴影
        self.set_cur()  # 鼠标悬停样式更改
        self.frame_2.hide()
        self.user_info = {                                       # 创建用户登录信息字典
            "username": None, "password": None}
        self.newuser_info = {                                    # 创建用户注册信息字典
            "username": None, "password": None, "telephone": None, "email": None,
            "name": None, "gender": None, "Birthdate": None, "job": None}
        # 鼠标位置属性定义
        self._startPos = None
        self._isTracking = None
        self._endPos = None

        # 为了跳转到function页的初始化定义
        self.status = True
        self.page = page

    # 设置点击返回按钮跳转到登录界面事件
    def register2login(self):
        self.frame_2.hide()
        self.frame.show()
        self.register_infoclr()
        self.label.setText("                WELCOME TO MDS！\n                       LOGIN HERE")

    # 设置点击注册按钮跳转到注册界面事件
    def login2register(self):
        self.frame.hide()
        self.toolButton_3.hide()            # 先要隐藏一下注册结果
        self.toolButton_4.hide()
        self.frame_2.show()

    #   用户登录事件
    def press_login(self):
        user_info_edit = [                               # 文本框登录信息列表,和字典顺序对应
           self.lineEdit.text(), self.lineEdit_2.text()
        ]
        self.user_info["username"] = user_info_edit[0]
        self.user_info["password"] = user_info_edit[1]
        self.press_login_result()

    def press_login_result(self):
        print(self.user_info)
        for key in self.user_info:       # 先检查一下输入的登录信息格式正不正确
            if self.user_info[key] == "":
                self.label.setText("                WELCOME TO MDS！\nPlEASE ENTER INFO-BELOW FIRST~")
                return
        if user_2MDS(self.user_info) == "success":                                                                          # 登陆成功,跳转到功能页面
            self.label.setText("                WELCOME TO MDS！\n            LOGIN SUCCESSFULLY~")
            self.status = False
            self.hide()
            self.page.welcome = "Welcome,User: " + str(self.user_info["username"])
            self.page.welcome_update()
            self.page.show()

        else:
            self.label.setText("                WELCOME TO MDS！\nTHE Username or Password is WRONG")

    # 注册新用户信息事件
    def press_register(self):
        index = 0
        self.toolButton_3.hide()         # 先要隐藏一下注册结果
        self.toolButton_4.hide()

        def gender():                    # 判断一下性别选择框
            if self.radioButton_3.isChecked():
                return "female"
            elif self.radioButton_4.isChecked():
                return "male"
            else:
                return "notchosen"

        newuser_info_edit = [                               # 文本框注册信息列表,和字典顺序对应
            self.lineEdit_8.text(), self.lineEdit_9.text(), self.lineEdit_10.text(), self.lineEdit_11.text(),
            self.lineEdit_12.text(), gender(), self.dateEdit_2.text(), self.comboBox_2.currentText()
        ]
        for key in self.newuser_info:                            # 用户信息字典更新
            self.newuser_info[key] = newuser_info_edit[index]
            index += 1
        self.press_register_result()

    def press_register_result(self):
        print(self.newuser_info)
        for key in self.newuser_info:       # 先检查一下输入的注册信息格式正不正确
            if self.newuser_info[key] == "" or self.newuser_info[key] == "notchosen":
                self.toolButton_4.show()
                return
        self.toolButton_3.show()
        b = newuser_info2medicaldb(self.newuser_info)  # 连接数据库medicaldb, 尝试写进新用户
        self.toolButton_3.setText(b)                   # 返回注册结果
        self.toolButton_3.show()
        if b[0] == '^':                                # 注册成功会把登记信息清空
            self.register_infoclr()

    #  登录页面信息恢复
    def login_infoclr(self):
        self.label.setText("                WELCOME TO MDS！\n")
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    # 注册页面信息清空
    def register_infoclr(self):
        for lineEdit in [self.lineEdit_8, self.lineEdit_9, self.lineEdit_10,
                         self.lineEdit_11, self.lineEdit_12]:
            lineEdit.setText("")
        self.dateEdit_2.setDate(QtCore.QDate(2002, 2, 2))
        self.comboBox_2.setCurrentText("None")

    # 添加阴影
    def add_shadow(self):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 0)  # 偏移
        effect_shadow.setBlurRadius(40)  # 阴影半径
        effect_shadow.setColor(QtCore.Qt.black)  # 阴影颜色
        self.widget.setGraphicsEffect(effect_shadow)  # 将设置套用到widget窗口中

    # 无边框拖动
    def mouseMoveEvent(self, e: QtGui.QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = True
            self._startPos = QtCore.QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None

    # 定义鼠标经过控件的样式
    def set_cur(self):
        self.pushButton.setCursor(QtCore.Qt.PointingHandCursor)             # 设置光标为手指
        self.pushButton_2.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_2.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_5.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_6.setCursor(QtCore.Qt.PointingHandCursor)
