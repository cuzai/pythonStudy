from bs4 import BeautifulSoup
from urllib import request
#import urllib.parse #한글을 유니코드로 바꿔주는 모듈 및 함수. 아래 참조

#res = urllib.parse.quote_plus("추천-강좌") # 추후에 url+res 작업을 통해 최종 url 만들어서 사용
#print(res)

url = "https://www.inflearn.com/"
req = request.urlopen(url).read()
soup = BeautifulSoup(req, 'html.parser')
#print(soup)

recom = soup.select('ul.slides')[0]
#print(recom)

for e, i in enumerate(recom, 1) :
    print("{}. {}".format(e, i.select_one('.block_title > a').string))