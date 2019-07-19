import logging
import re

import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QThread, pyqtSignal

class TechNeedle(QThread) :
    finished = pyqtSignal(str, str, str, str)
    error = pyqtSignal(str)

    def __init__(self, howMany):
        super().__init__()
        self.howMany = howMany
        self.url = 'http://techneedle.com/archives/category/default'

    def run(self):
        idx = 0
        while(True) :
            try :
               req = requests.get(self.url, verify = False).content
               break
            except Exception as e :
                logging.info(">>>> TechNeedle error : {}".format(e))
                continue

        soup = BeautifulSoup(req, 'html.parser')
        temp = soup.select('#post-wrapper article')
        for i in temp :
            href = i.select_one('.entry-title > a')['href']
            title = i.select_one('.entry-title > a').text
            dateTemp = i.select_one('.entry-date.published')['datetime']
            p = re.compile('(\\S*)-(\\S*)-(\\S*)T\\S*')
            m = p.search(dateTemp)
            date = "{}-{}-{}".format(m.group(1), m.group(2), m.group(3))

            self.finished.emit('techNeedle', title, href, date)

            idx += 1

            if idx == self.howMany :
                break

if __name__ == "__main__":
    TechNeedle(5).run()