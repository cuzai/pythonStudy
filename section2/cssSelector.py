from bs4 import BeautifulSoup
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
<div id = "main">
    <h1>강의목록</h1>
    <ul class = "lecs">
        <li>Java 초고수 되기</li>
        <li>파이썬 기초 프로그래밍</li>
        <li>파이썬 머신러닝 프로그래밍</li>
        <li>안드로이드 블루투스 프로그래밍</li>
    </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
h1 = soup.select("div#main > h1") #div 中 아이디가 main인 애를 찾고 그 하위에 h1태그를 가져와라
print("h1 = ", h1) #리스트로 반환. 따라서 h1.string이 먹히지 않는다. for문을 통해 추출하던가
                   # ex> for z in h1 :
                   #        print(z.string)
h1 = soup.select_one("div#main > h1")                   # 아니면 하나만 갖고 올때는 걍 select_one을 써라
print("h1 : ", h1.string)

list_li = soup.select("div#main > ul.lecs > li") # div 中 아이디가 main인 애를 찾고 그 하위에 ul태그 中 클래스가 lecs인 애 하위에서 li를 가지고 와라
for z in list_li :
    print(z.string) # 일반적으로 딱 하나밖에 없는건 생략해도 된다. 예를 들어 div#main 에서 어차피 main이란 아이디를 가진 놈은 하나뿐이니 생략해도 된다는 것. ul도 마찬가지. 걍 #main > .lecs > li 해도 된다는 것
