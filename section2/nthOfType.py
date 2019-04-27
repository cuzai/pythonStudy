from bs4 import BeautifulSoup

fp = open('food-list.html', encoding='utf-8')

soup = BeautifulSoup(fp, 'html.parser')

li = soup.select('li:nth-of-type(4)')[1] # nth-of-list(숫자)직계 자식들 중에서 내가 원하는 몇 번째 순서를 지정해서 갖고올 수 있는 선택자
print('nth-of-type : ', li.string)

li = soup.select_one('#ac-list > li:nth-of-type(4)') #id가 ac-list인 것 자식 중 리스트:4번째
print(li.string)

li = soup.select('#ac-list > li[data-lo=cn]') #select는 리스트로 반환한다.
print(li[0].string) # 리스트이므로 인덱스로 접근 要

li = soup.select('#ac-list > li.alcohol.high') #선택자로 활용할 때에는 띄어쓰기 안됨 .으로 띄어쓰기 표현 要. ※ id는 #으로 표현
print(li[0].string) # 리스트이므로 인덱스로 접근 要

param = {'data-lo':'cn', 'class':'alcohol'} #딕셔너리 형태로 파라미터 저장
li = soup.find('li', param) # 리스트 중에서 data-lo가 cn이고 class가 alcohol인 애를 찾아라
print(li.string)

li = soup.find(id = 'ac-list').find('li', param)
print(li.string)

for i in soup.find_all('li') :
    if (i['data-lo'] == 'us') :
        print('for : ', i.string)
