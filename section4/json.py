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

e = json.dumps(data)
print(type(e))
print(e)