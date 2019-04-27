from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html>
<body>
    <ul>
    <li> <a href = "http://www.naver.com">naver</a> </li>
    <li><a href = "http://www.daum.net">daum</a></li>
    <li><a href = "http://www.google.com">google</a></li>
    <li><a href = "http://www.tistory.com">tistory</a></li>
    </ul>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")  # 해당 엘리먼트를 한번에 가지고 옴(이 예제에서는 a태그)
print(type(links))

for a in links:
    #print("a : ", type(a), a)
    href = a.attrs['href'] # attrs : 직접 접근으로 속성을 활용할 수 있는데 return을 딕셔너리로 해 준다. key와 value로 이루어져 있다.
    txt = a.string
    print("txt : {} / href : {}".format(txt, href))

choose_all = soup.find_all('a', string = "naver" ) # 조건에 맞는 애 다 가지고 옴
print("choose_all : ", choose_all)

choice = soup.find('a') # 조건에 맞는 애 하나만 가지고 옴
print("choice : ", choice)

links_limit = soup.find_all('a', limit = 3) # 가지고 오는 갯수에 제한을 검
print("limit : ", links_limit)
