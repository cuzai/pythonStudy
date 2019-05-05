import urllib.request
from bs4 import BeautifulSoup
import os.path  # 파일의 경로를 확인


# 다운로드 URL
url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
saveName = 'forecast.xml'

if not os.path.exists(saveName) :
    urllib.request.urlretrieve(url, saveName)

# BS 파싱
xml = open(saveName, 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'html.parser')

# 지역 확인
info = {}
for location in soup.select('location') :
    loc = location.select_one('city').string
    # print(loc)
    weather = location.select('tmn')
    # print(weather)

    if not (loc in info) :
        info[loc] = []
    for tmn in weather :
        info[loc].append(tmn.string)

# print(info)
# print(info.keys())
# print(list(info.keys()))
# print(info.values())

# 각 지역별 날씨 텍스트 쓰기
with open('forecast.txt', 'wt') as f :
    for loc in sorted(info.keys()) :    #리스트를 오름차순으로 정렬
        f.write(loc)
        for n in info[loc] :
            f.write(" "+ n)
        f.write('\n')