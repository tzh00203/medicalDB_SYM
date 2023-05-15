import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from medicalSYM_login_GUI import *
from medicalSYM_register_GUI import *


class MyWindow_register(QMainWindow, Ui_Register):
    def __init__(self, parent=None):
        super(MyWindow_register, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 窗口置顶，无边框
        self.setupUi(self)
        self.add_shadow()  # 界面边框阴影

        # 鼠标位置属性定义
        self._startPos = None
        self._isTracking = None
        self._endPos = None

    # 设置点击返回按钮跳转到登录界面事件
    def register2login(self):
        pass

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


class MyWindow_login(QMainWindow, Ui_Login):
    def __init__(self, parent=None):
        super(MyWindow_login, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 窗口置顶，无边框
        self.setupUi(self)
        self.add_shadow()  # 界面边框阴影
        self.set_cur()  # 鼠标悬停样式更改

        # 鼠标位置属性定义
        self._startPos = None
        self._isTracking = None
        self._endPos = None

        # 跳转页面定义
        self.myWin_register = MyWindow_register()

    # 设置点击注册按钮跳转到注册界面事件
    def login2register(self):
        self.myWin_register.show()
        self.hide()
        print(888)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin_login = MyWindow_login()
    myWin_login.show()
    sys.exit(app.exec_())
