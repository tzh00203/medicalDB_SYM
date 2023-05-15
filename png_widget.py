import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel


class png_show(QWidget):
    def __init__(self, parent=None):
        super(png_show, self).__init__(parent)
        self.setWindowTitle("排列组合")

        layout = QFormLayout()
        self.label = QLabel(self)

        layout.addRow(self.label)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = png_show()
    form.show()
    sys.exit(app.exec_())
