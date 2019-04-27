import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request

imgUrl = "http://imgnews.naver.net/image/002/2017/03/13/0002026985_001_20170313153101670.jpg"
htmlUrl = "http://google.com"

savePath = "C:/Users/cuzai/Desktop/Web_Crawling/section2/cat.png"
savePath2 = "C:/Users/cuzai/Desktop/Web_Crawling/section2/index.html"

urllib.request.urlretrieve(imgUrl, savePath)
urllib.request.urlretrieve(htmlUrl, savePath2)


print("다운로드 완료")
