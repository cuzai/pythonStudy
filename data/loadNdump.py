import simplejson as json

data = {}
data['people'] = []
data['people'].append({
        "name": "park",
        "from": "seoul",
        "website": "naver.com",
        "grade" : [95, 88, 66, 10]
})

data['people'].append({
        "name": "kim",
        "from": "busan",
        "website": "daum.net",
        "grade" : [100, 90, 34, 70]
})

data['people'].append({
        "name": "lee",
        "from": "china",
        "website": "google.com",
        "grade" : [45, 25, 58, 45]
})

# json 파일 쓰기(dump)
with open('member.json', 'w') as outfile :
    json.dump(data, outfile)

with open('member.json', 'r') as infile :
    r = json.load(infile)
    # print(type(r), r)
    for i in r['people'] :
        print('Name : {}'.format(i['name']))
        print('From : {}'.format(i['from']))
        print('Web : {}'.format(i['website']))
        # print('Grade : {}'.format(i['grade']))
        grade = ''
        for e in i['grade'] :
            grade = grade + ' ' +str(e)
        print('Grade : {}'.format(grade))
