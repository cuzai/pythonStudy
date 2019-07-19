print("프로그램을 여는 중입니다.")
print("컴퓨터 사양에 따라 최대 10초까지 소요될 수 있습니다.")
print("프로그램을 종료할 때까지 이 창을 끄지 마십시오")

import datetime
import sqlite3
import time

from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot

from libs.KoreakClick.KoreanClick import KoreanClick
from libs.KoreakClick.KcClicked import KcClicked

from libs.Nielsen.Nielsen_Press import Nielsen_Press
from libs.Nielsen.Nielsen_Insight import Nielsen_Insight
from libs.Nielsen.NClicked import NClicked
from libs.Nielsen.Nielsen_Top import Nielsen_Top

from libs.DailyTrends.DailyTrends import DailyTrends
from libs.DailyTrends.DtClicked import DtClicked

from libs.Publy.PClicked import PClicked
from libs.Publy.Publy import Publy

from libs.TrendBird.TrendBird import TrendBird
from libs.TrendBird.TbClicked import TbClicked

from libs.TheBell.TheBell import TheBell
from libs.TheBell.BellClicked import BellClicked

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
    n_Insight_idx = 0
    n_Tv_idx = 0
    n_App_idx = 0
    n_Web_idx = 0

    publy_idx = 0

    tb_Biz_idx = 0
    tb_Tech_idx = 0
    tb_Design_idx = 0
    tb_Product_idx = 0
    tb_Consumer_idx = 0

    bell_Coopang_idx = 0
    bell_Ebay_idx = 0
    bell_Tmon_idx = 0
    bell_Wemap_idx = 0
    bell_11st_idx = 0
    bell_Market_idx = 0
    bell_Mushin_idx = 0
    bell_Ssg_idx = 0
    bell_Search_idx = 0


    def __init__(self):
        try :
            super().__init__()

            # initialize ui
            self.setupUi(self)

            # Daily Trends
            self.dailyTrend = DailyTrends(5)
            self.dailyTrend.error.connect(self.myError)
            self.dailyTrend.finished.connect(self.setTitle)
            self.dailyTrend.start()
            time.sleep(0.1)

            # Korean Click
            # self.kc_Internet = KoreanClick_Internet(self.howMany)
            self.kc_Internet = KoreanClick("koreanClick_Internet", self.howMany)
            self.kc_Internet.finished.connect(self.setTitle)
            self.kc_Internet.error.connect(self.myError)
            self.kc_Internet.start()
            time.sleep(0.1)

            # self.kc_Topic = KoreanClick_Topic(self.howMany)
            self.kc_Topic = KoreanClick("koreanClick_Topic", self.howMany)
            self.kc_Topic.finished.connect(self.setTitle)
            self.kc_Topic.error.connect(self.myError)
            self.kc_Topic.start()
            time.sleep(0.1)

            # self.kc_Digital = KoreanClick_DigitalNow(self.howMany)
            self.kc_Digital = KoreanClick("koreanClick_Digital", self.howMany)
            self.kc_Digital.finished.connect(self.setTitle)
            self.kc_Digital.error.connect(self.myError)
            self.kc_Digital.start()
            time.sleep(0.1)

            # self.kc_Buzz = KoreanClick_BuzzWord(self.howMany)
            self.kc_Buzz = KoreanClick("koreanClick_Buzz", self.howMany)
            self.kc_Buzz.finished.connect(self.setTitle)
            self.kc_Buzz.error.connect(self.myError)
            self.kc_Buzz.start()
            time.sleep(0.1)

            # Nielsen
            self.nielsen_Press = Nielsen_Press(self.howMany)
            self.nielsen_Press.finished.connect(self.setTitle)
            self.nielsen_Press.error.connect(self.myError)
            self.nielsen_Press.start()
            time.sleep(0.1)

            self.nielsen_Insight = Nielsen_Insight(self.howMany)
            self.nielsen_Insight.finished.connect(self.setTitle)
            self.nielsen_Insight.error.connect(self.myError)
            self.nielsen_Insight.start()
            time.sleep(0.1)

            self.nielsen_Top = Nielsen_Top()
            self.nielsen_Top.finished.connect(self.setTop)
            self.nielsen_Top.start()
            time.sleep(0.1)

            # publy
            self.publy = Publy(self.howMany)
            self.publy.finished.connect(self.setTitle)
            self.publy.start()
            time.sleep(0.2)

            # trendBird
            self.tb_Biz = TrendBird("tb_Biz", self.howMany)
            self.tb_Biz.finished.connect(self.setTitle)
            self.tb_Biz.start()
            time.sleep(0.1)

            self.tb_Tech = TrendBird("tb_Tech", self.howMany)
            self.tb_Tech.finished.connect(self.setTitle)
            self.tb_Tech.start()
            time.sleep(0.1)

            self.tb_Design = TrendBird("tb_Design", self.howMany)
            self.tb_Design.finished.connect(self.setTitle)
            self.tb_Design.start()
            time.sleep(0.1)

            self.tb_Product = TrendBird("tb_Product", self.howMany)
            self.tb_Product.finished.connect(self.setTitle)
            self.tb_Product.start()
            time.sleep(0.1)

            self.tb_Consumer = TrendBird("tb_Consumer", self.howMany)
            self.tb_Consumer.finished.connect(self.setTitle)
            self.tb_Consumer.start()
            time.sleep(0.1)

            # the bell
            self.bell_Coopang = TheBell("bell_Coopang", self.howMany)
            self.bell_Coopang.finished.connect(self.setTitle)
            self.bell_Coopang.start()
            time.sleep(0.1)

            self.bell_Ebay = TheBell("bell_Ebay", self.howMany)
            self.bell_Ebay.finished.connect(self.setTitle)
            self.bell_Ebay.start()
            time.sleep(0.1)

            self.bell_Tmon = TheBell("bell_Tmon", self.howMany)
            self.bell_Tmon.finished.connect(self.setTitle)
            self.bell_Tmon.start()
            time.sleep(0.1)

            self.bell_Wemap = TheBell("bell_Wemap", self.howMany)
            self.bell_Wemap.finished.connect(self.setTitle)
            self.bell_Wemap.start()
            time.sleep(0.1)

            self.bell_11st = TheBell("bell_11st", self.howMany)
            self.bell_11st.finished.connect(self.setTitle)
            self.bell_11st.start()
            time.sleep(0.1)

            self.bell_Market = TheBell("bell_Market", self.howMany)
            self.bell_Market.finished.connect(self.setTitle)
            self.bell_Market.start()
            time.sleep(0.1)

            self.lineEdit.returnPressed.connect(self.searchBell)

            # make db
            self.conn = sqlite3.connect('db/userData.db')
            now = datetime.datetime.now()
            self.nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
            self.c = self.conn.cursor()
            self.dbLi = ['dailyTrends', 'koreanClick_Internet', 'koreanClick_Topic', 'koreanClick_Digital', 'koreanClick_Buzz', 'nielsen_Press', 'nielsen_Insight', 'publy', 'tb_Biz', 'tb_Tech', 'tb_Design', 'tb_Product', 'tb_Consumer', 'bell_Coopang', 'bell_Ebay', 'bell_Tmon', 'bell_Wemap', 'bell_11st', 'bell_Market']
            for i in self.dbLi :
                self.c.execute("CREATE TABLE IF NOT EXISTS "+ i + "(title text, regdate text)")

        except Exception as e :
            logging.info(">>>>> __init__ error : {}".format(e))
            pass
# ---------------------------------------------------------------------------------
    @pyqtSlot(str, str, str, str)
    def setTitle(self, name, title, href, date):
        if name == "dailyTrends" :
            title_Li = [self.dailyTrend_Title1, self.dailyTrend_Title2, self.dailyTrend_Title3, self.dailyTrend_Title4, self.dailyTrend_Title5]
            date_Li = [self.dailyTrend_Date1, self.dailyTrend_Date2, self.dailyTrend_Date3, self.dailyTrend_Date4, self.dailyTrend_Date5]
            idx = self.dt_idx
        elif name == "koreanClick_Internet" :
            title_Li = [self.kc_Internet_Title1, self.kc_Internet_Title2, self.kc_Internet_Title3, self.kc_Internet_Title4, self.kc_Internet_Title5]
            date_Li = [self.kc_Internet_Date1, self.kc_Internet_Date2, self.kc_Internet_Date3, self.kc_Internet_Date4, self.kc_Internet_Date5]
            idx = self.kc_internet_idx
        elif name == "koreanClick_Topic" :
            title_Li =[self.kc_Topic_Title1, self.kc_Topic_Title2, self.kc_Topic_Title3, self.kc_Topic_Title4,self.kc_Topic_Title5]
            date_Li = [self.kc_Topic_Date1, self.kc_Topic_Date2, self.kc_Topic_Date3, self.kc_Topic_Date4, self.kc_Topic_Date5]
            idx = self.kc_topic_idx
        elif name == "koreanClick_Digital" :
            title_Li = [self.kc_DN_title1, self.kc_DN_title2, self.kc_DN_title3, self.kc_DN_title4, self.kc_DN_title5]
            date_Li = [self.kc_Digital_Date1, self.kc_Digital_Date2, self.kc_Digital_Date3, self.kc_Digital_Date4, self.kc_Digital_Date5]
            idx = self.kc_digital_idx
        elif name == "koreanClick_Buzz" :
            title_Li = [self.kc_BW_title1, self.kc_BW_title2, self.kc_BW_title3, self.kc_BW_title4, self.kc_BW_title5]
            date_Li = [self.kc_BuzzWord_Date1, self.kc_BuzzWord_Date2, self.kc_BuzzWord_Date3, self.kc_BuzzWord_Date4, self.kc_BuzzWord_Date5]
            idx = self.kc_buzz_idx
        elif name == "nielsen_Press" :
            title_Li = [self.nielsen_Press_title1, self.nielsen_Press_title2, self.nielsen_Press_title3, self.nielsen_Press_title4, self.nielsen_Press_title5]
            date_Li = [self.Nielsen_Press_Date1, self.Nielsen_Press_Date2, self.Nielsen_Press_Date3, self.Nielsen_Press_Date4, self.Nielsen_Press_Date5]
            idx = self.n_Press_idx
        elif name == "nielsen_Insight" :
            title_Li = [self.nielsen_Insight_title1, self.nielsen_Insight_title2, self.nielsen_Insight_title3]
            date_Li = [self.nielsen_Insight_Date1, self.nielsen_Insight_Date2, self.nielsen_Insight_Date3]
            idx = self.n_Insight_idx
        elif name == 'publy' :
            title_Li = [self.publy_Title1, self.publy_Title2, self.publy_Title3, self.publy_Title4, self.publy_Title5]
            date_Li = [self.pybly_Date1, self.pybly_Date2, self.pybly_Date3, self.pybly_Date4, self.pybly_Date5]
            idx = self.publy_idx
        elif name == 'tb_Biz' :
            title_Li = [self.trendBird_Biz_Title1, self.trendBird_Biz_Title2, self.trendBird_Biz_Title3, self.trendBird_Biz_Title4, self.trendBird_Biz_Title5]
            date_Li = [self.trendBird_Biz_Date1, self.trendBird_Biz_Date2, self.trendBird_Biz_Date3, self.trendBird_Biz_Date4, self.trendBird_Biz_Date5]
            idx = self.tb_Biz_idx
        elif name == 'tb_Tech' :
            title_Li = [self.trendBird_Tech_Title1, self.trendBird_Tech_Title2, self.trendBird_Tech_Title3, self.trendBird_Tech_Title4, self.trendBird_Tech_Title5]
            date_Li = [self.trendBird_Tech_Date1, self.trendBird_Tech_Date2, self.trendBird_Tech_Date3, self.trendBird_Tech_Date4, self.trendBird_Tech_Date5]
            idx = self.tb_Tech_idx
        elif name == 'tb_Design' :
            title_Li = [self.trendBird_Design_Title1, self.trendBird_Design_Title2, self.trendBird_Design_Title3, self.trendBird_Design_Title4, self.trendBird_Design_Title5]
            date_Li = [self.trendBird_Design_Date1, self.trendBird_Design_Date2, self.trendBird_Design_Date3, self.trendBird_Design_Date4, self.trendBird_Design_Date5]
            idx = self.tb_Design_idx
        elif name == 'tb_Product' :
            title_Li = [self.trendBird_Product_Title1, self.trendBird_Product_Title2, self.trendBird_Product_Title3, self.trendBird_Product_Title4, self.trendBird_Product_Title5]
            date_Li = [self.trendBird_Product_Date1, self.trendBird_Product_Date2, self.trendBird_Product_Date3, self.trendBird_Product_Date4, self.trendBird_Product_Date5]
            idx = self.tb_Product_idx
        elif name == 'tb_Consumer' :
            title_Li = [self.trendBird_Consumer_Title1, self.trendBird_Consumer_Title2, self.trendBird_Consumer_Title3, self.trendBird_Consumer_Title4, self.trendBird_Consumer_Title5]
            date_Li = [self.trendBird_Consumer_Date1, self.trendBird_Consumer_Date2, self.trendBird_Consumer_Date3, self.trendBird_Consumer_Date4, self.trendBird_Consumer_Date5]
            idx = self.tb_Consumer_idx
        elif name == 'bell_Coopang' :
            title_Li =[self.bell_Coopang_Title1, self.bell_Coopang_Title2, self.bell_Coopang_Title3, self.bell_Coopang_Title4, self.bell_Coopang_Title5]
            date_Li = [self.bell_Coopang_Date1, self.bell_Coopang_Date2, self.bell_Coopang_Date3, self.bell_Coopang_Date4, self.bell_Coopang_Date5]
            idx = self.bell_Coopang_idx
        elif name == 'bell_Ebay' :
            title_Li = [self.bell_Ebay_Title1, self.bell_Ebay_Title2, self.bell_Ebay_Title3, self.bell_Ebay_Title4, self.bell_Ebay_Title5]
            date_Li = [self.bell_Ebay_Date1, self.bell_Ebay_Date2, self.bell_Ebay_Date3, self.bell_Ebay_Date4, self.bell_Ebay_Date5]
            idx = self.bell_Ebay_idx
        elif name == 'bell_Tmon' :
            title_Li = [self.bell_Tmon_Title1, self.bell_Tmon_Title2, self.bell_Tmon_Title3, self.bell_Tmon_Title4, self.bell_Tmon_Title5]
            date_Li = [self.bell_Tmon_Date1, self.bell_Tmon_Date2, self.bell_Tmon_Date3, self.bell_Tmon_Date4, self.bell_Tmon_Date5]
            idx = self.bell_Tmon_idx
        elif name == 'bell_Wemap' :
            title_Li = [self.bell_Wemap_Title1, self.bell_Wemap_Title2, self.bell_Wemap_Title3, self.bell_Wemap_Title4, self.bell_Wemap_Title5]
            date_Li = [self.bell_Wemap_Date1, self.bell_Wemap_Date2, self.bell_Wemap_Date3, self.bell_Wemap_Date4, self.bell_Wemap_Date5]
            idx = self.bell_Wemap_idx
        elif name == 'bell_11st' :
            title_Li = [self.bell_11st_Title1, self.bell_11st_Title2, self.bell_11st_Title3, self.bell_11st_Title4, self.bell_11st_Title5]
            date_Li = [self.bell_11st_Date1, self.bell_11st_Date2, self.bell_11st_Date3, self.bell_11st_Date4, self.bell_11st_Date5]
            idx = self.bell_11st_idx
        elif name == 'bell_Market' :
            title_Li = [self.bell_Market_Title1, self.bell_Market_Title2, self.bell_Market_Title3, self.bell_Market_Title4, self.bell_Market_Title5]
            date_Li = [self.bell_Market_Date1, self.bell_Market_Date2, self.bell_Market_Date3, self.bell_Market_Date4, self.bell_Market_Date5]
            idx = self.bell_Market_idx

        title_Li[idx].setText(title)
        date_Li[idx].setText(date)

        # if in db, make the title and date grey
        if self.c.execute("SELECT title FROM " + name + " WHERE title = ?", (title,)).fetchone():
            title_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
            date_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')

        title_Li[idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        title_Li[idx].clicked.connect(lambda : self.whenClicked(name, href, title, idx, title_Li, date_Li))

        if name == "dailyTrends" :
            self.dt_idx += 1
        elif name == "koreanClick_Internet" :
            self.kc_internet_idx += 1
        elif name == "koreanClick_Topic" :
            self.kc_topic_idx += 1
        elif name == "koreanClick_Digital" :
            self.kc_digital_idx += 1
        elif name == "koreanClick_Buzz" :
            self.kc_buzz_idx += 1
        elif name == "nielsen_Press" :
            self.n_Press_idx += 1
        elif name == "nielsen_Insight" :
            self.n_Insight_idx += 1
        elif name == "publy" :
            self.publy_idx += 1
        elif name == "tb_Biz" :
            self.tb_Biz_idx += 1
        elif name == 'tb_Tech' :
            self.tb_Tech_idx += 1
        elif name == 'tb_Design' :
            self.tb_Design_idx += 1
        elif name == 'tb_Product' :
            self.tb_Product_idx += 1
        elif name == 'tb_Consumer' :
            self.tb_Consumer_idx += 1
        elif name == 'bell_Coopang' :
            self.bell_Coopang_idx += 1
        elif name == 'bell_Ebay' :
            self.bell_Ebay_idx += 1
        elif name == 'bell_Tmon' :
            self.bell_Tmon_idx += 1
        elif name == 'bell_Wemap' :
            self.bell_Wemap_idx += 1
        elif name == 'bell_11st' :
            self.bell_11st_idx += 1
        elif name == 'bell_Market' :
            self.bell_Market_idx += 1

    @pyqtSlot(str, str, str, str, str)
    def setTop(self, name, date, title, broadcast, audience):
        # date, programme, broadcast, audience
        if name == "nielsen_Top_Tv" :
            titleLi = [self.nielsen_TV_Programme1, self.nielsen_TV_Programme2, self.nielsen_TV_Programme3, self.nielsen_TV_Programme4, self.nielsen_TV_Programme5, self.nielsen_TV_Programme6, self.nielsen_TV_Programme7, self.nielsen_TV_Programme8, self.nielsen_TV_Programme9, self.nielsen_TV_Programme10]
            broadcastLi = [self.nielsen_TV_Broadcast1, self.nielsen_TV_Broadcast2, self.nielsen_TV_Broadcast3, self.nielsen_TV_Broadcast4, self.nielsen_TV_Broadcast5, self.nielsen_TV_Broadcast6, self.nielsen_TV_Broadcast7, self.nielsen_TV_Broadcast8, self.nielsen_TV_Broadcast9, self.nielsen_TV_Broadcast10]
            audienceLi = [self.nielsen_TV_Audience1, self.nielsen_TV_Audience2, self.nielsen_TV_Audience3, self.nielsen_TV_Audience4, self.nielsen_TV_Audience5, self.nielsen_TV_Audience6, self.nielsen_TV_Audience7, self.nielsen_TV_Audience8, self.nielsen_TV_Audience9, self.nielsen_TV_Audience10]
            idx = self.n_Tv_idx
            dateLi = self.nielsen_TV_Date
        # date, appName, None, Users
        elif name == "nielsen_Top_App" :
            titleLi = [self.nielsen_App_Name1, self.nielsen_App_Name2, self.nielsen_App_Name3, self.nielsen_App_Name4, self.nielsen_App_Name5, self.nielsen_App_Name6, self.nielsen_App_Name7, self.nielsen_App_Name8, self.nielsen_App_Name9, self.nielsen_App_Name10]
            audienceLi = [self.nielsen_App_User1, self.nielsen_App_User2, self.nielsen_App_User3, self.nielsen_App_User4, self.nielsen_App_User5, self.nielsen_App_User6, self.nielsen_App_User7, self.nielsen_App_User8, self.nielsen_App_User9, self.nielsen_App_User10]
            idx = self.n_App_idx
            dateLi = self.nielsen_App_Date
        # date, webTitle, webReach, webUser
        elif name == 'nielsen_Top_Web' :
            titleLi = [self.nielsen_Web_title1, self.nielsen_Web_title2, self.nielsen_Web_title3, self.nielsen_Web_title4, self.nielsen_Web_title5, self.nielsen_Web_title6, self.nielsen_Web_title7, self.nielsen_Web_title8, self.nielsen_Web_title9, self.nielsen_Web_title10]
            broadcastLi = [self.nielsen_Web_Reach1, self.nielsen_Web_Reach2, self.nielsen_Web_Reach3, self.nielsen_Web_Reach4, self.nielsen_Web_Reach5, self.nielsen_Web_Reach6, self.nielsen_Web_Reach7, self.nielsen_Web_Reach8, self.nielsen_Web_Reach9, self.nielsen_Web_Reach10]
            audienceLi = [self.nielsen_Web_User1, self.nielsen_Web_User2, self.nielsen_Web_User3, self.nielsen_Web_User4, self.nielsen_Web_User5, self.nielsen_Web_User6, self.nielsen_Web_User7, self.nielsen_Web_User8, self.nielsen_Web_User9, self.nielsen_Web_User10]
            idx = self.n_Web_idx
            dateLi = self.nielsen_Web_Date

        titleLi[idx].setText("   " + title)
        dateLi.setText(date)
        audienceLi[idx].setText(audience)
        try :
            broadcastLi[idx].setText("   " + broadcast)
        except Exception :
            # exception for neilsen top app
            pass

        if name == "nielsen_Top_Tv" :
            self.n_Tv_idx += 1
        elif name == "nielsen_Top_App" :
            self.n_App_idx += 1
        elif name == "nielsen_Top_Web" :
            self.n_Web_idx += 1

    def whenClicked(self, name, href, title, idx, title_Li, date_Li):
        try :
            if name == "dailyTrends" :
                clicked = DtClicked(href)
            elif name == "koreanClick_Internet" or name == "koreanClick_Topic" or name == "koreanClick_Digital" or name == "koreanClick_Buzz":
                clicked = KcClicked(href)
            elif name == "nielsen_Press" or name == "nielsen_Insight" :
                clicked = NClicked(href)
            elif name == 'publy' :
                clicked = PClicked(href)
            elif name == 'tb_Biz' or name == 'tb_Tech' or name == 'tb_Design' or name == 'tb_Product' or name == 'tb_Consumer':
                clicked = TbClicked(href)
            elif name == 'bell_Coopang' or name == 'bell_Ebay' or name == 'bell_Tmon' or name == 'bell_Wemap' or name == 'bell_11st' or name == 'bell_Market' :
                clicked = BellClicked(href)
            clicked.start()
            time.sleep(0.1)

            # insert into the db ONLY WHEN there is no same thing and make it grey
            if self.c.execute("SELECT title FROM " + name + " WHERE title = ?", (title,)).fetchone() is None :
                self.c.execute("INSERT INTO " + name + " VALUES(?, ?)", (title, self.nowDateTime,))
                self.conn.commit()
                title_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                date_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')

        except Exception as e:
            logging.info(">>>>> whenClicked error : {}".format(e))
            pass

    @pyqtSlot(str)
    def myError(self, name):
        if name == "koreanClick_Internet" :
            self.kc_Internet_Title3.setText("코리안클릭 웹사이트의 연결이 지연되고 있습니다. 잠시만 기다려주십시오.")
        elif name == "koreanClick_Topic" :
            self.kc_Topic_Title3.setText("코리안클릭 웹사이트의 연결이 지연되고 있습니다. 잠시만 기다려주십시오.")
        elif name == "koreanClick_Digital" :
            self.kc_DN_title3.setText("코리안클릭 웹사이트의 연결이 지연되고 있습니다. 잠시만 기다려주십시오.")
        elif name == 'koreanClick_Buzz' :
            self.kc_BW_title3.setText("코리안클릭 웹사이트의 연결이 지연되고 있습니다. 잠시만 기다려주십시오.")
        elif name == 'dailyTrend' :
            self.dailyTrend_Title3.setText("데일리트렌드 인터넷 연결이 지연되고 있습니다. 잠시만 기다려주십시오.")
        elif name == "nielsen_Press" :
            self.nielsen_Press_title3.setText("닐슨코리아 인터넷 연결이 지연되고 있습니다. 잠시만 기다려주십시오.")
        elif name == "nielsen_Insight" :
            self.nielsen_Insight_title2.setText("닐슨코리아 인터넷 연결이 지연되고 있습니다. 잠시만 기다려주십시오.")

    def searchBell(self):
        myInput = self.lineEdit.text()
        titleLi = [self.bell_Search_Title1, self.bell_Search_Title2, self.bell_Search_Title3, self.bell_Search_Title4, self.bell_Search_Title5]
        dateLi = [self.bell_Search_Date1, self.bell_Search_Date2, self.bell_Search_Date3, self.bell_Search_Date4, self.bell_Search_Date5]

        for i in titleLi :
            i.setText("")
            i.setStyleSheet('color:black; text-align:left; background:transparent;')

        for i in dateLi:
            i.setText("")
            i.setStyleSheet('color:black; text-align:left; background:transparent;')

        if myInput == "쿠팡" or myInput == "이베이" or myInput == "티몬" or myInput == "위메프" or myInput == "11번가" or myInput == "마켓컬리" or myInput == "무신사" or myInput == "신세계" :
            self.bell_Search_Title3.setText(myInput + "은(는) 이미 존재하는 탭입니다.")
        else :
            self.bell_Search_Title3.setText("잠시만 기다려주십시오...")
            self.bell_Search = TheBell(myInput, self.howMany)
            self.bell_Search.finished.connect(self.setSearchTitle)
            self.bell_Search.start()
            self.c.execute("CREATE TABLE IF NOT EXISTS bell_Search(title text, regdate text)")
            for i in titleLi:
                i.setText("")
                i.setStyleSheet('color:black; text-align:left; background:transparent;')

            for i in dateLi:
                i.setText("")
                i.setStyleSheet('color:black; text-align:left; background:transparent;')


    @pyqtSlot(str, str, str, str)
    def setSearchTitle(self, name, title, href, date):
        try :
            title_Li = [self.bell_Search_Title1, self.bell_Search_Title2, self.bell_Search_Title3, self.bell_Search_Title4, self.bell_Search_Title5]
            date_Li = [self.bell_Search_Date1, self.bell_Search_Date2, self.bell_Search_Date3, self.bell_Search_Date4, self.bell_Search_Date5]
            idx = self.bell_Search_idx

            title_Li[idx].setStyleSheet('color:black; text-align:left; background:transparent;')
            date_Li[idx].setStyleSheet('color:black; text-align:left; background:transparent;')

            if title == "검색결과가 없습니다." :
                title_Li[2].setText(title)
            else :
                title_Li[idx].setText(title)
                date_Li[idx].setText(date)

                # if in db, make the title and date grey
                if self.c.execute("SELECT title FROM bell_Search WHERE title = ?", (title,)).fetchone() :
                    title_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                    date_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')

                title_Li[idx].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                title_Li[idx].clicked.connect(lambda : self.whenSearchClicked(name, href, title, idx, title_Li, date_Li))

                self.bell_Search_idx += 1
                if self.bell_Search_idx == self.howMany :
                    self.bell_Search_idx = 0
        except Exception as e :
            logging.info(">>>>> setSearchTitle error : {}".format(e))
            pass

    def whenSearchClicked(self, name, href, title, idx, title_Li, date_Li):
        try :
            clicked = BellClicked(href)
            clicked.start()
            time.sleep(0.1)

            # insert into the db ONLY WHEN there is no same thing and make it grey
            if self.c.execute("SELECT title FROM bell_Search WHERE title = ?", (title,)).fetchone() is None:
                    self.c.execute("INSERT INTO bell_Search VALUES(?, ?)", (title, self.nowDateTime,))
                    self.conn.commit()
                    title_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')
                    date_Li[idx].setStyleSheet('color:grey; text-align:left; background:transparent;')

        except Exception as e :
            logging.info(">>>>> whenSearchClicked error : {}".format(e))
            pass

    def __del__(self):
        self.conn.close()
        self.dailyTrend.terminate()

        self.kc_Internet.terminate()
        self.kc_Topic.terminate()
        self.kc_Digital.terminate()
        self.kc_Buzz.terminate()

        self.nielsen_Press.terminate()
        self.nielsen_Insight.terminate()


if (__name__ == "__main__") :
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

