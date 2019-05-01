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

df = pandas.read_csv('csv_s1.csv', skiprows = [0], header = None, names = ['Month', 2013, 2014, 2015], index_col = [0]) # 몇번째 열을 인덱스로할 지 정함
print(df)

