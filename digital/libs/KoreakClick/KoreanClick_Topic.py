import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QThread, pyqtSignal

class KoreanClick_Topic(QThread) :
    finished = pyqtSignal(str, str, str)
    def __init__(self, howMany):
        super().__init__()
        self.url = 'http://www.koreanclick.com/insights/newsletter.html?code=topic'
        self.howMany = howMany

    def run(self):
        url = requests.get(self.url).content
        soup = BeautifulSoup(url, 'html.parser')
        temp = soup.select('table')[2].select('tr')

        for n, i in enumerate(temp):
            title = temp[n + 1].select_one('.tb_txt')
            href = title.select_one('a')['href']
            date = temp[n + 1].select('.tb_txt_center')[2].text
            self.finished.emit(title.text, href, date)
            if n == self.howMany - 1:
                break

if __name__ == "__main__":
    KoreanClick_Topic().run()
