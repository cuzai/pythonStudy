from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

index2 = """
<!DOCTYPE html>
<html>
<head>
  <title>HTML - 수업소개</title>
  <meta charset="utf-8">
</head>

<body>
  <h1><a href="index.html">HTML</a></h1>
  <p>문단1</p>
  <p>문단2</p>
<ol>
  <li><a href="1.html">기술 소개</a></li>
  <li><a href="2.html">기본 문법</a></li>
  <li><a href="3.html">하이퍼 텍스트와 속성</a></li>
  <li><a href="4.html">리스트와 태그의 중첩</a></li>
</ol>

<h2>제목</h2>

  내용
</body>

</html>
"""

soup = BeautifulSoup(index2, 'html.parser') #BeautifulSoup(파싱 원하는 html, 'html.parser')

print("pettify : ", soup.prettify())  #htlm을 보기 좋게 표현해 줌
h1 = soup.html.body.h1  #태그 이용 파싱
print("h1 : ", h1)  #태그까지 같이 딸려 나옴
print("h1.string : ", h1.string) #태그 없이 스트링 문자열 출력

p1 = soup.html.body.p
print("p1 : ", p1)
p2 = p1.next_sibling.next_sibling   #next_sibling : 태그간 이동 시 활용. 한번만 써주면 줄바꿈으로 인해 숨겨진 \n을 출력하므로 두 번 써준다.
print("p2 : ", p2)
p3 = p1.previous_sibling.previous_sibling
print("p3", p3)