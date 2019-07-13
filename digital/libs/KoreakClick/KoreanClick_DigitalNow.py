import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QThread, pyqtSignal

class KoreanClick_DigitalNow(QThread) :
    finished = pyqtSignal(str, str)
    def __init__(self, howMany):
        super().__init__()
        self.url = 'http://www.koreanclick.com/insights/newsletter.html?code=digitalnow'
        self.howMany = howMany

    def run(self):
        url = requests.get(self.url).content
        soup = BeautifulSoup(url, 'html.parser')
        temp = soup.select('.tb_txt')
        for n, i in enumerate(temp) :
            title = i.text
            href = soup.select('.tb_txt > a')[n]['href']
            self.finished.emit(title, href)
            if n == 4 :
                break

if __name__ == "__main__":
    KoreanClick_DigitalNow().run()