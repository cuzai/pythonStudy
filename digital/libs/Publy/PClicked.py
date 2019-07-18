from PyQt5.QtCore import *
import logging
from selenium import webdriver

logging.basicConfig(level=logging.INFO)

class PClicked(QThread):
    def __init__(self, link):
        super().__init__()
        self.link = link

    def run(self):
        try :
            self.driver = webdriver.Chrome(
                "./webdriver/chrome/chromedriver")
            url = 'https://publy.co/login?redirect_to=' + self.link
            self.driver.get(url)
            self.driver.implicitly_wait(10)

            self.driver.find_element_by_css_selector('#email').send_keys('khc1227@lotteshopping.com')
            self.driver.find_element_by_css_selector('#password').send_keys('elwlxjfwjsfir1')
            self.driver.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-block').click()

        except Exception as e :
            logging.info(">>>>> DtClicked error : {}".format(e))
            pass

if __name__ == "__main__":
    PClicked('https://www.dailytrend.co.kr/login/').run()
