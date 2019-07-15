import sqlite3
import simplejson as json
import datetime

# db 생성
conn = sqlite3.connect('databases/sqlite1.db') # isoloation_level = None: 오토커밋에 대한 내용. None일 경우 모든 코드는 자동 커밋.
                                                                    # 이거 없을 경우 커밋 할 때마다 conn.commit() 써 줘야 함

# 메모리 DB 생성
# conn = sqlite3.connect(':memory:')

# 날짜 생성
now = datetime.datetime.now()
# print(now)

nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
# print(nowDateTime)


# sqlite3 버전확인
# print(sqlite3.version)
# print(sqlite3.sqlite_version)


# Cursor 연결
c = conn.cursor()
# print(type(c))


# 테이블 생성(SQLite3 DataType : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, username text, phone text, website text, regdate text)")   # AUTOINCREMENT : 자동 증가, PRIMARY KEY : 기본 키. 중복이 될 수 없는 값


# 데이터 삽입
c.execute('INSERT INTO users VALUES(1, "kim", "010-000-0000", "kim.co.kr", ?)', (nowDateTime,)) # 매핑은 튜플로 한다.

userList = (
    (2, "kim", "010-000-0000", "kim.co.kr", nowDateTime),
    (3, "park", "010-000-0000", "park.co.kr", nowDateTime),
    (4, "lee", "010-000-0000", "lee.co.kr", nowDateTime),
)

# c.executemany("INSERT INTO users(id, username, phone, website, regdate) VALUES(?,?,?,?,?)", userList)

with open('data/users.json', 'r') as infile :
    r = json.load(infile)
    userData = []
    for user in r :
        tup = (user['id'], user['name'], user['phone'], user['website'], nowDateTime)
        # print(tup)
        userData.append(tup)
        c.execute("INSERT INTO users VALUES(?,?,?,?,?)", tup)
    # c.executemany("INSERT INTO users(id, username, phone, website, regdate) VALUES(?,?,?,?,?)", userData)    # userData리스트를 알아서 튜플로 형변환 해 준다.


# 데이터 삭제
# print('users db delete', conn.execute('delete from users').rowcount, "rows")



conn.commit()



conn.close()

