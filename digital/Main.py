import atexit
import datetime
import sqlite3

from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot

from libs.KoreakClick.KoreanClick import KoreanClick
from libs.KoreakClick.KcClicked import KcClicked
from libs.Nielsen.Nielsen_Press import Nielsen_Press
from libs.Nielsen.NClicked import NClicked
from libs.DailyTrends.DailyTrends import DailyTrends
from libs.DailyTrends.DtClicked import DtClicked
from libs.Rankey.RankeyTitle import RankeyTitle
from libs.Rankey.RankeyImg import RankeyImg

from ui.myUi import Ui_MainWindow
import sys
import logging

form_class = uic.loadUiType('./ui/main.ui')[0]
class Main(QtWidgets.QMainWindow, Ui_MainWindow) :
    kc_idx = 0
    dt_idx = 0
    n_Press_idx = 0

    def __init__(self):
        try :
            super().__init__()

            # initialize ui
            self.setupUi(self)
            # ranky rank img set
            # self.rk1st.setPixmap(QtGui.QPixmap("./res/rankey/rank1.png"))
            # self.rk2nd.setPixmap(QtGui.QPixmap("./res/rankey/rank2.png"))
            # self.rk3rd.setPixmap(QtGui.QPixmap("./res/rankey/rank3.png"))

            # # rankey
            # self.rkt = RankeyTitle()
            # self.rkt.finished.connect(self.rkSetTitle)
            # self.rkt.start()
            #
            # self.rki = RankeyImg()
            # self.rki.finished.connect(self.rkSetImg)
            # self.rki.start()

            # Daily Trends
            self.dailyTrend = DailyTrends(5)
            self.dailyTrend.finished.connect(self.dtSetTitle)
            self.dailyTrend.start()

            # Korean Click
            self.koreanClick = KoreanClick(5)
            self.koreanClick.finished.connect(self.set_Kc_Title)
            self.koreanClick.start()

            # Nielsen
            self.nielsen_Press = Nielsen_Press(5)
            self.nielsen_Press.finished.connect(self.set_N_Press_Title)
            self.nielsen_Press.start()

            # make db
            self.conn = sqlite3.connect('db/userData.db')
            now = datetime.datetime.now()
            self.nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
            self.c = self.conn.cursor()
            self.c.execute("CREATE TABLE IF NOT EXISTS dailyTrends(title text, regdate text)")
            self.c.execute("CREATE TABLE IF NOT EXISTS koreanClick(title text, regdate text)")
            self.c.execute("CREATE TABLE IF NOT EXISTS nielsen(title text, regdate text)")

        except Exception as e :
            logging.info("__init__ : {}".format(e))
            pass

# ---------------------------------------------------------------------------------
    # rankey.com
    # @pyqtSlot(str, str, str, str)
    # def rkSetTitle(self, title, name1, name2, name3):
    #     try :
    #         self.rk_title.setText(title)
    #         self.rk_img_name1.setText(name1)
    #         self.rk_img_name2.setText(name2)
    #         self.rk_img_name3.setText(name3)
    #     except Exception as e :
    #         logging.info("def rkSetTitle ", e)
    #
    # @pyqtSlot(str)
    # def rkSetImg(self, n):
    #     try :
    #         rk_img_Li = [self.rk_img1, self.rk_img2, self.rk_img3]
    #         fileName = os.getcwd() + '/res/rankey/img' + n + '.png'
    #         rk_img_Li[int(n)-1].setPixmap(QtGui.QPixmap(fileName))
    #     except Exception as e:
    #         logging.info("def rkSetImg", e)
    #

    # Daily Trends
    @pyqtSlot(str, str)
    def dtSetTitle(self, title, href):
        logging.info("dtSetTitle")
        try :
            self.dtLi = [self.dailyTrend_Title1, self.dailyTrend_Title2, self.dailyTrend_Title3, self.dailyTrend_Title4, self.dailyTrend_Title5]
            self.dtLi[self.dt_idx].setText(title)

            # if in db, make the title grey
            if self.c.execute("SELECT title FROM dailyTrends WHERE title = ?", (title,)).fetchone() :
                self.dtLi[self.dt_idx].setStyleSheet('color:grey; text-align:left; background:transparent;')

            # link link
            self.dtLi[self.dt_idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            idx = self.dt_idx
            self.dtLi[self.dt_idx].clicked.connect(lambda : self.dtClicked(href, title, idx))
            self.dt_idx += 1

        except Exception as e :
            logging.info("dtSetTitle : {}".format(e))
            pass

    def dtClicked(self, href, title, idx):
        self.dc = DtClicked(href)
        self.dc.start()

        # insert into the db only when there is no same thing
        if self.c.execute("SELECT title FROM dailyTrends WHERE title = ?", (title,)).fetchone() is None:
            self.c.execute("INSERT INTO dailyTrends VALUES(?, ?)", (title, self.nowDateTime,))
            self.conn.commit()
            self.dtLi[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')

    # korean click
    @pyqtSlot(str, str, str)
    def set_Kc_Title(self, title, href, date):
        logging.info("set_Kc_Title")
        try :
            self.kc_Li = [
                self.kc_Internet_Title1, self.kc_Internet_Title2, self.kc_Internet_Title3, self.kc_Internet_Title4, self.kc_Internet_Title5,
                self.kc_Topic_Title1, self.kc_Topic_Title2, self.kc_Topic_Title3, self.kc_Topic_Title4,self.kc_Topic_Title5,
                self.kc_BW_title1, self.kc_BW_title2, self.kc_BW_title3, self.kc_BW_title4, self.kc_BW_title5,
                self.kc_DN_title1, self.kc_DN_title2, self.kc_DN_title3, self.kc_DN_title4, self.kc_DN_title5
            ]
            self.kc_Date_Li = [
                self.kc_Internet_Date1, self.kc_Internet_Date2, self.kc_Internet_Date3, self.kc_Internet_Date4, self.kc_Internet_Date5,
                self.kc_Topic_Date1, self.kc_Topic_Date2, self.kc_Topic_Date3, self.kc_Topic_Date4, self.kc_Topic_Date5,
                self.kc_BuzzWord_Date1, self.kc_BuzzWord_Date2, self.kc_BuzzWord_Date3, self.kc_BuzzWord_Date4, self.kc_BuzzWord_Date5,
                self.kc_Digital_Date1, self.kc_Digital_Date2, self.kc_Digital_Date3, self.kc_Digital_Date4, self.kc_Digital_Date5
               ]

            self.kc_Li[self.kc_idx].setText(title)
            self.kc_Date_Li[self.kc_idx].setText(date)

            # if in db, make the title grey
            if self.c.execute("SELECT title FROM koreanClick WHERE title = ?", (title,)).fetchone() :
                self.kc_Li[self.kc_idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                self.kc_Date_Li[self.kc_idx].setStyleSheet('color:grey')

            self.kc_Li[self.kc_idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            idx = self.kc_idx
            self.kc_Li[self.kc_idx].clicked.connect(lambda: self.kcClicked(href, title, idx))
            self.kc_idx += 1
        except Exception as e :
            logging.info(">>>>> def kcSet_Title {}".format(e))
            pass

    def kcClicked(self, href, title, idx):
        self.kced = KcClicked(href)
        self.kced.start()

        try :
            # insert into the db only when there is no same thing
            if self.c.execute("SELECT title FROM koreanClick WHERE title = ?", (title,)).fetchone() is None:
                self.c.execute("INSERT INTO koreanClick VALUES(?, ?)", (title, self.nowDateTime,))
                self.conn.commit()
                self.kc_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                self.kc_Date_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
        except Exception as e:
            logging.info(">>>>> def kcClicked error : {}".format(e))


    # nielsen
    @pyqtSlot(str, str, str)
    def set_N_Press_Title(self, title, href, date):
        logging.info("set_N_Press_Title")
        try:
            self.n_Press_TitleLi = [self.nielsen_Press_title1, self.nielsen_Press_title2, self.nielsen_Press_title3, self.nielsen_Press_title4, self.nielsen_Press_title5]
            self.n_Press_DateLi = [self.Nielsen_Press_Date1, self.Nielsen_Press_Date2, self.Nielsen_Press_Date3, self.Nielsen_Press_Date4, self.Nielsen_Press_Date5]

            self.n_Press_TitleLi[self.n_Press_idx].setText(title)
            self.n_Press_DateLi[self.n_Press_idx].setText(date)

            self.n_Press_TitleLi[self.n_Press_idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.n_Press_TitleLi[self.n_Press_idx].clicked.connect(lambda: self.nClicked(href))
            self.n_Press_idx += 1

        except Exception as e :
            logging.info(">>>>> set_N_Press_Title : {}".format(e))
            pass

    def nClicked(self, href):
        self.nced = NClicked(href)
        self.nced.start()

if (__name__ == "__main__") :
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


