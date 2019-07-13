import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QThread, pyqtSignal
import logging

class KoreanClick_Internet(QThread) :
    finished = pyqtSignal(str, str, str)
    def __init__(self, howMany):
        logging.info("KoreanClick_Internet __init__")
        try :
            super().__init__()
            logging.info("1")
            self.url = 'http://www.koreanclick.com/insights/newsletter.html?copde=trend'
            logging.info("1")
            self.howMany = howMany
            logging.info("1")
        except Exception as e:
            logging.info(e)
            pass

    def run(self):
        logging.info("KoreanClick_Internet run")
        try :
            while (True):
                try :
                    url = requests.get(self.url).content
                    logging.info("1")
                    break
                except Exception as e :
                  logging.info("KCI request error".format(e))

            soup = BeautifulSoup(url, 'html.parser')
            logging.info("1")
            temp = soup.select('table')[2].select('tr')
            logging.info("1")

            for n, i in enumerate(temp) :
                title = temp[n+1].select_one('.tb_txt')
                logging.info("1")
                href = title.select_one('a')['href']
                logging.info("1")
                date = temp[n+1].select('.tb_txt_center')[2].text
                logging.info("1")
                self.finished.emit(title.text, href, date)
                logging.info("KoreanClick_Internet Emit")
                if n == self.howMany-1 :
                    break
            print()
        except Exception as e:
            logging.info(e)

if __name__ == "__main__":
    KoreanClick_Internet(5).run()

