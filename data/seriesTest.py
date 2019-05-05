# pip install matplotlib    #차트 그리는 모듈
# pip install pandas_datareader

from pandas import Series

# Series1 선언
series1 = Series([4234, 7876, 2313, 5678, 3455])    # 리스트 형태의 1차원 자료 구조
# print(series1)

# 총 개수
# print('count : ', series1.count())
# 요약
# print('describe : ', series1.describe())
# 인덱스 접근
# print(series1[2])

series2 = Series([4234, 7876, 2313, 5678, 3455], index = ['2018', '2019', '2020','2021', '2022'])    # 리스트 형태의 1차원 자료 구조
# print(series2)

# 인덱스 순회
# for date in series2.index :
#     print(date)

# 값 순회
# for val in series2.values :
#     print(val)

# Series3 선언
series_g1 = Series([10, 20, 30], index = ['n1', 'n2', 'n3'])
series_g2 = Series([60, 50, 40], index = ['n3', 'n2', 'n1'])

# series 병합 & 계산
sum = series_g1 + series_g2
mul = series_g1 * series_g2
cal = (series_g1 * series_g2) * 0.5

print(sum)  # 같은 인덱스 값끼리 계산한다.
print(mul)
print(cal)