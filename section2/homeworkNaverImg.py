from urllib import request
from urllib.parse import urlencode
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl1 = 'https://tvetamovie.pstatic.net/libs/1219/1219593/ed2664ae411dd869d4d0_20190130152218447.mp4-pBASE-v0-f73181-20190130152402318_10.mp4'
imgUrl2 = 'https://ssl.pstatic.net/tveta/libs/1226/1226175/7aadc1d6adb3f32d99af_20190118115250280.jpg'
saveTo1 = 'C:/Users/cuzai/Desktop/Web_Crawling/naverBannerBig.mp4'
saveTo2 = 'C:/Users/cuzai/Desktop/Web_Crawling/naverBannerSmall.png'



request.urlretrieve(imgUrl1, saveTo1)
request.urlretrieve(imgUrl2, saveTo2)
