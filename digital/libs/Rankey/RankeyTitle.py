from PyQt5.QtCore import QThread, pyqtSignal
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class RankeyTitle(QThread) :
    finished = pyqtSignal(str, str, str, str)
    def __init__(self):
        super().__init__()
        self.URL = 'http://www.rankey.com/blog/blog.php?type=letter'

    def run(self):
        try :
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(executable_path='./webdriver/chrome/chromedriver', options=chrome_options)
            driver.get(self.URL)

            # title
            driver.switch_to.frame(driver.find_element_by_css_selector('#view_letter_article'))
            temp = driver.find_element_by_css_selector('#print_area > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(4)')
            titles = temp.text
            temp = titles.split('\n')
            title = temp[3]
            name1 = temp[0]
            name2 = temp[1]
            name3 = temp[2]

            self.finished.emit(title, name1, name2, name3)
        except Exception as e :
            print("rankey ", e)




if __name__ == "__main__":
    RankeyTitle().run()
