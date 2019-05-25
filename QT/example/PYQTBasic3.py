import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore

class TestForm(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyQT Teset")
        self.setGeometry(800, 400, 500, 500)

        label1_1 = QLabel("입력테스트", self)
        label1_2 = QLabel("출력테스트", self)

        label1_1.move(20, 20)
        label1_2.move(20, 60)

        self.lineEdit = QLineEdit("", self) # Default값 = ""
        self.plainEdit = QtWidgets.QPlainTextEdit(self)
        # self.plainEdit.setReadOnly(True)

        self.lineEdit.move(110,20)
        self.plainEdit.setGeometry(QtCore.QRect(20, 90, 361, 231))

        self.lineEdit.textChanged.connect(self.lineEditChanged)
        self.lineEdit.returnPressed.connect(self.lineEditEnter)

        # 상태바
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def lineEditChanged(self) :
        self.statusBar.showMessage(self.lineEdit.text())

    def lineEditEnter(self):
        self.plainEdit.appendPlainText(self.lineEdit.text())    # insertPlainText : 줄바꿈을 해주지 않음
        # self.plainEdit.insertPlainText(self.lineEdit.text())
        self.lineEdit.clear()


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()