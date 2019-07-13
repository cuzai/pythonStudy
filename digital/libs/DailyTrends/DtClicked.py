from PyQt5.QtCore import *
import logging
from selenium import webdriver

logging.basicConfig(level=logging.INFO)

class DtClicked(QThread):
    def __init__(self, link):
        super().__init__()
        self.link = link

    def run(self):
        try :
            self.driver = webdriver.Chrome(
                "./webdriver/chrome/chromedriver")
            url = 'https://www.dailytrend.co.kr/login/?redirect_to=' + self.link
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            self.driver.find_elements_by_css_selector('.userpro-input')[0].find_element_by_css_selector('input').send_keys('retailrnd5')
            self.driver.find_elements_by_css_selector('.userpro-input')[1].find_element_by_css_selector('input').send_keys('fhtepqorghkwja5')
            self.driver.find_element_by_css_selector('.userpro-button').click()
        except Exception as e :
            print(e)



if __name__ == "__main__":
    DtClicked('https://www.dailytrend.co.kr/login/').run()
