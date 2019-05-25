import FinanceDataReader as fdr
import pandas as pd
import datetime
import sqlite3

# pandas, pandas_datareader 설치
try :
    with sqlite3.connect("databases/sqlite2.db") as conn :
        # 조회 시작 시간 & 마감시간
        start = datetime.datetime(2018, 2, 1)
        end = datetime.datetime(2018, 3, 3)

        # google 정보 호출
        gs = fdr.DataReader("090430", start, end)    # 아모레퍼시픽 주가 읽기

        print(gs)


        # 인덱스 출력
        # print(gs.index)

        # Column 출력
        # print(gs['Open'])

        # Row 출력
        # print(gs.ix['2018-02-01'])

        # Index to Column
        gs['Date'] = gs.index   # Date라는 새로운 column을 만들어서 거기에 gs.index 값을 넣어라

        # 인덱스 재설정
        gs.index = range(1, (len(gs.index)+1))

        print(gs)
        print(gs.loc[gs['Date'] == '2018-02-01'])   # 원하는 행 값 기준 찾기

        # pandas to Database(to_sql)
        gs.to_sql("AMORE", conn, if_exists = 'replace', index = True, index_label= 'id')  # fail : 테이블이 있으면 아무것도 안함, replace : 기존 자료가 있으면 지우고 새로운걸 넣는다., append : 기존에 있던거 두고 그 뒤에 추가
        # index 넣어주겠다. 그리고 그 인덱스 이름은 'id'다.
        conn.commit()

        # pandas read Database(read_sql) 전체 조회
        df = pd.read_sql(("SELECT * FROM AMORE"), conn) # index_col = 'id'
        print(df)

        # pandas read Databse(read_sql) 조건조회
        df = pd.read_sql(("SELECT * FROM AMORE WHERE id = ?"), conn, params = (1, ), index_col = 'id')
        print(df)



finally :
    print("Dataframe SQL Work Complete!")