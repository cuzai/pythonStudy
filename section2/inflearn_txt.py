from bs4 import BeautifulSoup
from urllib import request
import os
import errno

url = "https://www.inflearn.com/"
req = request.urlopen(url).read()
soup = BeautifulSoup(req, 'html.parser')

path = "C:/Users/cuzai/Desktop/Web_Crawling/test"
try :
    os.makedirs(path)
except OSError as e:
    if e.errno != errno.EEXIST :
        raise

img_list = soup.select('.slides')[0]

for n, i in enumerate(img_list, 1) :
    # 이미지 다운
    img_name = i.select_one('.block_title > a').string
    if ':'in img_name : #파일명에 : 등 특수문자 포함 안됨
        img_name = img_name.replace(':', '-') #문자열에 특수문자 포함 된 경우 바꿔주기

    fileName = os.path.join(path, str(n) +". " + img_name + ".png")
    request.urlretrieve(i.select_one('.block_media img')['src'], fileName)
    #print(str(n)+i.select_one('.block_media img')['src'])

    #텍스트 저장
    txt_name = "Inflearn"
    with open(path+txt_name+".txt",'a') as f :
       f.write(str(n) + '. ' + img_name +'\n\n')
    print(img_name)