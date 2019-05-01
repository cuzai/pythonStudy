import simplejson as json

#Dict(Json) 선언

data =  {}
data['people'] = []
data['people'].append({
    'name' : 'park',
    'website' : 'naver.com',
    'from' : 'seoul'
})

data['people'].append({
    'name' : 'kim',
    'website' : 'daum.net',
    'from' : 'busan'
})

data['people'].append({
    'name' : 'lee',
    'website' : 'google.com',
    'from' : 'china'
})

# print(data)

# dict(json) → str
e = json.dumps(data, indent = 4)    # json(딕셔너리) 오브젝트를 텍스트 파일로 변환, indent = json파일 정렬 시 들여쓰기 depth
# print(type(e))        # dumps(dump string) : 텍스트로 직렬화, dump : 열린 파일과 유사한 객체로 직렬화
# print(e)

# str → dict(json)
d = json.loads(e)   # str 오브젝트를 원래 자료형으로 변환
# print(type(d))
# print(d)

with open('member.json', 'w') as outfile:
    outfile.write(e)

# jsoneditoronline.org 에서 json 파일을 보기 좋게 바꿔준다.

with open('member.json', 'r') as infile :
    r = json.loads(infile.read())
    # print(type(r))
    # print(r)

    for i in r['people'] :
        print(i['name'])
        print(i['website'])
        print(i['from'])
        print()