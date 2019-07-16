import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QThread, pyqtSignal
import logging

class KoreanClick(QThread) :
    finished = pyqtSignal(str, str, str)

    def __init__(self, howMany):
        super().__init__()
        self.howMany = howMany

    def run(self):
        self.KoreanClick_Internet()
        self.KoreanClick_Topic()
        self.KoreanClick_DigitalNow()
        self.KoreanClick_BuzzWord()

    def KoreanClick_Internet(self):
        self.url = 'http://www.koreanclick.com/insights/newsletter.html?copde=trend'
        self.parse()

    def KoreanClick_Topic(self):
        self.url = 'http://www.koreanclick.com/insights/newsletter.html?code=topic'
        self.parse()

    def KoreanClick_BuzzWord(self):
        self.url = 'http://www.koreanclick.com/insights/newsletter.html?code=buzzword'
        self.parse()

    def KoreanClick_DigitalNow(self):
        self.url = 'http://www.koreanclick.com/insights/newsletter.html?code=digitalnow'
        self.parse_digital()

    def parse(self):
        try :
            while (True):
                try :
                    url = requests.get(self.url).content
                    break
                except Exception as e :
                    logging.info("KCI request error : {}".format(e))
                    continue

            soup = BeautifulSoup(url, 'html.parser')
            temp = soup.select('table')[2].select('tr')

            for n, i in enumerate(temp) :
                title = temp[n+1].select_one('.tb_txt')
                href = title.select_one('a')['href']
                date = temp[n+1].select('.tb_txt_center')[2].text
                self.finished.emit(title.text, href, date)
                logging.info("KoreanClick_Internet Emit")
                if n == self.howMany-1 :
                    break
        except Exception as e:
            logging.info(">>>>> KoreanClick.py error: {}".format(e))
            pass

    def parse_digital(self):
        try :
            while(True):
                try :
                    url = requests.get(self.url).content
                    break
                except Exception as e:
                    logging.info("parse_digital request error : {}".format(e))
                    continue
            soup = BeautifulSoup(url, 'html.parser')
            temp = soup.select('table')[2].select('tr')

            for n, i in enumerate(temp) :
                title = temp[n+1].select_one('.tb_txt')
                href = title.select_one('a')['href']
                date = temp[n+1].select('.tb_txt_center')[1].text
                self.finished.emit(title.text, href, date)
                logging.info("KoreanClick_Internet Emit")
                if n == self.howMany-1 :
                    break


        except Exception as e :
            logging.info((">>>>> def parse_digital() error : {}".format(e)))
            pass


if __name__ == "__main__" :
    KoreanClick(5).run()