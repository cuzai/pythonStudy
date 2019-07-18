import logging

import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QThread, pyqtSignal

class KoreanClick(QThread) :
    finished = pyqtSignal(str, str,str, str)
    error = pyqtSignal(str)

    def __init__(self, name, howMany):
        super().__init__()

        if name == 'koreanClick_Buzz' :
            self.url = 'http://www.koreanclick.com/insights/newsletter.html?code=buzzword'
        elif name == "koreanClick_Digital" :
            self.url = 'http://www.koreanclick.com/insights/newsletter.html?code=digitalnow'
        elif name == "koreanClick_Internet" :
            self.url = 'http://www.koreanclick.com/insights/newsletter.html?copde=trend'
        elif name == "koreanClick_Topic" :
            self.url = 'http://www.koreanclick.com/insights/newsletter.html?code=topic'

        self.howMany = howMany
        self.name = name

    def run(self):
        try :
            while(True):
                try :
                    req = requests.get(self.url).content
                    break
                except Exception as e:
                    self.error.emit(self.name)
                    logging.info(">>>>> {} request error : {}".format(self.name, e))
                    continue

            soup = BeautifulSoup(req, 'html.parser')
            temp = soup.select('table')[2].select('tr')

            for n, i in enumerate(temp) :
                title = temp[n+1].select_one('.tb_txt')
                href = title.select_one('a')['href']

                if self.name == "koreanClick_Digital" :
                    date = temp[n+1].select('.tb_txt_center')[1].text
                else :
                    date = temp[n+1].select('.tb_txt_center')[2].text
                self.finished.emit(self.name, title.text, href, date)
                logging.info("{} Emit".format(self.name))
                if n == self.howMany-1 :
                    break

        except Exception as e :
            logging.info((">>>>> def parse_{}() error : {}".format(self.name, e)))
            pass
if __name__ == "__main__":
    KoreanClick('koreanClick_Buzz', 5).run()