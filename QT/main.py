import sys
import os
from PyQt5 import QtWidgets
from lib.YouViewer import Ui_MainWindow
from lib.AuthDialog import AuthDialog
from PyQt5 import QtCore
from PyQt5 import uic
from datetime import datetime
import re
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl

# pip install PyQtWebEngine
# form_class = uic.loadUiType('C:/Users/cuzai/Desktop/Web_Crawling/pythonStudy/QT/ui/you_Viewer_v1.0.ui')[0]

class Main(QtWidgets.QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()

        # 초기화
        self.setupUi(self)

        # 초기 화면 잠금
        self.initAuthLock()
        self.setWindowTitle("Youtube Downloader")
        self.plainTextEdit.setReadOnly(True)
        self.pathTextEdit.setReadOnly(True)

        # 시그널 초기화
        self.initSignal()

        # 로그인 관련 변수 선언
        self.userID = None
        self.userpwd = None

        # 재생여부
        self.isPlaying = False



    # 기본 ui 비활성화
    def initAuthLock(self) :
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamComboBox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg("인증 안됨")

    # 기본 ui 활성화
    def initAuthActive(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamComboBox.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg("인증 완료")


    def showStatusMsg(self, msg) :
        self.statusbar.showMessage(msg)

    def initSignal(self) :
        self.loginButton.clicked.connect(self.authCheck)
        self.previewButton.clicked.connect(self.loadURL)
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)    # 종료 버튼

        self.webEngineView.loadProgress.connect(self.showProgressBrowserLoading)

    @pyqtSlot()
    def authCheck(self):
        dlg = AuthDialog()
        dlg.exec_()
        self.userID = dlg.user_id
        self.userpwd = dlg.user_pwd

        if True :
            self.initAuthActive()
            self.loginButton.setText("인증완료")
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setFocus()

            self.appendLogMsg("log in succeded")

        else :
            QtWidgets.QMessageBox.about(self, "인증오류", "아이디 또는 비밀번호 인증 오류")

        # print("ID : {}, PWD : {}".format(self.userID, self.userpwd))

    def loadURL(self):
        url = self.urlTextEdit.text().strip()
        v = re.compile('^https://www.youtube.com/?')
        if self.isPlaying :
            pass
        else :
            # if v.match(url) is not None :

            self.appendLogMsg('play click')
            self.webEngineView.load(QUrl(url))
            self.showStatusMsg(url + '재생중')
            self.previewButton.setText('중지')
            self.isPlaying = True
            self.startButton.setEnabled(True)
            # else :
            #     QtWidgets.QMessageBox.about(self, "오류", "제대로 된 주소를 넣어라")
            #     self.urlTextEdit.clear()
            #     self.urlTextEdit.setFocus(True)


    def appendLogMsg(self, act):
        now = datetime.now()
        nowDateTime = now.strftime('%Y%m%d %H-%M-%S')
        app_msg = self.userID + " : " + act + '- (' + nowDateTime + ')'
        self.plainTextEdit.appendPlainText(app_msg) # insertPlainText : 줄바꿈 하지 않음. set : 지우고 처음부터 써줌

        # 활동 로그 저장(또는 DB 사용 추천
        fileName = datetime.now().strftime('%Y%m%d') + 'log.txt'
        filePath = os.path.join(os.getcwd(),'log', fileName)
        with open(filePath, 'a') as f :
            f.write(app_msg + '\n')

    @ pyqtSlot(int)
    def showProgressBrowserLoading(self, v):
        self.progressBar.setValue(v)


if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()