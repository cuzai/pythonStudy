import simplejson as json
from tinydb import TinyDB
from tinydb.storages import MemoryStorage

# 파일 DB 생성
db = TinyDB('databases/database.db', default_table = 'users')



# 메모리 DB 생성 # 1회용으로 메모리에 담아서 쓸 수 있다.
# db = TinyDB(storage = MemoryStorage, default_table = 'users')

# 테이블 선택
users = db.table('users')
todos = db.table('todos')   # 없으면 만들어준다.

# 테이블에 데이터 삽입
# users.insert({'name' : 'Park', 'email' : 'cuzai@naver.com'})
# totos.insert({'name' : 'homework', 'iscomplete' : False})


# 테이블 데이터 전체 삽입
with open('data/users.json', 'r') as infile :
    r = json.loads(infile.read())
    for u in r :
        users.insert(u)

# 테이블 데이터 전체 삽입2
with open('data/todos.json', 'r') as infile :
    read = json.loads(infile.read())
    for i in read :
        todos.insert(i)

# 전체 데이터 출력
# print(users.all())
# print(todos.all())

# 테이블 목록
# print(db.tables())

# 전체 데이터 삭제(개별 테이블별로)
# users.purge()   # db.purge_table('users')와 똑같다.
# todos.purge()

# db.purge_tables()   # 테이블 상관없이 테이븖까지 전체 다 지워버림


db.close()