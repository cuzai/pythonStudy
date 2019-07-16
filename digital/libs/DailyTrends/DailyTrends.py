import requests
from PyQt5.QtCore import *
from bs4 import BeautifulSoup
import logging
import re

logging.basicConfig(level = logging.INFO)

class DailyTrends(QThread) :
    finished = pyqtSignal(str, str, str, str)
    error = pyqtSignal(str)

    def __init__(self, howMany):
        logging.info("DailyTrends __init__")
        try :
            super().__init__()
            self.baseUrl = 'https://www.dailytrend.co.kr/login/'

            self.titles = []
            self.href = []

            self.logIn_Url = 'https://www.dailytrend.co.kr/wp-admin/admin-ajax.php'
            self.parseUrl = 'https://www.dailytrend.co.kr/category/business-trend/retail-ecommerce/'
            self.howMany = howMany
            self.logIn_Info = {
                        'username_or_email': 'retailrnd5',
                        'user_pass': 'fhtepqorghkwja5'
                    }
            self.logIn_Info.update({
                'action' : 'userpro_process_form',
                'template': 'login',
                'group': 'default'
            })
        except Exception as e :
            logging.info(">>>>> DailyTrends __init__ error : {}".format(e))
            pass

    def run(self):
        logging.info("DailyTrends run")
        try :
            with requests.Session() as s:
                # log in
                while (True):
                    try:
                        login_req = s.post(self.logIn_Url, data = self.logIn_Info)
                        # logging.info(login_req.status_code)
                        break
                    except Exception as e:
                        self.error.emit('dailyTrend')
                        logging.info(">>>>> DailyTrends login error = {}".format(e))
                        continue

                if (login_req.status_code == 200 and login_req.ok):
                    # go to retail & e-tail
                    while(True) :
                        try :
                            url = s.get(self.parseUrl)
                            break
                        except Exception :
                            self.error.emit('dailyTrend')
                            logging.info(">>>>> DaliyTrends parseUrl error : {}".format(e))
                            continue
                    soup1 = BeautifulSoup(url.content, 'html.parser')

                    # get article name
                    # get the link
                    article = soup1.select('article .post-item-title.grid-title a')
                    for n, i in enumerate(article):
                        link = i['href']
                        self.href.append(link)

                        # get to the link and get title. this takes some time
                        try :
                            url = s.get(link)
                        except Exception as e :
                            self.error.emit("dailyTrend")
                            logging.info(">>>>> DailyTrends individual article error : {}".format(e))
                            continue

                        soup = BeautifulSoup(url.content, 'html.parser')
                        date = soup1.select('.updated')[n].text

                        temp = soup.select_one('title')
                        p = re.compile('((\\S*\\s*)*) - 데일리트렌드')
                        m = p.search(temp.text)
                        title = m.group(1)
                        self.finished.emit("dailyTrends", title, link, date)
                        if (n == self.howMany - 1) :
                            break
        except Exception as e :
            logging.info("DailyTrends error : {}".format(e))
            pass


if (__name__ == "__main__"):
    DailyTrends(5).run()