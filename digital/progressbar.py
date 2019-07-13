import time
from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import pyqtSlot
from test import test
from ui.progressbar import Ui_Dialog

class Progressbar(QtWidgets.QDialog, Ui_Dialog) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.test = test()
        self.test.finished.connect(self.run)
        self.test.start()

    @pyqtSlot(int)
    def run(self, val):
        self.progressBar.setValue(val)




if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    loginDialog = Progressbar()
    loginDialog.show()
    app.exec_()

