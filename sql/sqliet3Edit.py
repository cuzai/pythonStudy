import sqlite3

conn = sqlite3.connect('databases/sqlite1.db')

# 커서 연결
c = conn.cursor()

# 데이터 수정1
c.execute("UPDATE users SET username = ? WHERE id =?", ('niceman', 1))  #id가 1번인놈의 username을 niceman으로 바꿔라

# 데이터 수정2
c.execute("UPDATE users SET username = :name WHERE id = :id", {'name' : 'goodman', 'id' : '2'})

# 데이터 수정3
c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('cuteboy', 3))


# 데이터 삭제1
c.execute("DELETE FROM users WHERE id = ?", (4,))

# 중간 데이터 확인
for user in c.execute("SELECT * FROM users") :
    print(user)


conn.commit()
conn.close()