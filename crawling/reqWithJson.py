import requests

with requests.session() as s :
    r = s.get('http://httpbin.org/get', stream = True)
    #print(r.status_code)    #현재 상태 코드. 404Forbidden 같은 것들
    #print(r.ok) #현재 서버 상태가 ok인지 확인

    #https://jsonplaceholder.typicode.com

with requests.Session() as s :
    r = s.get('https://jsonplaceholder.typicode.com/posts/1')
    print(type(r))  #<class 'requests.models.Response'>
    print(r.encoding)
    print(r.json()) #json response일 경우 딕셔너리 타입으로 바로 변환
    print(r.json().keys())  #딕셔너리에서 키값만 가져오는 파이썬의 메서드
    print(r.json().values())    #value값만 가져오는 파이썬의 메서드
    print(r.encoding)   #현재 html이 어떤걸로 인코딩 되어있나
    print(r.content)
    print(r.raw)    #로우데이터 형태로
