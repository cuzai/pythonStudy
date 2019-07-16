import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QThread, pyqtSignal
import logging

class KoreanClick_Internet(QThread) :
    finished = pyqtSignal(str, str, str)
    error = pyqtSignal(str)
    def __init__(self, howMany):
        logging.info("KoreanClick_Internet __init__")
        try :
            super().__init__()
            self.url = 'http://www.koreanclick.com/insights/newsletter.html?copde=trend'
            self.howMany = howMany
        except Exception as e:
            logging.info(">>>> KoreanClick Internet : {}".format(e))
            pass

    def run(self):
        logging.info("KoreanClick_Internet run")
        try :
            while (True):
                try :
                    url = requests.get(self.url).content
                    break
                except Exception as e :
                    self.error.emit("koreanClick_Internet")
                    logging.info(">>>>> KCI request error : {}".format(e))
                    continue

            soup = BeautifulSoup(url, 'html.parser')
            temp = soup.select('table')[2].select('tr')

            for n, i in enumerate(temp) :
                title = temp[n+1].select_one('.tb_txt')
                href = title.select_one('a')['href']
                date = temp[n+1].select('.tb_txt_center')[2].text
                self.finished.emit(title.text, href, date)
                if n == self.howMany-1 :
                    break
            print()
        except Exception as e:
            logging.info(">>>>> KoreanClick Internet parse error : {}".format(e))

if __name__ == "__main__":
    KoreanClick_Internet(5).run()