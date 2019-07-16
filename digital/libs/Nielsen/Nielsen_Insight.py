import logging

import requests
from PyQt5.QtCore import QThread, pyqtSignal
from bs4 import BeautifulSoup

class Nielsen_Insight(QThread) :
    finished = pyqtSignal(str, str, str)

    def __init__(self, howMany):
        super().__init__()
        self.url = 'https://www.nielsen.com/kr/ko/insights/'
        self.howMany = howMany

    def run(self):
        while(True) :
            try :
                url = requests.get(self.url, verify = False).content
                break
            except Exception as e :
                logging.info(">>>>> Nielsen insight request error : {}".format(e))
                continue
        soup = BeautifulSoup(url, 'html.parser')
        temp = soup.select('.featured-posts.module.module-slim > article')
        for n, i in enumerate(temp) :
            title = i.select_one('h2').text

            link = i.select_one('h2 a')['href']
            time = i.select_one('.updated.knockout.h5').text
            self.finished.emit(title, link, time)
            if n == self.howMany-1 :
                break

if __name__ == "__main__" :
    Nielsen_Insight(5).run()
