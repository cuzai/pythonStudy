from PyQt5.QtCore import QThread
from selenium import webdriver

class NClicked(QThread) :
    def __init__(self, link):
        super().__init__()
        self.url = link

    def run(self):
        driver = webdriver.Chrome('./webdriver/chrome/chromedriver')
        driver.get(self.url)
