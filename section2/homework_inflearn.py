from bs4 import BeautifulSoup
from urllib import request
import os
import errno

url = "https://www.inflearn.com/"
req = request.urlopen(url).read()
soup = BeautifulSoup(req, 'html.parser')
#print(soup)

slides = soup.select('.slides')
#print(len(slides)) #슬라이드 총 5개, 문제없음

# 0. 기본 경로
basePath = "C:/Users/cuzai/Desktop/Web_Crawling/test2"

# 텍스트 다운 함수
def downTxt(param, page) :

    for n, i in enumerate(param, 1):
        title = i.select_one('.block_title a').string

        txtPath = os.path.join(basePath, page)  #서비스별 경로 설정
        print(txtPath)
        try:
            os.makedirs(txtPath)
        except OSError as o:
            if o.errno != errno.EEXIST:
                raise

        with open(txtPath + '/' + page + '.txt', 'a') as f:
            f.write(str(n) + ". " + title + '\n\n')

# 이미지 다운 함수
def downImg(param, page) :
    for n, i in enumerate(param, 1) :
        img = i.select_one('img')['src']
        title = i.select_one('.block_title a').string
        if ':' in title :   #타이틀에 있는 특수문자 제거
            title = title.replace(':', '-')

        imgPath = os.path.join(basePath, page)  #서비스별 경로 설정
        try :
            os.makedirs(imgPath)
        except OSError as o :
            if o.errno != errno.EEXIST :
                raise

        fileName = os.path.join(imgPath, str(n) + '. '+ title + ".png")
        request.urlretrieve(img, fileName)



# 1. 나만의 웹서비스 만들기
webService = slides[1].select('li')
# 1-1. 텍스트 다운받기
downTxt(webService, 'web')
# 1-2. 이미지 다운받기
downImg(webService, 'web')

# 2. 요즘 잘나가는 프론트엔드
frontend = slides[2].select('li')
#2-1. 텍스트 다운
downTxt(frontend, 'front')
# 2-2. 이미지 다운
downImg(frontend, 'front')