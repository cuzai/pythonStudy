import time

from PyQt5.QtCore import QThread, pyqtSignal


class test(QThread) :
    finished = pyqtSignal(int)

    def run(self):
        for i in range(101):
            self.finished.emit(i)
            time.sleep(0.1)