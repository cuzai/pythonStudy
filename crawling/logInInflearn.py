import requests
from bs4 import BeautifulSoup
import os, errno
from urllib import request

LOGIN_INFO = {
    'log' : 'cuzai',
    'pwd' : 'ha9317je'
}

def downImg(url) :
    path = 'C:/Users/cuzai/Desktop/Web_Crawling/badge'
    try :
        os.makedirs(path)
    except OSError as o :
        if o.errno != errno.EEXIST :
            raise
    fileName = os.path.join(path, "badge.png")
    request.urlretrieve(url, fileName)



with requests.Session() as s :
    login_req = s.post('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F', data = LOGIN_INFO)
    #print(login_req.text)

    if login_req.status_code == 200 and login_req.ok :
        url = s.get('https://www.inflearn.com/members/cuzai/')
        url.raise_for_status()
        soup = BeautifulSoup(url.text, 'html.parser')
        #print(soup)
        img = soup.select_one('.tip.ajax-badge')
        imgSrc = img.select_one('img')['src']
        downImg(imgSrc)

