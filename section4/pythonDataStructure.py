# a = 'hello'
#
# print(type(a))
# print(a[0])
# print(a[0 : 3])
# print(a[-1])
#
# for i in a :
#     print(i)


# 리스트 자료형(순서o, 중복o, 수정o, 삭제o)
# 선언
a = []
b = list()
c =[0, 0, 1, 2]
d = [0, 1, 'car', 'apple', 'apartment']
e = [0, 1, ['car', 'apple', 'apartment']]    # 중첩 리스트


# 인덱싱
# print("#=======#")
# print('d- ', type(d), d )
# print('d- ', type(d), d[1] )
# print('d- ', type(d), d[0] + d[1] + d[1] )  #같은 자료형끼리 연산이 가능
# print('d- ', type(d), d[2] + d[3])  #같은 자료형끼리 연산이 가능
# print('e- ', type(e), e[-1][1])
# print('e- ', type(e), e[2][1])


# # 슬라이싱
# print("#=======#")
# print('d- ', d[3])
# print('d- ', d[2 : ])


# 연산
# print(c + d)
# print(c * 3)
# print('hi' + str(c[0]))


# 리스트 수정, 삭제
print("#=======#")
c[0] = 4
print(c)
c[1 : 2] = ['a', 'b', 'c']  #범위에 리스트를 집어넣었을때는 리스트가 아니라 각각의 원소로 반영
print(c)
c[1] = ['a', 'b', 'c']  # 하나의 인덱스에 리스트를 넣어주면 그 때는 리스트 자체로 반영
print(c)

