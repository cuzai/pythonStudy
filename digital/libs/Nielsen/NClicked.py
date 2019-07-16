import logging

from PyQt5.QtCore import QThread
from selenium import webdriver

class NClicked(QThread) :
    def __init__(self, link):
        super().__init__()
        self.url = link

    def run(self):
        try :
            driver = webdriver.Chrome('./webdriver/chrome/chromedriver')
            driver.get(self.url)
        except Exception as e :
            logging.info(">>>>> NClicked.py error : {}".format(e))
            pass
