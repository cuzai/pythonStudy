from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5 import uic

uiPath = 'C:/Users/cuzai/Desktop/Web_Crawling/pythonStudy/QT/example/PyQTBasic3.ui'

form_class = uic.loadUiType(uiPath)[0]


class TestForm(QtWidgets.QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__' :
    app = QtWidgets.QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()