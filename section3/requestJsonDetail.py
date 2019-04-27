import requests, json

with requests.Session() as s :
    r = s.get('http://httpbin.org/stream/20', stream = True) #stream = True : 세션을 닫을때까지 연결이 끊기지 않게 해 준다.
    #print(type(r))  #<class 'requests.models.Response'>
    #print(r.text)  #결과값이 json처럼 생겼음
    #print(r.json()) #돌려보면 에러가 남. json처럼 생겼지만 json response가 아니란 말
    #print(r.encoding)  #인코딩도 안돼있음. None이라고 나옴
    if r.encoding == None :
        r.encoding = 'utf-8'    #우선 utf-8로 인코딩 해줌

    for line in r.iter_lines(decode_unicode=True) : #매 줄 돌면서 유니코드로 디코딩한다(?) 그냥 하면 값이 바이너리로 나옴. 디코딩 해줌으로써 str 형식으로 변환 해 주는 것
        print(line)
        b = json.loads(line) #json형식의 string을 python dictionary로 변환해준다.
        #print(b)
        print(b.keys()) #딕셔너리에서 key값 가져오는 메서드
        for i in b.keys() :
            print("key : ", i, " / value : ", b[i])    #딕셔너리 b에 key를 넣으면 상응하는 value를 돌려줌