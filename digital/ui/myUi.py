# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1326, 692)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color : white")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color : white")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(31, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("QScrollArea {\n"
"background-color : white;\n"
"border: none;\n"
"\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -755, 1256, 1486))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 30, 30)
        self.gridLayout_2.setVerticalSpacing(42)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_10 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        self.groupBox_10.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_10.setStyleSheet("QGroupBox{\n"
"    border: 0px solid black;\n"
"    margin-top: 1em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -20px;\n"
"    left: 20px;\n"
"}")
        self.groupBox_10.setTitle("")
        self.groupBox_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_10)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox_10)
        self.label_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout_2.addWidget(self.groupBox_10, 1, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_8.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setStyleSheet("QGroupBox{\n"
"    border: 1px solid black;\n"
"    margin-top: 1.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -15px;\n"
"    left: 20px;\n"
"}")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_11.setContentsMargins(-1, 40, -1, -1)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setStyleSheet("QGroupBox{\n"
"    border: 0px solid rgb(220, 220, 220);\n"
"    margin-top: 0em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: 0px;\n"
"    left: 20px;\n"
"}")
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_9.setContentsMargins(20, 20, -1, -1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.kc_Internet_Date1_2 = QtWidgets.QTabWidget(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kc_Internet_Date1_2.sizePolicy().hasHeightForWidth())
        self.kc_Internet_Date1_2.setSizePolicy(sizePolicy)
        self.kc_Internet_Date1_2.setMinimumSize(QtCore.QSize(0, 300))
        self.kc_Internet_Date1_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.kc_Internet_Date1_2.setFont(font)
        self.kc_Internet_Date1_2.setStyleSheet("background : transparent")
        self.kc_Internet_Date1_2.setObjectName("kc_Internet_Date1_2")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_14)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.kc_Internet_Date5 = QtWidgets.QLabel(self.tab_14)
        self.kc_Internet_Date5.setText("")
        self.kc_Internet_Date5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Internet_Date5.setObjectName("kc_Internet_Date5")
        self.gridLayout_8.addWidget(self.kc_Internet_Date5, 4, 1, 1, 1)
        self.kc_Internet_Date3 = QtWidgets.QLabel(self.tab_14)
        self.kc_Internet_Date3.setText("")
        self.kc_Internet_Date3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Internet_Date3.setObjectName("kc_Internet_Date3")
        self.gridLayout_8.addWidget(self.kc_Internet_Date3, 2, 1, 1, 1)
        self.kc_Internet_Title4 = QtWidgets.QPushButton(self.tab_14)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_Internet_Title4.setFont(font)
        self.kc_Internet_Title4.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_Internet_Title4.setText("")
        self.kc_Internet_Title4.setObjectName("kc_Internet_Title4")
        self.gridLayout_8.addWidget(self.kc_Internet_Title4, 3, 0, 1, 1)
        self.kc_Internet_Date2 = QtWidgets.QLabel(self.tab_14)
        self.kc_Internet_Date2.setText("")
        self.kc_Internet_Date2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Internet_Date2.setObjectName("kc_Internet_Date2")
        self.gridLayout_8.addWidget(self.kc_Internet_Date2, 1, 1, 1, 1)
        self.kc_Internet_Date4 = QtWidgets.QLabel(self.tab_14)
        self.kc_Internet_Date4.setText("")
        self.kc_Internet_Date4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Internet_Date4.setObjectName("kc_Internet_Date4")
        self.gridLayout_8.addWidget(self.kc_Internet_Date4, 3, 1, 1, 1)
        self.kc_Internet_Title2 = QtWidgets.QPushButton(self.tab_14)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_Internet_Title2.setFont(font)
        self.kc_Internet_Title2.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_Internet_Title2.setText("")
        self.kc_Internet_Title2.setObjectName("kc_Internet_Title2")
        self.gridLayout_8.addWidget(self.kc_Internet_Title2, 1, 0, 1, 1)
        self.kc_Internet_Title1 = QtWidgets.QPushButton(self.tab_14)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_Internet_Title1.setFont(font)
        self.kc_Internet_Title1.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_Internet_Title1.setText("")
        self.kc_Internet_Title1.setObjectName("kc_Internet_Title1")
        self.gridLayout_8.addWidget(self.kc_Internet_Title1, 0, 0, 1, 1)
        self.kc_Internet_Title5 = QtWidgets.QPushButton(self.tab_14)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_Internet_Title5.setFont(font)
        self.kc_Internet_Title5.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_Internet_Title5.setText("")
        self.kc_Internet_Title5.setObjectName("kc_Internet_Title5")
        self.gridLayout_8.addWidget(self.kc_Internet_Title5, 4, 0, 1, 1)
        self.kc_Internet_Title3 = QtWidgets.QPushButton(self.tab_14)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_Internet_Title3.setFont(font)
        self.kc_Internet_Title3.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_Internet_Title3.setObjectName("kc_Internet_Title3")
        self.gridLayout_8.addWidget(self.kc_Internet_Title3, 2, 0, 1, 1)
        self.kc_Internet_Date1 = QtWidgets.QLabel(self.tab_14)
        self.kc_Internet_Date1.setText("")
        self.kc_Internet_Date1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Internet_Date1.setObjectName("kc_Internet_Date1")
        self.gridLayout_8.addWidget(self.kc_Internet_Date1, 0, 1, 1, 1)
        self.kc_Internet_Date1_2.addTab(self.tab_14, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_15)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.kc_Topic_Date1 = QtWidgets.QLabel(self.tab_15)
        self.kc_Topic_Date1.setText("")
        self.kc_Topic_Date1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Topic_Date1.setObjectName("kc_Topic_Date1")
        self.gridLayout_13.addWidget(self.kc_Topic_Date1, 0, 1, 1, 1)
        self.kc_Topic_Title1 = QtWidgets.QPushButton(self.tab_15)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_Topic_Title1.setFont(font)
        self.kc_Topic_Title1.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_Topic_Title1.setText("")
        self.kc_Topic_Title1.setObjectName("kc_Topic_Title1")
        self.gridLayout_13.addWidget(self.kc_Topic_Title1, 0, 0, 1, 1)
        self.kc_Topic_Title3 = QtWidgets.QPushButton(self.tab_15)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_Topic_Title3.setFont(font)
        self.kc_Topic_Title3.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_Topic_Title3.setObjectName("kc_Topic_Title3")
        self.gridLayout_13.addWidget(self.kc_Topic_Title3, 2, 0, 1, 1)
        self.kc_Topic_Title4 = QtWidgets.QPushButton(self.tab_15)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_Topic_Title4.setFont(font)
        self.kc_Topic_Title4.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_Topic_Title4.setText("")
        self.kc_Topic_Title4.setObjectName("kc_Topic_Title4")
        self.gridLayout_13.addWidget(self.kc_Topic_Title4, 3, 0, 1, 1)
        self.kc_Topic_Title2 = QtWidgets.QPushButton(self.tab_15)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_Topic_Title2.setFont(font)
        self.kc_Topic_Title2.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_Topic_Title2.setText("")
        self.kc_Topic_Title2.setObjectName("kc_Topic_Title2")
        self.gridLayout_13.addWidget(self.kc_Topic_Title2, 1, 0, 1, 1)
        self.kc_Topic_Title5 = QtWidgets.QPushButton(self.tab_15)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_Topic_Title5.setFont(font)
        self.kc_Topic_Title5.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_Topic_Title5.setText("")
        self.kc_Topic_Title5.setObjectName("kc_Topic_Title5")
        self.gridLayout_13.addWidget(self.kc_Topic_Title5, 4, 0, 1, 1)
        self.kc_Topic_Date2 = QtWidgets.QLabel(self.tab_15)
        self.kc_Topic_Date2.setText("")
        self.kc_Topic_Date2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Topic_Date2.setObjectName("kc_Topic_Date2")
        self.gridLayout_13.addWidget(self.kc_Topic_Date2, 1, 1, 1, 1)
        self.kc_Topic_Date3 = QtWidgets.QLabel(self.tab_15)
        self.kc_Topic_Date3.setText("")
        self.kc_Topic_Date3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Topic_Date3.setObjectName("kc_Topic_Date3")
        self.gridLayout_13.addWidget(self.kc_Topic_Date3, 2, 1, 1, 1)
        self.kc_Topic_Date4 = QtWidgets.QLabel(self.tab_15)
        self.kc_Topic_Date4.setText("")
        self.kc_Topic_Date4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Topic_Date4.setObjectName("kc_Topic_Date4")
        self.gridLayout_13.addWidget(self.kc_Topic_Date4, 3, 1, 1, 1)
        self.kc_Topic_Date5 = QtWidgets.QLabel(self.tab_15)
        self.kc_Topic_Date5.setText("")
        self.kc_Topic_Date5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Topic_Date5.setObjectName("kc_Topic_Date5")
        self.gridLayout_13.addWidget(self.kc_Topic_Date5, 4, 1, 1, 1)
        self.kc_Internet_Date1_2.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_16)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.kc_DN_title4 = QtWidgets.QPushButton(self.tab_16)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_DN_title4.setFont(font)
        self.kc_DN_title4.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_DN_title4.setText("")
        self.kc_DN_title4.setObjectName("kc_DN_title4")
        self.gridLayout_14.addWidget(self.kc_DN_title4, 3, 0, 1, 1)
        self.kc_DN_title1 = QtWidgets.QPushButton(self.tab_16)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_DN_title1.setFont(font)
        self.kc_DN_title1.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_DN_title1.setText("")
        self.kc_DN_title1.setObjectName("kc_DN_title1")
        self.gridLayout_14.addWidget(self.kc_DN_title1, 0, 0, 1, 1)
        self.kc_DN_title2 = QtWidgets.QPushButton(self.tab_16)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_DN_title2.setFont(font)
        self.kc_DN_title2.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_DN_title2.setText("")
        self.kc_DN_title2.setObjectName("kc_DN_title2")
        self.gridLayout_14.addWidget(self.kc_DN_title2, 1, 0, 1, 1)
        self.kc_DN_title5 = QtWidgets.QPushButton(self.tab_16)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_DN_title5.setFont(font)
        self.kc_DN_title5.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_DN_title5.setText("")
        self.kc_DN_title5.setObjectName("kc_DN_title5")
        self.gridLayout_14.addWidget(self.kc_DN_title5, 4, 0, 1, 1)
        self.kc_DN_title3 = QtWidgets.QPushButton(self.tab_16)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_DN_title3.setFont(font)
        self.kc_DN_title3.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_DN_title3.setObjectName("kc_DN_title3")
        self.gridLayout_14.addWidget(self.kc_DN_title3, 2, 0, 1, 1)
        self.kc_Digital_Date1 = QtWidgets.QLabel(self.tab_16)
        self.kc_Digital_Date1.setText("")
        self.kc_Digital_Date1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Digital_Date1.setObjectName("kc_Digital_Date1")
        self.gridLayout_14.addWidget(self.kc_Digital_Date1, 0, 1, 1, 1)
        self.kc_Digital_Date2 = QtWidgets.QLabel(self.tab_16)
        self.kc_Digital_Date2.setText("")
        self.kc_Digital_Date2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Digital_Date2.setObjectName("kc_Digital_Date2")
        self.gridLayout_14.addWidget(self.kc_Digital_Date2, 1, 1, 1, 1)
        self.kc_Digital_Date3 = QtWidgets.QLabel(self.tab_16)
        self.kc_Digital_Date3.setText("")
        self.kc_Digital_Date3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Digital_Date3.setObjectName("kc_Digital_Date3")
        self.gridLayout_14.addWidget(self.kc_Digital_Date3, 2, 1, 1, 1)
        self.kc_Digital_Date4 = QtWidgets.QLabel(self.tab_16)
        self.kc_Digital_Date4.setText("")
        self.kc_Digital_Date4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Digital_Date4.setObjectName("kc_Digital_Date4")
        self.gridLayout_14.addWidget(self.kc_Digital_Date4, 3, 1, 1, 1)
        self.kc_Digital_Date5 = QtWidgets.QLabel(self.tab_16)
        self.kc_Digital_Date5.setText("")
        self.kc_Digital_Date5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Digital_Date5.setObjectName("kc_Digital_Date5")
        self.gridLayout_14.addWidget(self.kc_Digital_Date5, 4, 1, 1, 1)
        self.kc_Internet_Date1_2.addTab(self.tab_16, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab_17)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.kc_BW_title5 = QtWidgets.QPushButton(self.tab_17)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_BW_title5.setFont(font)
        self.kc_BW_title5.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_BW_title5.setText("")
        self.kc_BW_title5.setObjectName("kc_BW_title5")
        self.gridLayout_15.addWidget(self.kc_BW_title5, 4, 0, 1, 1)
        self.kc_BW_title1 = QtWidgets.QPushButton(self.tab_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kc_BW_title1.sizePolicy().hasHeightForWidth())
        self.kc_BW_title1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_BW_title1.setFont(font)
        self.kc_BW_title1.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_BW_title1.setText("")
        self.kc_BW_title1.setObjectName("kc_BW_title1")
        self.gridLayout_15.addWidget(self.kc_BW_title1, 0, 0, 1, 1)
        self.kc_BW_title4 = QtWidgets.QPushButton(self.tab_17)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_BW_title4.setFont(font)
        self.kc_BW_title4.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_BW_title4.setText("")
        self.kc_BW_title4.setObjectName("kc_BW_title4")
        self.gridLayout_15.addWidget(self.kc_BW_title4, 3, 0, 1, 1)
        self.kc_BW_title2 = QtWidgets.QPushButton(self.tab_17)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_BW_title2.setFont(font)
        self.kc_BW_title2.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_BW_title2.setText("")
        self.kc_BW_title2.setObjectName("kc_BW_title2")
        self.gridLayout_15.addWidget(self.kc_BW_title2, 1, 0, 1, 1)
        self.kc_BW_title3 = QtWidgets.QPushButton(self.tab_17)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.kc_BW_title3.setFont(font)
        self.kc_BW_title3.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.kc_BW_title3.setObjectName("kc_BW_title3")
        self.gridLayout_15.addWidget(self.kc_BW_title3, 2, 0, 1, 1)
        self.kc_BuzzWord_Date1 = QtWidgets.QLabel(self.tab_17)
        self.kc_BuzzWord_Date1.setText("")
        self.kc_BuzzWord_Date1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_BuzzWord_Date1.setObjectName("kc_BuzzWord_Date1")
        self.gridLayout_15.addWidget(self.kc_BuzzWord_Date1, 0, 1, 1, 1)
        self.kc_BuzzWord_Date2 = QtWidgets.QLabel(self.tab_17)
        self.kc_BuzzWord_Date2.setText("")
        self.kc_BuzzWord_Date2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_BuzzWord_Date2.setObjectName("kc_BuzzWord_Date2")
        self.gridLayout_15.addWidget(self.kc_BuzzWord_Date2, 1, 1, 1, 1)
        self.kc_BuzzWord_Date3 = QtWidgets.QLabel(self.tab_17)
        self.kc_BuzzWord_Date3.setText("")
        self.kc_BuzzWord_Date3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_BuzzWord_Date3.setObjectName("kc_BuzzWord_Date3")
        self.gridLayout_15.addWidget(self.kc_BuzzWord_Date3, 2, 1, 1, 1)
        self.kc_BuzzWord_Date4 = QtWidgets.QLabel(self.tab_17)
        self.kc_BuzzWord_Date4.setText("")
        self.kc_BuzzWord_Date4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_BuzzWord_Date4.setObjectName("kc_BuzzWord_Date4")
        self.gridLayout_15.addWidget(self.kc_BuzzWord_Date4, 3, 1, 1, 1)
        self.kc_BuzzWord_Date5 = QtWidgets.QLabel(self.tab_17)
        self.kc_BuzzWord_Date5.setText("")
        self.kc_BuzzWord_Date5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_BuzzWord_Date5.setObjectName("kc_BuzzWord_Date5")
        self.gridLayout_15.addWidget(self.kc_BuzzWord_Date5, 4, 1, 1, 1)
        self.kc_Internet_Date1_2.addTab(self.tab_17, "")
        self.gridLayout_9.addWidget(self.kc_Internet_Date1_2, 1, 0, 1, 1)
        self.kc_Internet_Date1_3 = QtWidgets.QLabel(self.groupBox_9)
        self.kc_Internet_Date1_3.setText("")
        self.kc_Internet_Date1_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.kc_Internet_Date1_3.setObjectName("kc_Internet_Date1_3")
        self.gridLayout_9.addWidget(self.kc_Internet_Date1_3, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_9, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_8, 3, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(900, 800))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"    border: 1px solid black;\n"
"    margin-top: 1.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -15px;\n"
"    left: 20px;\n"
"}")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setContentsMargins(20, 50, -1, -1)
        self.gridLayout_4.setHorizontalSpacing(9)
        self.gridLayout_4.setVerticalSpacing(34)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 300))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"    border: 0px solid rgb(220, 220, 220);\n"
"    margin-top: 0em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: 0px;\n"
"    left: 20px;\n"
"}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_12.setContentsMargins(40, 40, -1, -1)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.dailyTrend_Title4 = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.dailyTrend_Title4.setFont(font)
        self.dailyTrend_Title4.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.dailyTrend_Title4.setText("")
        self.dailyTrend_Title4.setObjectName("dailyTrend_Title4")
        self.gridLayout_12.addWidget(self.dailyTrend_Title4, 3, 0, 1, 1)
        self.dailyTrend_Title2 = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.dailyTrend_Title2.setFont(font)
        self.dailyTrend_Title2.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.dailyTrend_Title2.setText("")
        self.dailyTrend_Title2.setObjectName("dailyTrend_Title2")
        self.gridLayout_12.addWidget(self.dailyTrend_Title2, 1, 0, 1, 1)
        self.dailyTrend_Title5 = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.dailyTrend_Title5.setFont(font)
        self.dailyTrend_Title5.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.dailyTrend_Title5.setText("")
        self.dailyTrend_Title5.setObjectName("dailyTrend_Title5")
        self.gridLayout_12.addWidget(self.dailyTrend_Title5, 4, 0, 1, 1)
        self.dailyTrend_Title1 = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.dailyTrend_Title1.setFont(font)
        self.dailyTrend_Title1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.dailyTrend_Title1.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.dailyTrend_Title1.setText("")
        self.dailyTrend_Title1.setObjectName("dailyTrend_Title1")
        self.gridLayout_12.addWidget(self.dailyTrend_Title1, 0, 0, 1, 1)
        self.dailyTrend_Title3 = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.dailyTrend_Title3.setFont(font)
        self.dailyTrend_Title3.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.dailyTrend_Title3.setObjectName("dailyTrend_Title3")
        self.gridLayout_12.addWidget(self.dailyTrend_Title3, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_12.addWidget(self.label_3, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("QGroupBox{\n"
"    border: 0px solid rgb(220, 220, 220);\n"
"    margin-top: 0em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: 0px;\n"
"    left: 20px;\n"
"}")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setContentsMargins(20, 40, -1, -1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_3.sizePolicy().hasHeightForWidth())
        self.tabWidget_3.setSizePolicy(sizePolicy)
        self.tabWidget_3.setMinimumSize(QtCore.QSize(0, 300))
        self.tabWidget_3.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.tabWidget_3.setFont(font)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_12)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.nielsen_Press_title5 = QtWidgets.QPushButton(self.tab_12)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.nielsen_Press_title5.setFont(font)
        self.nielsen_Press_title5.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.nielsen_Press_title5.setText("")
        self.nielsen_Press_title5.setObjectName("nielsen_Press_title5")
        self.gridLayout_5.addWidget(self.nielsen_Press_title5, 4, 0, 1, 1)
        self.nielsen_Press_title1 = QtWidgets.QPushButton(self.tab_12)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.nielsen_Press_title1.setFont(font)
        self.nielsen_Press_title1.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.nielsen_Press_title1.setText("")
        self.nielsen_Press_title1.setObjectName("nielsen_Press_title1")
        self.gridLayout_5.addWidget(self.nielsen_Press_title1, 0, 0, 1, 1)
        self.nielsen_Press_title4 = QtWidgets.QPushButton(self.tab_12)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.nielsen_Press_title4.setFont(font)
        self.nielsen_Press_title4.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.nielsen_Press_title4.setText("")
        self.nielsen_Press_title4.setObjectName("nielsen_Press_title4")
        self.gridLayout_5.addWidget(self.nielsen_Press_title4, 3, 0, 1, 1)
        self.Nielsen_Press_Date4 = QtWidgets.QLabel(self.tab_12)
        self.Nielsen_Press_Date4.setText("")
        self.Nielsen_Press_Date4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.Nielsen_Press_Date4.setObjectName("Nielsen_Press_Date4")
        self.gridLayout_5.addWidget(self.Nielsen_Press_Date4, 3, 1, 1, 1)
        self.Nielsen_Press_Date1 = QtWidgets.QLabel(self.tab_12)
        self.Nielsen_Press_Date1.setText("")
        self.Nielsen_Press_Date1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.Nielsen_Press_Date1.setObjectName("Nielsen_Press_Date1")
        self.gridLayout_5.addWidget(self.Nielsen_Press_Date1, 0, 1, 1, 1)
        self.Nielsen_Press_Date3 = QtWidgets.QLabel(self.tab_12)
        self.Nielsen_Press_Date3.setText("")
        self.Nielsen_Press_Date3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.Nielsen_Press_Date3.setObjectName("Nielsen_Press_Date3")
        self.gridLayout_5.addWidget(self.Nielsen_Press_Date3, 2, 1, 1, 1)
        self.nielsen_Press_title3 = QtWidgets.QPushButton(self.tab_12)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.nielsen_Press_title3.setFont(font)
        self.nielsen_Press_title3.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.nielsen_Press_title3.setObjectName("nielsen_Press_title3")
        self.gridLayout_5.addWidget(self.nielsen_Press_title3, 2, 0, 1, 1)
        self.Nielsen_Press_Date2 = QtWidgets.QLabel(self.tab_12)
        self.Nielsen_Press_Date2.setText("")
        self.Nielsen_Press_Date2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.Nielsen_Press_Date2.setObjectName("Nielsen_Press_Date2")
        self.gridLayout_5.addWidget(self.Nielsen_Press_Date2, 1, 1, 1, 1)
        self.Nielsen_Press_Date5 = QtWidgets.QLabel(self.tab_12)
        self.Nielsen_Press_Date5.setText("")
        self.Nielsen_Press_Date5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.Nielsen_Press_Date5.setObjectName("Nielsen_Press_Date5")
        self.gridLayout_5.addWidget(self.Nielsen_Press_Date5, 4, 1, 1, 1)
        self.nielsen_Press_title2 = QtWidgets.QPushButton(self.tab_12)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        self.nielsen_Press_title2.setFont(font)
        self.nielsen_Press_title2.setStyleSheet("text-align: left;\n"
"background: transparent;")
        self.nielsen_Press_title2.setText("")
        self.nielsen_Press_title2.setObjectName("nielsen_Press_title2")
        self.gridLayout_5.addWidget(self.nielsen_Press_title2, 1, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.tabWidget_3.addTab(self.tab_13, "")
        self.gridLayout_7.addWidget(self.tabWidget_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_6, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.kc_Internet_Date1_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Retail Tech Trends"))
        self.label_2.setText(_translate("MainWindow", "- 디지털 전략본부"))
        self.groupBox_8.setTitle(_translate("MainWindow", "커머스 트렌드"))
        self.groupBox_9.setTitle(_translate("MainWindow", "코리안 클릭"))
        self.kc_Internet_Title3.setText(_translate("MainWindow", "Loading..."))
        self.kc_Internet_Date1_2.setTabText(self.kc_Internet_Date1_2.indexOf(self.tab_14), _translate("MainWindow", "월간 인터넷 사용 동향"))
        self.kc_Topic_Title3.setText(_translate("MainWindow", "Loading..."))
        self.kc_Internet_Date1_2.setTabText(self.kc_Internet_Date1_2.indexOf(self.tab_15), _translate("MainWindow", "월간토픽"))
        self.kc_DN_title3.setText(_translate("MainWindow", "Loading..."))
        self.kc_Internet_Date1_2.setTabText(self.kc_Internet_Date1_2.indexOf(self.tab_16), _translate("MainWindow", "Digital Now"))
        self.kc_BW_title3.setText(_translate("MainWindow", "Loading..."))
        self.kc_Internet_Date1_2.setTabText(self.kc_Internet_Date1_2.indexOf(self.tab_17), _translate("MainWindow", "버즈워드 토픽"))
        self.groupBox_2.setTitle(_translate("MainWindow", "비즈니스 트렌드"))
        self.groupBox_3.setTitle(_translate("MainWindow", "데일리 트렌드"))
        self.dailyTrend_Title3.setText(_translate("MainWindow", "Loading..."))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_6.setTitle(_translate("MainWindow", "닐슨"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("MainWindow", "Insight"))
        self.nielsen_Press_title3.setText(_translate("MainWindow", "Loading..."))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), _translate("MainWindow", "Press"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), _translate("MainWindow", "Top10"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
