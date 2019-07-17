import time

import requests
from PyQt5.QtCore import QThread, pyqtSignal
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


class Nielsen_Top(QThread) :
    finished = pyqtSignal(str, str, str, str, str)

    def __init__(self):
        super().__init__()
        self.url = 'https://www.nielsen.com/kr/ko/top-ten/'
        self.chromeOptions = Options()
        self.chromeOptions.add_argument('--headless')

    def run(self):
        try :
            self.driver = webdriver.Chrome(chrome_options = self.chromeOptions, executable_path = './webdriver/chrome/chromedriver')
            # self.driver = webdriver.Chrome(chrome_options = self.chromeOptions, executable_path = '../../webdriver/chrome/chromedriver')
            self.driver.get(self.url)
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
            self.parseTv()
            self.parseApp()
            self.parseWeb()

        except Exception as e :
            logging.info("Nielsen_Top error : {}".format(e))
            pass

    def parseTv(self):
        self.driver.switch_to.frame(self.driver.find_elements_by_css_selector('iframe')[0])
        self.parse("nielsen_Top_Tv")

    def parseApp(self):
        self.driver.switch_to.frame(self.driver.find_elements_by_css_selector('iframe')[1])
        date = self.driver.find_elements_by_css_selector('.igc-table-cell-span')[0].text

        temp = self.driver.find_elements_by_css_selector('tbody')[1].find_elements_by_css_selector('tr')
        for i in temp:
            app = i.find_elements_by_css_selector('td')[1].text
            users = i.find_elements_by_css_selector('td')[2].text
            self.finished.emit("nielsen_Top_App", date, app, "", users)
        self.driver.switch_to.default_content()

    def parseWeb(self):
        self.driver.switch_to.frame(self.driver.find_elements_by_css_selector('iframe')[2])
        self.parse('nielsen_Top_Web')

    def parse(self, name):
        date = self.driver.find_elements_by_css_selector('.igc-table-cell-span')[0].text

        temp = self.driver.find_elements_by_css_selector('tbody')[1].find_elements_by_css_selector('tr')
        for i in temp:
            title = i.find_elements_by_css_selector('td')[1].text
            broadcast = i.find_elements_by_css_selector('td')[2].text
            audience = i.find_elements_by_css_selector('td')[3].text
            self.finished.emit(name, date, title, broadcast, audience)
        self.driver.switch_to.default_content()


if __name__ == "__main__" :
    Nielsen_Top().run()
