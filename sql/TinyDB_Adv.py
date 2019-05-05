import simplejson as json
from tinydb import TinyDB, Query, where

db = TinyDB('databases/database1.db')

# db.insert({'name' : 'park', 'email' : 'cuzai@naver.com'})   #json(dict), 1 개씩
# db.insert_multiple([{'name' : 'lee', 'email' : 'lee@naver.com'}, {'name' : 'kim', 'email' : 'kim@naver.com'}])  #jsonArray(dict) [{}, {}, {}]

SQL =Query()

el = db.get(SQL.name == 'kim')  # find 같은 느낌
ll = db.search(SQL.name == 'kim')   # 리스트로 돌려줌, find_all 같은 느낌

# id값 출력
# print(el)
# print(el.doc_id)
# print(ll)


# 데이터 수정
# db.update({'email' : 'test1@google.com'})

# 데이터 수정 및 추가
db.upsert({'email' : 'test1@naver.com', 'log_in' : True}, SQL.name == 'park')   #update + insert

# 데이터 삭제
db.remove(SQL.name == 'lee')


# 전체 조회
print(db.all())
