import sqlite3

# DB 생성
conn = sqlite3.connect('databases/sqlite1.db')

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 1개 row 선택
# print(c.fetchone()) # 최초에는 가장 첫번째 row에 커서
# print(c.fetchone()) # 그 다음에는 자동으로 다음 row

# print(c.fetchmany(size = 4))    # 3번쨰 row부터 4개 선택

# 전체 row 선택
# print(c.fetchall()) # 7 번째부터 전체 다 가져옴
# print(c.fetchone()) # 더이상 커서가 가르킬 row 가 없으므로 None 반환

# 순회1
# for row in c.fetchall() :
#     print(row)

# 순회2
# for row in c.execute("SELECT * FROM users") :
#     print(row)


# 조건 조회1
# param1 = (1,)
# c.execute("SELECT * FROM users WHERE id=?", param1)
# print(c.fetchall())

# 조건 조회2
# param2 = 1
# c.execute("SELECT * FROM users WHERE id = '%s'" % param2)   # %s, %d, %f 같은 파이썬 내부 매핑이랑 상관 없음 SQL에서는 문자든 숫자든 그냥 무조건 %s
# print(c.fetchall())

# 조건 조회3
# c.execute("SELECT * FROM users WHERE id = :id", {'id' : 1})
# print(c.fetchall())

# 조건 조회4
# param4 = (1, 4)
# c.execute("SELECT * FROM users WHERE id IN(?, ?)", param4)
# print(c.fetchall())

# 조건 조회5
# c.execute("SELECT * FROM users WHERE id = :id1 OR id = :id2", {'id1' : 1, 'id2' : 4})
# print(c.fetchall())

# dump
with conn :
    # dump 출력
    with open('data/test.dump', 'w') as f :
        for line in conn.iterdump() :
            f.write('%s\n' % line)
        print("Dump write complete")