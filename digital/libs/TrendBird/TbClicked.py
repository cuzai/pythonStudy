from PyQt5.QtCore import *
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.INFO)

class TbClicked(QThread):
    def __init__(self, link):
        super().__init__()
        self.url = 'http://www.trendbird.biz' + link

    def run(self):
        try :
            self.driver = webdriver.Chrome("./webdriver/chrome/chromedriver")
            self.driver.get(self.url)
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_css_selector('.password_input').send_keys('khc1227@lotteshopping.com')
            self.driver.find_element_by_css_selector('.password_input').send_keys(Keys.ENTER)
        except Exception as e :
            logging.info(">>>>> TbClicked error : {}".format(e))
            pass

if __name__ == "__main__":
    TbClicked('https://www.dailytrend.co.kr/login/').run()
