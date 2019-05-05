import simplejson as json
from tinydb import TinyDB, Query

db = TinyDB('databases/database.db')

users = db.table('users')
todos = db.table('todos')

# user 테이블 출력
# for n, item in enumerate(users) :
#     if n is not 0 :
#         print('-'*100)
#     print('name : ', item['name'])
#     print('user name : ', item['username'])
#     print('city : ', item['address']['city'])
#     print('phone : ', item['phone'])

# 연결 관계 출력
# for item in users :
#     print(item['username'])
#     for todo in todos :
#         if todo['userId'] == item['id'] :
#             print('{}({})'.format(todo['title'], todo['completed']))
#     print('-'*100)
#



# 쿼리 객체
# SQL = Query()
Users = Query()
Todos = Query()

# row 수정
users.update({'username' : 'kim'}, Users.id == 3)

user_3 = users.search(Users.id == 3) # >, < 등등 사용 가능
print(user_3)

# 삭제
users.remove(Users.id == 3)

db.close()