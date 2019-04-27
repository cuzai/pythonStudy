from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
import os # 윈도우 즉 OS단의 명령어를 사용하고자 할 때 임포트
import errno

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
search = input("input keyword : ")
quote = parse.quote_plus(search)
url = base + quote
#print(url)


req = request.urlopen(url).read()
path = os.path.join("C:/Users/cuzai/Desktop/Web_Crawling", search)

#내 혼자 만든 버전
try:
    os.makedirs(path) #경로 만들어라. 최초에 만들 땐 문제없이 만들어짐. 하지만 한번경로가 생성된 후 다시 프로그램 실행시키면 이미 존재하는 경로라 새로 만들 수 없다는 에러가 뜸
except OSError as e : #우선 OS 에러를 다 쌩까되
    if e.errno == errno.EEXIST : #이미 존재하는 경로라는 에러의 경우에는 말 해줘라
        #print("Path already exists")
        pass
    else : #그 외에는 에러 일으켜라(디스크 공간 부족, 권한 없음 등)
        print("Failed to create the dir")
        raise

#수업 버전
"""try :
    if not(os.path.isdir(savePath)) : #savePath가 존재하지 않으면
        os.makedirs(os.path.join(savePath)) #savePath라는 경로를 만들어라
except OSError as e :
    if e.errno != errno.EEXIST :
        print("폴더만들기 실패")
        raise"""

soup = BeautifulSoup(req, 'html.parser')
#print(soup.prettify())

img_list = soup.select(".photo_grid._box a>img")

for n, i in enumerate(img_list, 1) :
    href = i['data-source']
    name = i['alt']
    #print("{}. {} : {}".format(n, name, href))
    fileName = os.path.join(path, search+str(n)+'.jpg')
    #print(fileName)
    request.urlretrieve(i['data-source'], fileName)

print("Download Complete")