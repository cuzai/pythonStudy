from bs4 import BeautifulSoup
from urllib import request as req

url = "https://finance.naver.com/"
res = req.urlopen(url).read().decode('euc-kr') #한글 깨질 때 사용
soup = BeautifulSoup(res, "html.parser")
#print(soup.prettify())

top = soup.select("div.aside_area.aside_popular > table.tbl_home > tbody > tr")
#print(type(top)) #class 'list'

for e, i in enumerate(top, 1) : # enumerate(리스트, 시작 인덱스) 함수는 반복문에 인덱싱을 가능하게 해 줌
     print("{}. {} : {}".format(e, i.select_one('a').string, i.select_one('td').string))