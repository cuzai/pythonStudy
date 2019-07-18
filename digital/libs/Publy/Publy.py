from PyQt5.QtCore import QThread, pyqtSignal
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

class Publy(QThread) :
    finished = pyqtSignal(str, str, str, str)

    def __init__(self, howMany):
        super().__init__()
        self.howMany = howMany
        self.url = 'https://publy.co/category/all'
        self.chromeOptions = Options()
        self.chromeOptions.add_argument('--headless')

    def run(self):
        try :
            idx = 0
            divNum = 0  # 해당월 內 아티클이 howMany보다 적을 경우 그 前월 것을 가져오기 위함
            self.driver = webdriver.Chrome(chrome_options = self.chromeOptions, executable_path = './webdriver/chrome/chromedriver')
            # self.driver = webdriver.Chrome(chrome_options = self.chromeOptions, executable_path = '../../webdriver/chrome/chromedriver')
            self.driver.get(self.url)
            while(True) :
                temp = self.driver.find_elements_by_css_selector('.set-list__container.curation.bg-white.pt-7')[divNum]
                titleLi = temp.find_elements_by_css_selector('.set-list > div')
                for i in titleLi :
                    article = i.find_elements_by_css_selector('.col-4.mb-4')
                    for e in article :
                        # get title
                        title = e.find_element_by_css_selector('h6').text

                        # regrex the link
                        tempLink = e.find_element_by_css_selector('a').get_attribute('href')
                        p = re.compile('https://publy.co(\\S*)')
                        m = p.search(tempLink)
                        link = m.group(1)

                        # regrex the date
                        tempTime = e.find_element_by_css_selector('img').get_attribute('src')
                        p = re.compile('https://publy.imgix.net/images/(\\S*)/(\\S*)/(\\S*)/\\S*')
                        m = p.search(tempTime)
                        time = m.group(1) + '-' + m.group(2) + '-' + m.group(3)

                        self.finished.emit("publy", title, link, time)

                        idx += 1
                        if idx < self.howMany :
                            divNum = 1
                        else : break
                    if idx < self.howMany :
                        pass
                    else : break
                if idx < self.howMany:
                    pass
                else:
                    break


        except Exception as e :
            logging.info(">>>>> Pybly error : {}".format(e))

if __name__ == "__main__" :
    Publy(5).run()