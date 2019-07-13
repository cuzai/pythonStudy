import sys
from PyQt5 import QtWidgets

class AuthDialog(QtWidgets.QDialog) :
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.user_id = None
        self.user_pwd = None


    def setupUI(self):
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle("Sign in")
        self.setFixedSize(300, 100)

        label1 = QtWidgets.QLabel("ID : ")
        label2 = QtWidgets.QLabel("Password : ")

        self.lineEdit1 = QtWidgets.QLineEdit()
        self.lineEdit2 = QtWidgets.QLineEdit()

        self.lineEdit2.setEchoMode(QtWidgets.QLineEdit().Password)  # 비밀번호 별표표시

        self.pushButton = QtWidgets.QPushButton("Log in")
        self.pushButton.clicked.connect(self.submitLogin)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)

        self.setLayout(layout)

    def submitLogin(self):
        self.user_id = self.lineEdit1.text()
        self.user_pwd = self.lineEdit2.text()
        # print(self.user_id, self.user_ pwd)

        if self.user_id == None or self.user_id == "" or not self.user_id :
            QtWidgets.QMessageBox.about(self, "인증 오류", "ID를 입력하세요")
            self.lineEdit1.setFocus(True)
            return

        if not self.user_pwd:
            QtWidgets.QMessageBox.about(self, "인증 오류", "비밀번호를 입력하세요")
            self.lineEdit2.setFocus(True)
            return

        self.close()

if __name__ == '__main__' :
    app = QtWidgets.QApplication(sys.argv)
    loginDialog = AuthDialog()
    loginDialog.show()
    app.exec_()