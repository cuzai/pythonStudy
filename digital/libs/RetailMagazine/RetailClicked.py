import time

from PyQt5.QtCore import *
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.INFO)

class RetailClicked(QThread):
    def __init__(self, link):
        super().__init__()
        self.logIn = 'http://www.retailing.co.kr/member/login.php?goUrl=%2Fmall%2Fsubscriber.php'
        self.url = 'http://www.retailing.co.kr' + link

    def run(self):
        try :
            self.driver = webdriver.Chrome("./webdriver/chrome/chromedriver")
            # self.driver = webdriver.Chrome("../../webdriver/chrome/chromedriver")
            self.driver.get(self.logIn)
            self.driver.implicitly_wait(10)
            self.driver.find_elements_by_css_selector('.input_text')[0].send_keys('digital1')
            self.driver.find_elements_by_css_selector('.input_text')[1].send_keys('elwlxjfwjsfir1')
            self.driver.find_elements_by_css_selector('.input_text')[1].send_keys(Keys.ENTER)

            self.driver.get(self.url)
        except Exception as e :
            logging.info(">>>>> RetailMagazine Clicked error : {}".format(e))
            pass

if __name__ == "__main__":
    RetailClicked('retail_Cover').run()
