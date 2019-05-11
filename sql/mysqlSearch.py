import pymysql

conn = pymysql.connect(host = 'localhost', user = 'cuzaiPy', password = '1111!', db = 'python_app1', charset = 'utf8')

try :
    with conn.cursor() as c :   # conn.curser(pymysql.cursors.DictCursor)   # 기본인 튜플이 아니라 딕셔너리 형태로 리턴해준다.
        c.execute("SELECT * FROM users")
        # # 1개 row
        # print(c.fetchone())
        # # row 선택
        # print(c.fetchmany(3))
        # # 전체 row
        # print(c.fetchall())
        
        # # 순회 1
        # c.execute("SELECT * FROM users ORDER BY id DESC") # ASC : 오름차순이라는 뜻  DESC : 내림차순
        # for row in c.fetchall() :
        #     print(row)

        # # 조건 조회 1
        # param1 = (1,)
        # c.execute("SELECT * FROM users WHERE id = %s", param1)
        # print(c.fetchall())

        # # 조건 조회 2
        # param2 = 1
        # c.execute("SELECT * FROM users WHERE id = %d" %param2)  # %s로 넣어도 알아서 형변환 해 준다.
        # print(c.fetchall())

        # # 조건조회 3
        # param3 = (4, 5)
        # c.execute("SELECT * FROM users WHERE id IN(%s, %s)", param3)
        # print(c.fetchall())

        # 조건조회 4
        param4 = (4, 5)
        c.execute("SELECT username FROM users WHERE id IN('%s', '%s')" %param4) # * 대신 원하는 value 값만 추려낼수도 있다.
        print(c.fetchall())

finally :
    conn.close()