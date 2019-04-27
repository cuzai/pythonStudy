from urllib import request
from urllib.parse import urlencode
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp'

values = {
    'ctxcd' : '1001'
}

print('before : ', values)

params = urlencode(values)

print("after : ", params)


url = API + '?' + params

print(url)

reqData = request.urlopen(url).read().decode('utf-8')

print(reqData)

print("done")
