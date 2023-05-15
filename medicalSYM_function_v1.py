import os
from PyQt5.QtWidgets import QMainWindow
from medicalSYM_function_GUI import *
from PyQt5.QtMultimedia import QMediaPlayer


from function_mysql import *
from png_widget import *


def doctors_page_font(atm_btn, table, i, j):

    font = QtGui.QFont()
    font.setBold(True)
    font.setUnderline(True)
    atm_btn.setFont(font)   # 字体下划线
    atm_btn.setCursor(QtCore.Qt.PointingHandCursor)  # 设置鼠标悬浮样式
    table.setCellWidget(i, j, atm_btn)      # 添加单元格元素
    atm_btn.setStyleSheet("QToolButton{\n"
                          "    background-color: transparent;\n"
                          "    font-size:21px;\n"
                          "    border:none;\n"
                          "    color:blue;\n"
                          "    }"
                          "QToolButton:hover{\n"
                          "    color:rgb(60,170,255);\n"
                          "    }"
                          )


# 前端表格常规设置，并且会链接数据库获取数据
def table_set(table, Mysql, name, headerNames, index):

    # 连接数据库，生成表格数据
    table_value = Mysql.data_mysql(name)
    items = table_value
    rows = len(items)
    cols = len(items[0]) + index

    # table格式常规设置
    table.setColumnCount(cols)  # 设置表格数据列数
    table.setRowCount(rows)  # 设置表格数据行数
    table.setHorizontalHeaderLabels(headerNames)
    table.horizontalHeader().setCascadingSectionResizes(True)
    table.horizontalHeader().setHighlightSections(True)
    table.horizontalHeader().setVisible(True)
    table.verticalHeader().setVisible(True)
    table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # 表格长度填充
    table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 表格数据不可编辑
    table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)  # 每行内容自动换行

    return items, rows, cols


class MyWindow_function(Ui_Function, QMainWindow):  # 如果这两个参数调换就会导致Q_video_widget能否播放问题
    def __init__(self, parent=None):
        # 与mysql数据库连接初始化
        self.mysql = function2mysql('root', '127.0.0.1', "tzh2002315", "medicaldb")

        # 页面转换，初始化加载login页
        self.login_page = None
        self.welcome = None

        # 在创建可视化窗体之前先练一下数据库
        super(QMainWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 窗口置顶，无边框
        self.setupUi(self)
        self.add_shadow()  # 界面边框阴影
        self.set_cur()  # 鼠标悬停样式更改
        self.toolButStyle = "color:black;font: 63 9pt 'Bahnschrift SemiBold';font-size:23px;"
        self.toolButStyle_new = self.toolButStyle + "background-color: rgb(215, 215, 215); border-top:slide;"
        self.toolButtonList = [self.toolButton_2, self.toolButton_3, self.toolButton_4, self.toolButton_9]

        # 视频播放
        # 播放器
        self.player = QMediaPlayer()
        # self.player.setVideoOutput(self.wdt_player)

        # 鼠标位置属性定义
        self._startPos = None
        self._isTracking = None
        self._endPos = None

        # 表格数据初始化
        self.items_tep = None
        self.headerNames_dep = ['科室名字', '科室位置', '科室介绍', '科室人员']
        self.headerNames_doc = ['医生姓名', '年龄', '电话', '性别', '级别', '入职日期', '图片介绍']
        self.headerNames_pt = ['患者名字', '年龄', '性别', '电话', '居住地址', '入库日期', '病历本']
        self.headerNames_pt_records = ['患者姓名', '病历本id', '病例日期', '病类名', '诊治医生']
        self.one = png_show()    # 图片子窗口先加载
        self.dep_name = None     # 临时科室名字

        # 数据库新增数据字典定义
        self.newdep_info = {"dep_name": None, "location": None, "introduction": None}  # 创建科室注册信息字典

        self.newdoc_info = {"doc_name": None, "age": None, "tel": None,                # 创建医生注册信息字典
                            "gender": None, "introduction": None, "dep_name": None, "level": None,
                            "join_date": None}

        self.newpt_info = {"pt_name": None, "age": None, "gender": None, "tel": None,   # 创建患者注册信息字典
                           "address": None, "creation_date": None}
        # 数据库科室列表更新，方便添加医生时选择
        self.dep_list = []
        self.welcome_update()

    # 更新欢迎用户
    def welcome_update(self):
        print(str(self.welcome))
        self.label_2.clear()
        self.label_2.setText(self.welcome)

    # 数据库科室列表更新
    def dep_list_update(self):
        self.dep_list = []
        dep_value = self.mysql.data_mysql("departments")
        for line in dep_value:
            self.dep_list.append(line[0])
        self.comboBox_4.clear()
        self.comboBox_4.addItems(self.dep_list)

    # 删除元素操作
    def delete_dep(self):
        try:
            row = self.tableWidget.selectedItems()[0].row()
            main_name = self.tableWidget.item(row, 0).text()
            print(main_name)
            self.mysql.delete_data("departments", "dep_name", main_name)
        finally:
            self.press_Doctor()

    def delete_doc(self):
        try:
            row = self.tableWidget_3.selectedItems()[0].row()
            main_name = self.tableWidget_3.item(row, 0).text()
            print(main_name)
            self.mysql.delete_data("departments_consist", "doc_name", main_name)
        finally:
            self.label_8.setText("DEPARTMENTS_CONSIST_" + self.dep_name)
            self.stackedWidget.setCurrentIndex(4)
            self.init_doc_table(self.tableWidget_3, "doctors", self.headerNames_doc, self.dep_name)

    def delete_pt(self):
        try:
            row = self.tableWidget_2.selectedItems()[0].row()
            main_name = self.tableWidget_2.item(row, 0).text()
            print(main_name)
            self.mysql.delete_data("patients", "pt_name", main_name)
        finally:
            self.press_Patient()

    # doctors页面的departments表格初始化
    def init_dep_table(self, table, name, headerNames):
        # table常规设置，调用外部函数，减少代码冗余
        items, rows, cols = table_set(table, self.mysql, name, headerNames, 1)
        self.items_tep = items

        # table格式个性化设置
        for i in range(rows):
            nickname = str(items[i][0])
            for j in range(cols):
                if j != cols-1:
                    if str(items[i][j][0]) != '/':
                        item = QtWidgets.QTableWidgetItem(str(items[i][j]))
                        table.setItem(i, j, item)
                    else:  # 表格中添加原子操作

                        print("原子数据相对地址: " + str(items[i][j]))
                        # 设置跳转到介绍详情的按钮
                        atm_btn = QtWidgets.QToolButton()
                        doctors_page_font(atm_btn, table, i, j)
                        atm_btn.setText(nickname+"详情")  # 设置按钮跳转的文本
                        atm_btn.clicked.connect(self.atm_dep_info)  # 点击跳转到人员组成页
                # 科室人员列处理
                else:
                    # 设置跳转到组成人员的按钮
                    atm_btn = QtWidgets.QToolButton()
                    doctors_page_font(atm_btn, table, i, j)
                    atm_btn.setText(nickname+"人员")  # 设置按钮跳转的文本
                    atm_btn.clicked.connect(self.atm_doc_info)  # 点击跳转到介绍页

    # doctors页面的doctors表格初始化
    def init_doc_table(self, table, name, headerNames, dep_name):
        # table常规设置，调用外部函数，减少代码冗余
        items, rows, cols = table_set(table, self.mysql, name, headerNames, 2)
        self.dep_name = dep_name
        # 设置变量存储doctors、departments_consist表格数据,设置新的items、rows、cols用于循环
        items, rows = self.mysql.and_mysql("departments_consist", "doctors", dep_name)
        table.setRowCount(rows)  # 再次调整表格数据行数

        # table格式个性化设置
        for i in range(rows):
            nickname = str(items[i][0])
            for j in range(cols):

                if str(items[i][j])[0] != '/':
                    item = QtWidgets.QTableWidgetItem(str(items[i][j]))
                    # 设置单元格内容右对齐并与底部对齐
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    table.setItem(i, j, item)

                else:  # 表格中添加原子操作

                    print("原子数据相对地址: " + str(items[i][j]))
                    # 设置跳转到介绍详情的按钮
                    atm_btn = QtWidgets.QToolButton()
                    doctors_page_font(atm_btn, table, i, j)
                    atm_btn.setText(nickname+"图片")  # 设置按钮跳转的文本
                    atm_btn.clicked.connect(self.atm_doc_png)  # 点击跳转到人员组成页

    # patients页面的patients表格初始化
    def init_pt_table(self, table, name, headerNames):
        # table常规设置，调用外部函数，减少代码冗余
        items, rows, cols = table_set(table, self.mysql, name, headerNames, 1)

        # table格式个性化设置
        for i in range(rows):
            nickname = str(items[i][0])
            for j in range(cols):

                if j != cols-1:
                    item = QtWidgets.QTableWidgetItem(str(items[i][j]))
                    # 设置单元格内容右对齐并与底部对齐
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    table.setItem(i, j, item)

                else:  # 表格中添加原子操作
                    # 设置跳转到介绍详情的按钮
                    atm_btn = QtWidgets.QToolButton()
                    doctors_page_font(atm_btn, table, i, j)
                    atm_btn.setText(nickname+"病历本")  # 设置按钮跳转的文本
                    atm_btn.clicked.connect(self.atm_pt_info)  # 点击跳转到人员组成页

    # patients页面的病历表格初始化
    def init_pt_records(self, table, name, headerNames, pt_name):
        # table常规设置，调用外部函数，减少代码冗余
        table_set(table, self.mysql, name, headerNames, 0)
        # 设置变量存储doctors、departments_consist表格数据,设置新的items、rows、cols用于循环
        items, rows, cols = self.mysql.pt_records_mysql("patients_med_disease",  pt_name)
        table.setRowCount(rows)  # 再次调整表格数据行数
        # table格式个性化设置
        for i in range(rows):
            for j in range(cols):

                item = QtWidgets.QTableWidgetItem(str(items[i][j]))
                # 设置单元格内容右对齐并与底部对齐
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                table.setItem(i, j, item)

    # 科室介绍页面
    def atm_dep_info(self):
        currentPath = os.getcwd().replace('\\', '/')    # 获取当前路径
        filename = currentPath + "/后端/departments_intro/" + self.sender().text()[:-2] + ".txt"
        print(filename)
        file = open(filename, 'r', encoding="utf-8")  # fileAddress为txt文件的路径
        fileContent = file.read()  # 读取文件内容
        file.close()
        self.plainTextEdit.setPlainText(fileContent)  # 文本框变量名为textEdit
        self.stackedWidget.setCurrentIndex(3)

    # 科室人员详情页面
    def atm_doc_info(self):
        dep_name = self.sender().text()[:-2]
        currentPath = os.getcwd().replace('\\', '/')    # 获取当前路径
        filename = currentPath + "/后端/departments_intro/" + dep_name + ".png"
        print(filename)
        self.label_8.setText("DEPARTMENTS_CONSIST_" + dep_name)
        self.stackedWidget.setCurrentIndex(4)
        self.init_doc_table(self.tableWidget_3, "doctors", self.headerNames_doc, dep_name)

    #   医生图片小窗口
    def atm_doc_png(self):
        # 这个是可以单独运行的窗口
        currentPath = os.getcwd().replace('\\', '/')    # 获取当前路径
        filename = currentPath + "/后端/doctors_intro/" + self.sender().text()[:-2] + ".png"
        print(filename)
        self.one.label.setPixmap(QtGui.QPixmap(filename))  # 要注意是one的label
        self.one.label.setScaledContents(True)  # 图片大小与label适应，否则图片可能显示不全

        self.one.setWindowTitle(self.sender().text()[:-2] + "医生介绍卡片")
        self.one.show()

    #   患者病历详情页面
    def atm_pt_info(self):
        pt_name = self.sender().text()[:-3]
        self.label_9.setText("PATIENTS_RECORD_" + pt_name)
        self.stackedWidget.setCurrentIndex(10)
        self.init_pt_records(self.tableWidget_4, "patients_med_disease", self.headerNames_pt_records, pt_name)

    # # 打开视频文件并播放
    # def video_play(self):
    #     self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))
    #     self.player.play()

    # 主菜单各按钮被点击之后更改样式
    def press_selected(self):
        self.sender().setStyleSheet(self.toolButStyle_new)
        for btn in self.toolButtonList:
            if btn != self.sender():
                btn.setStyleSheet(self.toolButStyle)

    # 主菜单各按钮被点击之后切换页面
    def press_Logo(self):
        for btn in self.toolButtonList:
            btn.setStyleSheet(self.toolButStyle)
        self.stackedWidget.setCurrentIndex(0)

    def press_Hospital(self):
        self.stackedWidget.setCurrentIndex(1)
        self.lineEdit.clear()

    def press_Doctor(self):
        self.stackedWidget.setCurrentIndex(2)
        self.init_dep_table(self.tableWidget, 'departments', self.headerNames_dep)

    def press_Patient(self):
        self.stackedWidget.setCurrentIndex(5)
        self.init_pt_table(self.tableWidget_2, 'patients', self.headerNames_pt)

    def press_Drug(self):
        self.stackedWidget.setCurrentIndex(6)

    def press_keshi(self):
        self.register_dep_infoclr()
        self.stackedWidget.setCurrentIndex(7)

    def press_yisheng(self):
        self.register_doc_infoclr()
        self.dep_list_update()
        self.stackedWidget.setCurrentIndex(8)

    def press_huanzhe(self):
        self.register_pt_infoclr()
        self.stackedWidget.setCurrentIndex(9)

    # 添加阴影
    def add_shadow(self):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(0, 0)  # 偏移
        effect_shadow.setBlurRadius(40)  # 阴影半径
        effect_shadow.setColor(QtCore.Qt.black)  # 阴影颜色
        self.widget.setGraphicsEffect(effect_shadow)  # 将设置套用到widget窗口中

    # 无边框拖动
    def mouseMoveEvent(self, end: QtGui.QMouseEvent):  # 重写移动事件
        self._endPos = end.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, end: QtGui.QMouseEvent):
        if end.button() == QtCore.Qt.LeftButton:
            self._isTracking = True
            self._startPos = QtCore.QPoint(end.x(), end.y())

    def mouseReleaseEvent(self, end: QtGui.QMouseEvent):
        if end.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None

    def get_txtfile(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", os.getcwd(), "All Files(*);;Text Files(*.txt)")
        print(fileName)
        self.lineEdit_14.setText(fileName)

    def get_pngfile(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", os.getcwd(), "All Files(*);;Text Files(*.txt)")
        print(fileName)
        self.lineEdit_17.setText(fileName)

    def dep_2data(self):
        index = 0
        newdep_info_edit = [                               # 文本框注册信息列表,和字典顺序对应
            self.lineEdit_12.text(), self.lineEdit_13.text(), self.lineEdit_14.text()
        ]
        for key in self.newdep_info:                            # 科室信息字典更新
            self.newdep_info[key] = newdep_info_edit[index]
            index += 1
        self.dep_2data_result()

    def dep_2data_result(self):
        print(self.newdep_info)
        for key in self.newdep_info:       # 先检查一下输入的注册信息格式正不正确
            if self.newdep_info[key] == "":
                self.label_13.setText("The input information is incorrect")
                return

        b = self.mysql.newdep_info2medicaldb(self.newdep_info)  # 连接数据库medicaldb, 尝试写进新科室
        self.label_13.setText(b)                       # 返回注册结果
        if b[0] == '^':                                # 注册成功会把登记信息清空
            self.lineEdit_12.clear()
            self.lineEdit_13.clear()
            self.lineEdit_14.clear()

    def doc_2data(self):
        index = 0

        def gender():                    # 判断一下性别选择框
            if self.radioButton_3.isChecked():
                return "female"
            elif self.radioButton_4.isChecked():
                return "male"
            else:
                return "notchosen"

        newdoc_info_edit = [                               # 文本框注册信息列表,和字典顺序对应
            self.lineEdit_15.text(), self.lineEdit_16.text(), self.lineEdit_18.text(),
            gender(), self.lineEdit_17.text(), self.comboBox_4.currentText(),
            self.comboBox_6.currentText(), None  # 目前的入库时间先不确定，在后端里面确定
        ]
        for key in self.newdoc_info:                            # 医生信息字典更新
            self.newdoc_info[key] = newdoc_info_edit[index]
            index += 1
        self.doc_2data_result()

    def doc_2data_result(self):
        print(self.newdoc_info)
        for key in self.newdoc_info:       # 先检查一下输入的注册信息格式正不正确
            if self.newdoc_info[key] == "" or self.newdoc_info[key] == "notchosen":
                self.label_14.setText("The input information is incorrect")
                return

        b = self.mysql.newdoc_info2medicaldb(self.newdoc_info)  # 连接数据库medicaldb, 尝试写进新医生
        self.label_14.setText(b)                       # 返回注册结果
        if b[0] == '^':                                # 注册成功会把登记信息清空
            self.lineEdit_15.clear()
            self.lineEdit_16.clear()
            self.lineEdit_17.clear()
            self.lineEdit_18.clear()

    def pt_2data(self):
        index = 0

        def gender():                    # 判断一下性别选择框
            if self.radioButton_5.isChecked():
                return "女"
            elif self.radioButton_6.isChecked():
                return "男"
            else:
                return "notchosen"

        newpt_info_edit = [                               # 文本框注册信息列表,和字典顺序对应
            self.lineEdit_19.text(), self.lineEdit_20.text(),
            gender(), self.lineEdit_22.text(), self.lineEdit_21.text(),
            None  # 目前的入库时间先不确定，在后端里面确定
        ]
        print(newpt_info_edit)
        for key in self.newpt_info:                            # 患者信息字典更新
            self.newpt_info[key] = newpt_info_edit[index]
            index += 1
        self.pt_2data_result()

    def pt_2data_result(self):
        print(self.newpt_info)
        for key in self.newpt_info:       # 先检查一下输入的注册信息格式正不正确
            if self.newpt_info[key] == "" or self.newpt_info[key] == "notchosen":
                self.label_15.setText("The input information is incorrect")
                return

        b = self.mysql.newpt_info2medicaldb(self.newpt_info)  # 连接数据库medicaldb, 尝试写进新患者
        self.label_15.setText(b)                       # 返回注册结果
        if b[0] == '^':                                # 注册成功会把登记信息清空
            self.lineEdit_19.clear()
            self.lineEdit_20.clear()
            self.lineEdit_21.clear()
            self.lineEdit_22.clear()

    def register_dep_infoclr(self):
        self.label_13.setText("ADD_DATA_2_DEPARTMENTS")
        self.lineEdit_12.clear()
        self.lineEdit_13.clear()
        self.lineEdit_14.clear()

    def register_doc_infoclr(self):
        self.label_14.setText("ADD_DATA_2_DOCTORS")
        self.lineEdit_15.clear()
        self.lineEdit_16.clear()
        self.lineEdit_17.clear()
        self.lineEdit_18.clear()

    def register_pt_infoclr(self):
        self.label_15.setText("ADD_DATA_2_PATIENTS")
        self.lineEdit_19.clear()
        self.lineEdit_20.clear()
        self.lineEdit_21.clear()
        self.lineEdit_22.clear()

    def search_data(self):
        index = 1
        self.stackedWidget.setCurrentIndex(1)
        self.plainTextEdit_4.clear()
        key = self.lineEdit.text()
        search_result = self.mysql.search_mysql(key)
        if type(search_result) == str:
            self.plainTextEdit_4.appendPlainText(search_result)
            return
        for x in search_result:
            self.plainTextEdit_4.appendPlainText("(" + str(index) + ")  Relevant data tuples are found in this table: " + str(x))
            self.plainTextEdit_4.appendPlainText("     Relevant data : " + str(search_result[x]) + "\n")
            index += 1
        return

    def search_clear(self):
        self.lineEdit.clear()

    def ID_switch(self):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setWindowTitle('IDswitch')
        messageBox.setText('Are you sure to switch the ID?')
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        buttonY = messageBox.button(QtWidgets.QMessageBox.Yes)
        buttonY.setText('yes')
        buttonN = messageBox.button(QtWidgets.QMessageBox.No)
        buttonN.setText('no')
        messageBox.exec_()

        if messageBox.clickedButton() == buttonY:
            print('点击了yes')
            messageBox.close()
            self.close()
            self.login_page.login_infoclr()
            self.login_page.show()

    def function2login(self, login_page):
        self.login_page = login_page

    # 定义鼠标经过控件的样式
    def set_cur(self):
        # 设置光标为手指
        self.toolButton_6.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_2.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_3.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_4.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_9.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_11.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_12.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_16.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_17.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_18.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_19.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_25.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_5.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_6.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_7.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_20.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_21.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_23.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_24.setCursor(QtCore.Qt.PointingHandCursor)
        self.toolButton_8.setCursor(QtCore.Qt.PointingHandCursor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin_function = MyWindow_function()
    myWin_function.show()
    sys.exit(app.exec_())
