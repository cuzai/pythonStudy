import pymysql
import simplejson as json
import datetime

# mySQL connection
conn = pymysql.connect(host = 'localhost', user = 'cuzaiPy', password = '1111!', db = 'python_app1', charset = 'utf8')

# pymysql 버전 확인
# print(pymysql.__version__)

# 데이터베이스 선택
# conn.select_db('python_app1')     # 중간에 db 바꿔주고 싶을 때

# Cursor 연결
c = conn.cursor()

# 데이터베이스 생성
# c.execute('create databases python_app2')   # 권한 있는 유저라면 DDL, DML, DCL 다 생성 가능

# 커서반환
# c.close()
# 접속 해제
# conn.close()

# 트랜젝션 시작 선언
# conn.begin()

# 커밋
# conn.commit()

# 롤백
# conn.rollback()

# 날짜 생성
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print(now)

# 테이블 생성
c.execute("CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL, \
                                            username varchar(20), \
                                            email varchar(30), \
                                            phone varchar(30), \
                                            website varchar(30), \
                                            regdate varchar(20) NOT NULL, PRIMARY KEY(id))")
# NOT NULL : 비워놓으면 안된다는 뜻
# varchar : 가변형 스트링 데이터타입
# PRIMARY KEY : 중복되면 안되는 값
# AUTO_INCREMENT : 자동 증가
# DEFAULT

try :
    with conn.cursor() as c :
        #JSON to Mysql
        with open('data/users.json', 'r') as infile :
            r = json.load(infile)
            for user in r :
                tup = (user['id'], user['username'], user['email'], user['phone'], user['website'], now)
                c.execute('INSERT INTO users VALUES(%s, %s, %s, %s, %s, %s)', tup)
        conn.commit()
finally :
    conn.close()