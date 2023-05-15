from medicalSYM_login_v2 import *
from medicalSYM_function_v1 import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin_function = MyWindow_function()
    myWin_function.show()
    myWin_function.hide()
    myWin_login = MyWindow_login(myWin_function)
    myWin_function.function2login(myWin_login)
    myWin_login.show()

    sys.exit(app.exec_())
