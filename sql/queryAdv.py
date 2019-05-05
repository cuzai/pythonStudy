import simplejson as json
from tinydb import TinyDB, Query, where

db = TinyDB('databases/database.db')

users = db.table('users')
todos = db.table('todos')

Users = Query()
Todos = Query()

# 여러가지 조회방법
# print(users.search(Users.id == 7))
# print(users.search(Users['id'] == 7))
# print(users.search(where('id') == 7))
# print(users.search(Query()['id'] == 7))
# print(users.search(where('address')['zipcode'] == '90566-7771'))
# print(users.search(where('address').zipcode == '90566-7771'))

# 고급 쿼리
# print(users.search(Users.email.exists()))   # 특정 키가 있는 row를 다 가져옴

# NOT
# print(users.search(~(Users.username == 'Antonette')))

# OR
# print(users.search( (Users.username == 'Antonette') | (Users.username == 'Kamren') ))

# And
# print(users.search( (Users.username == 'Antonette') & (Users.id == 2) ))

# 기타 함수
# print(len(users))   # 길이
# print(users.contains(Users.username == 'Kamren'))   # 특정 키를 갖는 게 있는지
# print(users.count(Users.username == 'Kamren'))   # 특정 키를 갖는 요소 개수


