from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open('cars.html', encoding='utf-8')

soup = BeautifulSoup(fp, 'html.parser')

def car_func(selector) : #selector을 매개변수로 받음
    print("car func : ", soup.select_one(selector).string)

car_func('#gr')
car_func("li[id = 'gr']")
car_func('li:nth-of-type(4)')

print(soup.select('li')[3].string)

car_lambda = lambda q : print('car_lambda : ', soup.select_one(q).string) #람다식
#함수명 = lambda 매개변수 : 함수
car_lambda('li')