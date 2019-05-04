import pandas

# 기본 읽기
# df = pandas.read_csv('csv_s1.csv')
# print(df)


# 행 스킵
# df = pandas.read_csv('csv_s1.csv', skiprows = [0, 1])   #원하는 인덱스를 넣어서 행을 생략해줄 수 있다.
# print(df)


# 행 스킵, 헤더 생략
# df = pandas.read_csv('csv_s1.csv', skiprows = [0], header = None)   # 맨 첫 행을 헤더로 지정하지 않는다.
# print(df)


# 헤더 정의
# df = pandas.read_csv('csv_s1.csv', skiprows = [0], header = None, names = ['Month', 2013, 2014, 2015])  #임의로 헤더를 넣어준다.
# print(df)


#인덱스 컬럼 정의
# df = pandas.read_csv('csv_s1.csv', skiprows = [0], header = None, names = ['Month', 2013, 2014, 2015], index_col = [0]) # 몇번째 열을 인덱스로할 지 정함
# print(df)


# 특정 값 치환
# df = pandas.read_csv('csv_s1.csv', skiprows = [0], header = None, names = ['Month', 2013, 2014, 2015], index_col = [0],
#                      na_values = ['JAN'])
# print(pandas.isnull(df))


#실습 정리 및 인덱스 재정의
# df = pandas.read_csv('csv_s1.csv', skiprows = [0], header = None, names = ['Month', 2013, 2014, 2015])
# print(df)
# print(df.index)
# print(list(df.index))
# print(df.index.values.tolist())
# print(df.rename(index = {0 : 'aa',1 : 'bb', 2 : 'cc'}))
# print(df.rename(index = lambda i : i + 1))


# 읽기
df2 = pandas.read_csv('csv_s2.csv', sep = ';', skiprows = [0], header = None, names = ["First name",  "Test1", "Test2", "Test3",  "Final", "Grade"])
# print(df2)


# 컬럼 내용 변경
# df2['Grade'] = df2['Grade'].str.replace('C', 'A++')
# print(df2)


#평균 컬럼 추가
# df2['Avg'] = df2[['Test1', 'Test2', 'Test3', 'Final']].mean(axis = 1)   # axis = 1 일 경우는 가로 방향으로, 0일 경우에는 세로 방향으로
# print(df2)


# 합계 컬럼 추가
df2['Sum'] = df2[['Test1', 'Test2', 'Test3', 'Final']].sum(axis = 1)
print(df2)