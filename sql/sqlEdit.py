import pymysql

conn = pymysql.connect(host = 'localhost', user = 'cuzaiPy', password = '1111!', db = 'python_app1', charset = 'utf8')

try :
    with conn.cursor() as c :
        # 데이터 수정1
        c.execute("UPDATE users SET username = %s WHERE id = %s", ('niceman', 1))

        # 데이터 수정2
        c.execute("UPDATE users SET username = '%s' WHERE id = '%d'" %('good boy', 2))

        # 중간데이터 확인1
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall() :
            print(row)

        # 데이터 삭제1
        c.execute("DELETE FROM users WHERE id = %s", (1,))

        # 데이터 삭제2
        c.execute("DELETE FROM users WHERE id = '%d'" %(2, ))


    conn.commit()

finally:
    conn.close()