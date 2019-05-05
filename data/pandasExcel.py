#pip install xlrd / pip install openpyxl

import pandas as pd

# 기본 읽기

# df = pd.read_excel('excel_s1.xlsx', sheet_name = 0) # 디폴트는 자동으로 0 넣어줌

# print(df.head())    # 수많은 데이터 중 상위 몇개만 보여줌
# print(df.tail())     # 하위 몇 개만 보여줌

# 행과 Footer 스킵
# df = pd.read_excel('excel_s1.xlsx', skiprows = [0], skipfooter = 10) # skip_footer : 하위에서 10개를 제외하고 가져오겠다.
# print(df)

# 헤더 정의(1)
# df = pd.read_excel('excel_s1.xlsx', header = 0)
# print(df)
# print(list(df)) # 헤더 부분만 리스트로 돌려줌
# print(list(df.columns.values))

# 헤더 정의(2)
# df = pd.read_excel('excel_s1.xlsx', skiprows = [0], header = None, names = ['state', '2003', '2004', '2005'])
# print(df)

# 특정 값 치환
# df = pd.read_excel('excel_s1.xlsx', header=0, na_values = '...', converters = {'2003' : lambda i : i if i > 60000 else None}) # 특정 열 중에서 특정 값 찾아서 치환
# print(df)

# 실습 정리 및 인덱스 재정의
df = pd.read_excel('excel_s1.xlsx', header = 0)
print(df.rename(index = lambda i : i+1).index)