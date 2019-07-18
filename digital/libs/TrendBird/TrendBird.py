import logging
import re

import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QThread, pyqtSignal

class TrendBird(QThread) :
    finished = pyqtSignal(str, str, str, str)
    error = pyqtSignal(str)

    def __init__(self, name, howMany):
        super().__init__()
        self.howMany = howMany
        self.name = name

        if name == 'tb_Biz' :
            self.url = 'http://www.trendbird.biz/category/Business'
        elif name == 'tb_Tech' :
            self.url = 'http://www.trendbird.biz/category/Tech'
        elif name == 'tb_Design' :
            self.url = 'http://www.trendbird.biz/category/Design'
        elif name == 'tb_Product' :
            self.url = 'http://www.trendbird.biz/category/Product'
        elif name == 'tb_Consumer' :
            self.url = 'http://www.trendbird.biz/category/Consumer'

    def run(self):
        idx = 0
        while(True) :
            try :
               req = requests.get(self.url, verify = False).content
               break
            except Exception as e :
                logging.info(">>>> TrendBird error : {}".format(e))
                continue

        soup = BeautifulSoup(req, 'html.parser')
        temp = soup.select('#thumb_main tr td')
        for i in temp :
            href = i.select_one('a')['href']
            title = i.select_one('img')['alt']

            url = "http://www.trendbird.biz" + href
            while(True) :
                try :
                    req =  requests.get(url).content
                    break
                except Exception :
                    continue
            soup = BeautifulSoup(req, 'html.parser')
            dateTemp = soup.select_one('.date').text
            p = re.compile('(\\S*)/(\\S*)/(\\S*)\\S*')
            m = p.search(dateTemp)
            date = m.group(1) + "-" + m.group(2) + "-" + m.group(3)

            self.finished.emit(self.name, title, href, date)

            idx += 1

            if idx == self.howMany :
                break

if __name__ == "__main__":
    TrendBird('tb_Biz', 5).run()