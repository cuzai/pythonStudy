from PyQt5.QtCore import *
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.INFO)

class BellClicked(QThread):
    def __init__(self, link):
        super().__init__()
        self.url = 'http://www.thebell.co.kr/free/content/' + link

    def run(self):
        try :
            self.driver = webdriver.Chrome("./webdriver/chrome/chromedriver")
            self.driver.get(self.url)
        except Exception as e :
            logging.info(">>>>> BEll Clicked error : {}".format(e))
            pass

if __name__ == "__main__":
    BellClicked('').run()
