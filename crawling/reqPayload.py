#www.apistore.co.kr/api/apiList.do

import requests, json

#r = requests.get('https://api.github.com/events')
#r.raise_for_status()    #request 한 후 에러가 발생했을 때 예외를 발생시겨줌
#print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('name', 'kim', domain = 'httpbin.org', path = '/cookies')

#r = requests.get('http://httpbin.org/cookies', cookies = jar)
#r.raise_for_status()
#print(r.text)

#r = requests.get('https://github.com', timeout = 3) #서버가 바뀔때까지 3초간의 대기를 주겠다. 너무 자주 요청하면 차단당할수도 있음
#print(r.text)

#post : 파일 업로드라든지, get 방식으로 데이터를 url에 노출되면 보안 등 위협이 있음. 데이터를 서버상에 저장하는 형식
#r = requests.post('http://httpbin.org/post', data = {'name':'kim'}, cookies = jar)
#print(r.text)

#payload 데이터를 서버상에 요청할 때 담을 수 있는 것
payload1 = {'key1' : 'value1', 'key2' : 'value2'}   #dict 형태
payload2 = (('key1', 'value1'), ('key2', 'value2')) #tuple 형태

#r = requests.post('http://httpbin.org/post', data = payload2)  #form 데이터로 받음
#print(r.text)

payload3 = {'some' : 'nice'}
r = requests.post('http://httpbin.org/post', data = json.dumps(payload3))   #json으로 받음
