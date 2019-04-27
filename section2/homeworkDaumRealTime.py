from bs4 import BeautifulSoup
from urllib import request

url = "https://www.daum.net/"
req = request.urlopen(url).read()

soup = BeautifulSoup(req, 'html.parser')
#print(soup)

hot = soup.select('.hotissue_builtin li')

for n, i in enumerate(hot, 1) :
    print("{}위 {} : {}".format(n, i.select_one('a').string, i.select_one('a').attrs['href']))
