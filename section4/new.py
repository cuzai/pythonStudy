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
    weather = location.select_one('tmn')
    # print(weather)

    if not (loc in info) :
        info[loc] = []
    for tmn in weather :
        info[loc].append(tmn.string)

print(info)

# 각 지역별 날씨 텍스트 쓰기
