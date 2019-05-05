from bs4 import BeautifulSoup
import requests

s = requests.Session()
req = s.get('https://www.naver.com')  #PUT(FETCH), DELETE, GET, POST
#print('1', req.text)

req = s.get('http://httpbin.org/cookies', cookies = {'from' : 'myName'})
#print(req.text)

url = 'http://httpbin.org/get'
headers = {'user-agent' : 'myPythonApp'}

r = s.get(url, headers = headers)
#print(r.text)

s.close() #추후 버튼을 누르는 등 누적적인 작업을 할 때에는 리소스가 낭비되기 때문에 반드시 close를 해 주어야 한다.

with requests.Session() as s :
    r = s.get('https://www.naver.com')
    print(r.text)