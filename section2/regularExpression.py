from bs4 import BeautifulSoup
import sys
import io
import re #regex, 정규 표현식(regular expression) string 자료형을 파싱할 때 주로 사용

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = """
<html>
<body>
    <ul>
    <li><a id = "naver" href = "http://www.naver.com">naver</a></li>
    <li><a href = "http://www.daum.net">daum</a></li>
    <li><a href = "https://www.google.com">google</a></li>
    <li><a href = "https://www.tistory.com">tistory</a></li>
    </ul>
</body>
</html>
"""

soup = BeautifulSoup(url, "html.parser")
a = soup.find('a', string = "naver")
print(a.string)

a = soup.find(id = 'naver') # id는 페이지상에서 유일한 값
print(a.string)

li = soup.find_all(href = re.compile(r"^https://")) # 정규표현식 사용. r은 raw string을 말하는 것으로 파이썬에서 /사용 시 좀 복잡한걸 해결하기 위함인데 찾아봐라
for i in li :
    print(i.attrs["href"])

li = soup.find_all(href = re.compile(r'da')) #da가 들어가 있는 href를 찾아라
for i in li :
    print(i.attrs['href'])
