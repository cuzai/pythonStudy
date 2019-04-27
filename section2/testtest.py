from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open('naver.html', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

li = soup.select('#PM_ID_themecastBody > div.flick-panel')

print(li)
