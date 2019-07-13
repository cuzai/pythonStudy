from PyQt5.QtCore import QThread, pyqtSignal
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib import request
from urllib.parse import urljoin
import os

class RankeyImg(QThread) :
    finished = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.URL = 'http://www.rankey.com/blog/blog.php?type=letter'

    def run(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(
            executable_path='./webdriver/chrome/chromedriver', options=chrome_options)
        driver.get(self.URL)

        # get images
        driver.switch_to.frame(driver.find_element_by_css_selector('#view_letter_article'))
        temp = driver.find_element_by_css_selector('#print_area > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(4)')
        temp = temp.find_elements_by_css_selector('img')

        for n, i in enumerate(temp) :
            if (n == 1 or n == 2 or n ==3):
                currentDir = os.getcwd()
                temp = urljoin(currentDir, 'res/rankey/img')
                fileName = temp + str(n) + '.png'
                request.urlretrieve(i.get_attribute('src'), fileName)
                self.finished.emit(str(n))

if __name__ == "__main__":
    RankeyImg().run()