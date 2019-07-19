import logging
import re

import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QThread, pyqtSignal

class RetailMagazine(QThread) :
    finished = pyqtSignal(str, str, str, str)
    error = pyqtSignal(str)

    def __init__(self, name, howMany):
        super().__init__()
        self.howMany = howMany
        self.name = name

        if name == 'retail_Special' :
            self.url = 'http://www.retailing.co.kr/article/special.php'
        elif name == 'retail_Store' :
            self.url = 'http://www.retailing.co.kr/article/store.php'
        elif name == 'retail_Strategy' :
            self.url = 'http://www.retailing.co.kr/article/strategy.php'
        elif name == 'retail_Global' :
            self.url = 'http://www.retailing.co.kr/article/global.php'
        elif name == 'retail_Market' :
            self.url = 'http://www.retailing.co.kr/article/market.php'
        elif name == 'retail_Field':
            self.url = 'http://www.retailing.co.kr/article/field.php'

    def run(self):
        idx = 0
        while(True) :
            try :
                req = requests.get(self.url).content
                break
            except Exception as e :
                logging.info(">>>>> Retail Magazine error : {}".format(e))
                continue

        soup = BeautifulSoup(req, 'html.parser')

        temp = soup.select('li .title_strong')
        for n, i in enumerate(temp) :
            href = i.select_one('a')['href']
            title = "   " + i.select_one('a').text
            date = ""

            self.finished.emit(self.name, title, href, date)

            if n == self.howMany -1 :
                break

if __name__ == "__main__":
    RetailMagazine('retail_Cover', 5).run()