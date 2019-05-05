import pandas as pd

df = pd.read_excel('excel_s1.xlsx', header = 0)
# print(df)

# 컬럼 값 수정
# print(df['State'])
# df['State'] = df['State'].str.replace(' ', '|')
# print(df)

# 평균 컬럼 추가
# df['Average'] = df[['2003', '2004', '2005']].mean(axis = 1).round(2)    # round() 소수점 몇째자리까지
# print(df)

# 합계 추가
# df['Sum'] = df[['2003', '2004', '2005']].sum(axis = 1)
# print(df)

# 최대값
# print(df[['2003', '2004', '2005']].max(axis = 0))

# 최소값
# print(df[['2003', '2004', '2005']].min(axis = 0))

# 상세정보
print(df.describe())

df.to_excel('result.xlsx', index = None)