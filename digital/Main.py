import datetime
import sqlite3
import time

from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot

from libs.KoreakClick.KcClicked import KcClicked
from libs.KoreakClick.KoreanClick_BuzzWord import KoreanClick_BuzzWord
from libs.KoreakClick.KoreanClick_DigitalNow import KoreanClick_DigitalNow
from libs.KoreakClick.KoreanClick_Internet import KoreanClick_Internet
from libs.KoreakClick.KoreanClick_Topic import KoreanClick_Topic
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
    howMany = 5
    kc_internet_idx = 0
    kc_topic_idx = 0
    kc_digital_idx = 0
    kc_buzz_idx = 0

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
            self.dailyTrend.error.connect(self.myError)
            self.dailyTrend.finished.connect(self.dtSetTitle)
            self.dailyTrend.start()
            time.sleep(0.2)

            # Korean Click
            self.kc_Internet = KoreanClick_Internet(self.howMany)
            self.kc_Internet.finished.connect(self.set_Kc_Internet_Title)
            self.kc_Internet.error.connect(self.myError)
            self.kc_Internet.start()
            time.sleep(0.2)

            self.kc_Topic = KoreanClick_Topic(self.howMany)
            self.kc_Topic.finished.connect(self.set_Kc_Topic_Title)
            self.kc_Topic.error.connect(self.myError)
            self.kc_Topic.start()
            time.sleep(0.2)

            self.kc_Digital = KoreanClick_DigitalNow(self.howMany)
            self.kc_Digital.finished.connect(self.set_Kc_Digital_Title)
            self.kc_Digital.error.connect(self.myError)
            self.kc_Digital.start()
            time.sleep(0.2)

            self.kc_Buzz = KoreanClick_BuzzWord(self.howMany)
            self.kc_Buzz.finished.connect(self.set_Kc_Buzz_Title)
            self.kc_Buzz.error.connect(self.myError)
            self.kc_Buzz.start()
            time.sleep(0.2)

            # Nielsen
            self.nielsen_Press = Nielsen_Press(5)
            self.nielsen_Press.finished.connect(self.set_N_Press_Title)
            self.nielsen_Press.start()
            time.sleep(0.2)

            # make db
            self.conn = sqlite3.connect('db/userData.db')
            now = datetime.datetime.now()
            self.nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
            self.c = self.conn.cursor()
            self.c.execute("CREATE TABLE IF NOT EXISTS dailyTrends(title text, regdate text)")
            self.c.execute("CREATE TABLE IF NOT EXISTS koreanClick_Internet(title text, regdate text)")
            self.c.execute("CREATE TABLE IF NOT EXISTS koreanClick_Topic(title text, regdate text)")
            self.c.execute("CREATE TABLE IF NOT EXISTS koreanClick_Digital(title text, regdate text)")
            self.c.execute("CREATE TABLE IF NOT EXISTS koreanClick_Buzz(title text, regdate text)")
            self.c.execute("CREATE TABLE IF NOT EXISTS nielsen_Press(title text, regdate text)")

        except Exception as e :
            logging.info(">>>>> __init__ error : {}".format(e))
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
    @pyqtSlot(str, str, str)
    def dtSetTitle(self, title, href, date):
        try :
            self.dtLi = [self.dailyTrend_Title1, self.dailyTrend_Title2, self.dailyTrend_Title3, self.dailyTrend_Title4, self.dailyTrend_Title5]
            self.dt_Date_Li = [self.dailyTrend_Date1, self.dailyTrend_Date2, self.dailyTrend_Date3, self.dailyTrend_Date4, self.dailyTrend_Date5]

            self.dtLi[self.dt_idx].setText(title)
            self.dt_Date_Li[self.dt_idx].setText(date)

            # if in db, make the title grey
            if self.c.execute("SELECT title FROM dailyTrends WHERE title = ?", (title,)).fetchone() :
                self.dtLi[self.dt_idx].setStyleSheet('color:grey; text-align:left; background:transparent;')

            # link the link
            self.dtLi[self.dt_idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            idx = self.dt_idx
            self.dtLi[self.dt_idx].clicked.connect(lambda : self.dtClicked(href, title, idx))
            self.dt_idx += 1

        except Exception as e :
            logging.info(">>>>> def dtSetTitle error : {}".format(e))
            pass

    def dtClicked(self, href, title, idx):
        try :
            self.dc = DtClicked(href)
            self.dc.start()

            # insert into the db only when there is no same thing
            if self.c.execute("SELECT title FROM dailyTrends WHERE title = ?", (title,)).fetchone() is None:
                self.c.execute("INSERT INTO dailyTrends VALUES(?, ?)", (title, self.nowDateTime,))
                self.conn.commit()
                self.dtLi[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
        except Exception as e:
            logging.info(">>>>> def dtClicked error : {}".format(e))
            pass

    # korean click
    @pyqtSlot(str, str, str)
    def set_Kc_Internet_Title(self, title, href, date):
        logging.info("set_Kc_Title")
        try :
            self.kc_Internet_Li = [self.kc_Internet_Title1, self.kc_Internet_Title2, self.kc_Internet_Title3, self.kc_Internet_Title4, self.kc_Internet_Title5]
            self.kc_Internet_Date_Li = [self.kc_Internet_Date1, self.kc_Internet_Date2, self.kc_Internet_Date3, self.kc_Internet_Date4, self.kc_Internet_Date5]

            self.kc_Internet_Li[self.kc_internet_idx].setText(title)
            self.kc_Internet_Date_Li[self.kc_internet_idx].setText(date)

            # if in db, make the title grey
            if self.c.execute("SELECT title FROM koreanClick_Internet WHERE title = ?", (title,)).fetchone() :
                self.kc_Internet_Li[self.kc_internet_idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                self.kc_Internet_Date_Li[self.kc_internet_idx].setStyleSheet('color:grey')

            self.kc_Internet_Li[self.kc_internet_idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            idx = self.kc_internet_idx
            self.kc_Internet_Li[self.kc_internet_idx].clicked.connect(lambda: self.kcClicked(href, title, idx, "koreanClick_Internet"))
            self.kc_internet_idx += 1
        except Exception as e :
            logging.info(">>>>> def Set_kcInternet_Title error :  {}".format(e))
            pass

    def set_Kc_Topic_Title(self, title, href, date):
        logging.info("set_Kc_Topic_Title")
        try :
            self.kc_Topic_Li = [self.kc_Topic_Title1, self.kc_Topic_Title2, self.kc_Topic_Title3, self.kc_Topic_Title4,self.kc_Topic_Title5]
            self.kc_Topic_Date_Li = [self.kc_Topic_Date1, self.kc_Topic_Date2, self.kc_Topic_Date3, self.kc_Topic_Date4, self.kc_Topic_Date5]

            self.kc_Topic_Li[self.kc_topic_idx].setText(title)
            self.kc_Topic_Date_Li[self.kc_topic_idx].setText(date)

            # if in db, make the title grey
            if self.c.execute("SELECT title FROM koreanClick_Topic WHERE title = ?", (title,)).fetchone() :
                self.kc_Topic_Li[self.kc_topic_idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                self.kc_Topic_Date_Li[self.kc_topic_idx].setStyleSheet('color:grey')

            self.kc_Topic_Li[self.kc_topic_idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            idx = self.kc_topic_idx
            self.kc_Topic_Li[self.kc_topic_idx].clicked.connect(lambda: self.kcClicked(href, title, idx, "koreanClick_Topic"))
            self.kc_topic_idx += 1
        except Exception as e :
            logging.info(">>>>> def Set_kc_topic_Title error :  {}".format(e))
            pass

    def set_Kc_Digital_Title(self, title, href, date):
        logging.info("set_Kc_Digital_Title")
        try :
            self.kc_Digital_Li = [self.kc_DN_title1, self.kc_DN_title2, self.kc_DN_title3, self.kc_DN_title4, self.kc_DN_title5]
            self.kc_Digital_Date_Li = [self.kc_Digital_Date1, self.kc_Digital_Date2, self.kc_Digital_Date3, self.kc_Digital_Date4, self.kc_Digital_Date5]

            self.kc_Digital_Li[self.kc_digital_idx].setText(title)
            self.kc_Digital_Date_Li[self.kc_digital_idx].setText(date)

            # if in db, make the title grey
            if self.c.execute("SELECT title FROM koreanClick_Digital WHERE title = ?", (title,)).fetchone() :
                self.kc_Digital_Li[self.kc_digital_idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                self.kc_Digital_Date_Li[self.kc_digital_idx].setStyleSheet('color:grey')

            self.kc_Digital_Li[self.kc_digital_idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            idx = self.kc_digital_idx
            self.kc_Digital_Li[self.kc_digital_idx].clicked.connect(lambda: self.kcClicked(href, title, idx, "koreanClick_Digital"))
            self.kc_digital_idx += 1
        except Exception as e :
            logging.info(">>>>> def Set_kcDigital_Title error :  {}".format(e))
            pass

    def set_Kc_Buzz_Title(self, title, href, date):
        logging.info("set_Kc_Buzz_Title")
        try :
            self.kc_Buzz_Li = [self.kc_BW_title1, self.kc_BW_title2, self.kc_BW_title3, self.kc_BW_title4, self.kc_BW_title5]
            self.kc_Buzz_Date_Li = [self.kc_BuzzWord_Date1, self.kc_BuzzWord_Date2, self.kc_BuzzWord_Date3, self.kc_BuzzWord_Date4, self.kc_BuzzWord_Date5]

            self.kc_Buzz_Li[self.kc_buzz_idx].setText(title)
            self.kc_Buzz_Date_Li[self.kc_buzz_idx].setText(date)

            # if in db, make the title grey
            if self.c.execute("SELECT title FROM koreanClick_Buzz WHERE title = ?", (title,)).fetchone() :
                self.kc_Buzz_Li[self.kc_buzz_idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                self.kc_Buzz_Date_Li[self.kc_buzz_idx].setStyleSheet('color:grey')

            self.kc_Buzz_Li[self.kc_buzz_idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            idx = self.kc_buzz_idx
            self.kc_Buzz_Li[self.kc_buzz_idx].clicked.connect(lambda: self.kcClicked(href, title, idx, "koreanClick_Buzz"))
            self.kc_buzz_idx += 1

        except Exception as e :
            logging.info(">>>>> def Set_kcBuzz_Title error :  {}".format(e))
            pass

    def kcClicked(self, href, title, idx, name):
        self.kced = KcClicked(href)
        self.kced.start()

        try :
            # insert into the db only when there is no same thing
            if self.c.execute("SELECT title FROM "+ name +" WHERE title = ?", (title,)).fetchone() is None:
                self.c.execute("INSERT INTO " + name + " VALUES(?, ?)", (title, self.nowDateTime,))
                self.conn.commit()

                if name == 'koreanClick_Internet' :
                    self.kc_Internet_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                    self.kc_Internet_Date_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                elif name == 'koreanClick_Topic' :
                    self.kc_Topic_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                    self.kc_Topic_Date_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                elif name == 'koreanClick_Digital' :
                    self.kc_Digital_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                    self.kc_Digital_Date_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                elif name == 'koreanClick_Buzz' :
                    self.kc_Buzz_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                    self.kc_Buzz_Date_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')

        except Exception as e:
            logging.info(">>>>> def kcClicked error : {}".format(e))
            pass

    @pyqtSlot(str)
    def myError(self, name):
        if name == "koreanClick_Internet" :
            self.kc_Internet_Title3.setText("코리안클릭 웹사이트의 연결이 지연되고 있습니다.")
        elif name == "koreanClick_Topic" :
            self.kc_Topic_Title3.setText("코리안클릭 웹사이트의 연결이 지연되고 있습니다.")
        elif name == "koreanClick_Digital" :
            self.kc_DN_title3.setText("코리안클릭 웹사이트의 연결이 지연되고 있습니다.")
        elif name == 'koreanClick_Buzz' :
            self.kc_BW_title3.setText("코리안클릭 웹사이트의 연결이 지연되고 있습니다.")
        elif name == 'dailyTrend' :
            self.dailyTrend_Title3.setText("데일리트렌드 인터넷 연결이 지연되고 있습니다.")

    # nielsen
    @pyqtSlot(str, str, str)
    def set_N_Press_Title(self, title, href, date):
        logging.info("set_N_Press_Title")
        try:
            self.n_Press_TitleLi = [self.nielsen_Press_title1, self.nielsen_Press_title2, self.nielsen_Press_title3, self.nielsen_Press_title4, self.nielsen_Press_title5]
            self.n_Press_DateLi = [self.Nielsen_Press_Date1, self.Nielsen_Press_Date2, self.Nielsen_Press_Date3, self.Nielsen_Press_Date4, self.Nielsen_Press_Date5]

            self.n_Press_TitleLi[self.n_Press_idx].setText(title)
            self.n_Press_DateLi[self.n_Press_idx].setText(date)

            # if in db, make the title grey
            if self.c.execute("SELECT title FROM nielsen_Press WHERE title = ?", (title,)).fetchone() :
                self.n_Press_TitleLi[self.kc_buzz_idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                self.n_Press_DateLi[self.kc_buzz_idx].setStyleSheet('color:grey')

            idx = self.n_Press_idx

            self.n_Press_TitleLi[self.n_Press_idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.n_Press_TitleLi[self.n_Press_idx].clicked.connect(lambda: self.nClicked(href, title, idx, 'nielsen_Press'))
            self.n_Press_idx += 1

        except Exception as e :
            logging.info(">>>>> set_N_Press_Title error : {}".format(e))
            pass

    def nClicked(self, href, title, idx, name):
        try :
            self.nced = NClicked(href)
            self.nced.start()

            # insert into the db only when there is no same thing
            if self.c.execute("SELECT title FROM " + name + " WHERE title = ?", (title,)).fetchone() is None:
                self.c.execute("INSERT INTO " + name + " VALUES(?, ?)", (title, self.nowDateTime,))
                self.conn.commit()

                if name == 'nielsen_Press':
                    self.n_Press_TitleLi[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                    self.n_Press_DateLi[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')

        except Exception as e:
            logging.info(">>>>> nClicked error : {}".format(e))
            pass

if (__name__ == "__main__") :
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

