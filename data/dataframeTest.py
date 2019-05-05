from pandas import Series, DataFrame

# 데이터프레임은 딕셔너리의 형태를 갖는다.

r_data = {'City' : ['서울', '대전', '대구', '부산'], 'Total1' : [55000, 49000, 52000, 50000], 'Total2' : [12000, 45000, 78000, 450000]}
i_data = ['One', 'Two', 'Three', 'Four']

d_frame = DataFrame(r_data, index = i_data)
# print(d_frame)
# print(d_frame.index)
# print(d_frame.values)
# print(d_frame['City'])  # 열 기준으로 가져오기. type는 series
# print(d_frame.ix['One'])    # 행 기준으로 가져오기. type는 series

# 값 순회
for e in d_frame.values :
    for n, i in enumerate(e) :
        print(n, i)