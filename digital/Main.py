from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot

from libs.KoreakClick.KoreanClick_Internet import KoreanClick_Internet
from libs.KoreakClick.KoreanClick_Topic import KoreanClick_Topic
from libs.KoreakClick.KoreanClick_DigitalNow import KoreanClick_DigitalNow
from libs.KoreakClick.KoreanClick_BuzzWord import KoreanClick_BuzzWord
from libs.KoreakClick.KcClicked import KcClicked

from libs.Nielsen.Nielsen_Press import Nielsen_Press
from libs.Nielsen.NClicked import NClicked

from libs.Rankey.RankeyTitle import RankeyTitle
from libs.Rankey.RankeyImg import RankeyImg

from libs.DailyTrends.DailyTrends import DailyTrends
from libs.DailyTrends.DtClicked import DtClicked

from ui.myUi import Ui_MainWindow
import sys
import logging

logging.basicConfig(level = logging.INFO)

form_class = uic.loadUiType('./ui/main.ui')[0]
class Main(QtWidgets.QMainWindow, Ui_MainWindow) :
    dt_idx = 0

    kcInternet_idx = 0
    kcTopic_idx = 0
    kcDN_idx = 0
    kcBW_idx = 0
    n_Press_idx = 0

    def __init__(self):
        try :
            super().__init__()

            # initialize ui
            self.setupUi(self)
            # self.rk1st.setPixmap(QtGui.QPixmap("./res/rankey/rank1.png"))
            # self.rk2nd.setPixmap(QtGui.QPixmap("./res/rankey/rank2.png"))
            # self.rk3rd.setPixmap(QtGui.QPixmap("./res/rankey/rank3.png"))

            # Daily Trends
            self.dailyTrend = DailyTrends(5)
            self.dailyTrend.finished.connect(self.dtSetTitle)
            self.dailyTrend.start()

            # # rankey
            # self.rkt = RankeyTitle()
            # self.rkt.finished.connect(self.rkSetTitle)
            # self.rkt.start()
            #
            # self.rki = RankeyImg()
            # self.rki.finished.connect(self.rkSetImg)
            # self.rki.start()

            # Korean Click
            self.koreanClick_Internet = KoreanClick_Internet(5)
            self.koreanClick_Internet.finished.connect(self.set_Kc_Internet_Title)
            self.koreanClick_Internet.start()

            self.koreanClick_Topic = KoreanClick_Topic(5)
            self.koreanClick_Topic.finished.connect(self.set_Kc_Topic_Title)
            self.koreanClick_Topic.start()

            self.koreanClick_DigitalNow = KoreanClick_DigitalNow(5)
            self.koreanClick_DigitalNow.finished.connect(self.set_Kc_DigitalNow_Title)
            self.koreanClick_DigitalNow.start()

            self.koreanClick_BuzzWords = KoreanClick_BuzzWord(5)
            self.koreanClick_BuzzWords.finished.connect(self.set_Kc_BuzzWord_Title)
            self.koreanClick_BuzzWords.start()

            # Nielsen
            self.nielsen_Press = Nielsen_Press(5)
            self.nielsen_Press.finished.connect(self.set_N_Press_Title)
            self.nielsen_Press.start()

        except Exception as e :
            logging.info("__init__ : {}".format(e))
            pass

# ---------------------------------------------------------------------------------
    # Daily Trends
    @pyqtSlot(str, str)
    def dtSetTitle(self, title, href):
        logging.info("dtSetTitle")
        try :
            dtLi = [self.dailyTrend_Title1, self.dailyTrend_Title2, self.dailyTrend_Title3, self.dailyTrend_Title4, self.dailyTrend_Title5]
            dtLi[self.dt_idx].setText(title)
            dtLi[self.dt_idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            dtLi[self.dt_idx].clicked.connect(lambda : self.dtClicked(href))
            self.dt_idx += 1

        except Exception as e :
            logging.info("dtSetTitle : {}".format(e))
            pass

    def dtClicked(self, href):
        self.dc = DtClicked(href)
        self.dc.start()

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

    # korean click
    @pyqtSlot(str, str, str)
    def set_Kc_Internet_Title(self, title, href, date):
        logging.info("set_Kc_Internet_Title")
        try :
            self.kc_Internet_Title_Li = [self.kc_Internet_Title1, self.kc_Internet_Title2, self.kc_Internet_Title3, self.kc_Internet_Title4, self.kc_Internet_Title5]
            self.kc_Internet_Date_Li = [self.kc_Internet_Date1, self.kc_Internet_Date2, self.kc_Internet_Date3, self.kc_Internet_Date4, self.kc_Internet_Date5]

            self.kc_Internet_Title_Li[self.kcInternet_idx].setText(title)
            self.kc_Internet_Date_Li[self.kcInternet_idx].setText(date)
            self.kc_Internet_Title_Li[self.kcInternet_idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.kc_Internet_Title_Li[self.kcInternet_idx].clicked.connect(lambda: self.kcClicked(href))
            self.kcInternet_idx += 1
        except Exception as e :
            logging.info("def kcSet_InternetTitle", e)
            pass

    @pyqtSlot(str, str, str)
    def set_Kc_Topic_Title(self, title, href, date):
        logging.info("set_Kc_Topic_Title")
        try :
            self.kc_Topic_Title_Li = [self.kc_Topic_Title1, self.kc_Topic_Title2, self.kc_Topic_Title3, self.kc_Topic_Title4, self.kc_Topic_Title5]
            self.kc_Topic_Date_Li = [self.kc_Topic_Date1, self.kc_Topic_Date2, self.kc_Topic_Date3, self.kc_Topic_Date4, self.kc_Topic_Date5]

            self.kc_Topic_Title_Li[self.kcTopic_idx].setText(title)
            self.kc_Topic_Date_Li[self.kcTopic_idx].setText(date)
            self.kc_Topic_Title_Li[self.kcTopic_idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.kc_Topic_Title_Li[self.kcTopic_idx].clicked.connect(lambda: self.kcClicked(href))
            self.kcTopic_idx += 1
        except Exception as e :
            logging.info("def kcSet_TopicTitle : {} ".format(e))
            pass

    @pyqtSlot(str, str)
    def set_Kc_DigitalNow_Title(self, title, href):
        logging.info("set_Kc_DigitalNow_Title")
        try :
            self.kc_DN_Li = [self.kc_DN_title1, self.kc_DN_title2, self.kc_DN_title3, self.kc_DN_title4, self.kc_DN_title5]
            self.kc_DN_Li[self.kcDN_idx].setText(title)
            self.kc_DN_Li[self.kcDN_idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.kc_DN_Li[self.kcDN_idx].clicked.connect(lambda: self.kcClicked(href))
            self.kcDN_idx += 1

        except Exception as e :
            logging.info("set_Kc_DigitalNow_Title : {}".format(e))
            pass

    @pyqtSlot(str, str)
    def set_Kc_BuzzWord_Title(self, title, href):
        logging.info("set_Kc_Bussword_Title")
        try:
            self.kc_BW_Li = [self.kc_BW_title1, self.kc_BW_title2, self.kc_BW_title3, self.kc_BW_title4, self.kc_BW_title5]
            self.kc_BW_Li[self.kcBW_idx].setText(title)
            self.kc_BW_Li[self.kcBW_idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.kc_BW_Li[self.kcBW_idx].clicked.connect(lambda: self.kcClicked(href))
            self.kcBW_idx += 1

        except Exception as e :
            logging.info("set_Kc_Bussword_Title".format(e))
            pass

    def kcClicked(self, href):
        self.kced = KcClicked(href)
        self.kced.start()

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
            logging.info("set_N_Press_Title : {}".format(e))
            pass

    def nClicked(self, href):
        self.nced = NClicked(href)
        self.nced.start()


if (__name__ == "__main__") :
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


