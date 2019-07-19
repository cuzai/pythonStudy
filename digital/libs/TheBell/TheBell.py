import logging
import re
from urllib import parse

import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QThread, pyqtSignal

class TheBell(QThread) :
    finished = pyqtSignal(str, str, str, str)
    error = pyqtSignal(str)

    def __init__(self, name, howMany):
        super().__init__()
        self.howMany = howMany
        self.name = name

        if name == 'bell_Coopang' :
            self.url = 'http://www.thebell.co.kr/free/content/Search.asp?keyword=%EC%BF%A0%ED%8C%A1'
        elif name == 'bell_Ebay' :
            self.url = 'http://www.thebell.co.kr/free/content/Search.asp?keyword=%EC%9D%B4%EB%B2%A0%EC%9D%B4'
        elif name == 'bell_Tmon' :
            self.url = 'http://www.thebell.co.kr/free/content/Search.asp?keyword=%ED%8B%B0%EB%AA%AC'
        elif name == 'bell_Wemap' :
            self.url = 'http://www.thebell.co.kr/free/content/Search.asp?keyword=%EC%9C%84%EB%A9%94%ED%94%84'
        elif name == 'bell_11st' :
            self.url = 'http://www.thebell.co.kr/free/content/Search.asp?keyword=11%EB%B2%88%EA%B0%80'
        elif name == 'bell_Market':
            self.url = 'http://www.thebell.co.kr/free/content/Search.asp?keyword=%EB%A7%88%EC%BC%93%EC%BB%AC%EB%A6%AC'
        elif name == 'bell_Mushin' :
            self.url ='http://www.thebell.co.kr/free/content/Search.asp?keyword=%EB%AC%B4%EC%8B%A0%EC%82%AC'
        elif name == 'bell_Ssg' :
            self.url = 'http://www.thebell.co.kr/free/content/Search.asp?keyword=%EC%8B%A0%EC%84%B8%EA%B3%84'
        else  :
            self.url = 'http://www.thebell.co.kr/free/content/Search.asp?keyword=' + self.name

    def run(self):
        idx = 0
        while(True) :
            try :
                req = requests.get(self.url).content
                break
            except Exception as e :
                logging.info(">>>>> TheBell error : {}".format(e))
                continue

        soup = BeautifulSoup(req, 'html.parser')

        temp = soup.select('.listBox li')
        if temp == [] :
            self.finished.emit(self.name, "검색결과가 없습니다.", "", "")
        else :
            for i in temp :
                href = i.select_one('a')['href']
                title = i.select_one('a > dt').text
                dateTemp = i.select_one('.date').text
                p = re.compile('^(\\S*) \\S* \\S*')
                m = p.search(dateTemp)
                date = m.group(1)
                self.finished.emit(self.name, title, href, date)
                idx += 1
                if idx == self.howMany :
                    break

if __name__ == "__main__":
    TheBell('sdfsdf', 5).run()