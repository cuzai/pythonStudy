from PyQt5.QtCore import QThread
from selenium import webdriver

class KcClicked(QThread) :
    def __init__(self, link):
        super().__init__()
        self.url = "http://www.koreanclick.com/insights/" + link

    def run(self):
        driver = webdriver.Chrome('./webdriver/chrome/chromedriver')
        driver.get(self.url)
