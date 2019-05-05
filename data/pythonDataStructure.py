# a = 'hello'
#
# print(type(a))
# print(a[0])
# print(a[0 : 3])   # 앞에 인덱스 ~ 뒤에 인덱스-1 까지 호출
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


# 리스트 수정
# print("#=======#")
# c[0] = 4
# print(c)
# c[1 : 2] = ['a', 'b', 'c']  #범위에 리스트를 집어넣었을때는 리스트가 아니라 각각의 원소로 반영
# print(c)
# c[1] = ['a', 'b', 'c']  # 하나의 인덱스에 리스트를 넣어주면 그 때는 리스트 자체로 반영
# print(c)
# c[1 : 3] = []
# print(c)
#
#
# 리스트 삭제
# del c[3]
# print(c)


# 리스트 함수
# f = [5, 2, 3, 1, 4]
# print("#=======#")
# print(f)
#
# f.append(6)
# print(f)
#
# f.sort()    # 오름차순 정렬
# print(f)
#
# f.reverse()    # 내림차순 정렬
# print(f)
#
# print(f.count(3))  # 리스트는 중복을 허용하므로 해당 원소의 개수를 돌려줌
#
# f.remove(2) # del은 인덱싱을 통해 지우는거고 remove는 값 자체에 대한 지정으로 삭제
# print(f)
#
# print(f.pop())  # 마지막 원소를 빼내줌(삭제랑 다름)
# print(f)
#
# ex = [8, 9]
# f.extend(ex)
# print(f)


# 리스트 삭제 : del(인덱스 번호), remove(값 자체), pop(맨 마지막)



# 튜플(순서o, 중복o, 수정x, 삭제x) : 불변
# 속도 : 튜플 > 리스트
# a = (0, )   # 원소가 하나만 있을때는 뒤에 콤마 찍어줘야 함


# 딕셔너리(key, value → 순서x, 중복x, 수정o, 삭제o)
# 선언
# a = {'name' : 'park', 'phone' : '010-000-0000', 'birth' : '881214'}
# b = {0 : 'hello'}
# c = {'arr' : [0, 1, 2, 3]}
# print(type(a), a)
#
# print(a['name'])    # 없는 키값이면 예외가 발생
# print(a.get('name'))    # 없는 키값이면 none을 돌려줌
# print(c.get('arr'))
#
# # 딕셔너리 추가
# a['address'] = '서울'
# print(a)
#
# a['rank'] = [1, 2, 3]
# print(a)
#
# print(type(a.keys()))   # 명시적으로 list로 형변환 가능
#
# print(a.values())   # 명시적으로 list로 형변환 가능
#
# print(a.items())    # 튜플형으로 돌려줌
#
# print('name' in a)  # 키값이 있는지 iterate 가능
# print('city' in a)


# sets 집합 자료형(순서x, 중복x, 수정o, 삭제o)
# 선언
a = set([1, 2, 3, 4])
print(a)    # 인덱싱을 제공 x

t = tuple(a)
print(t[0:2])

l = list(a)
print(l[0:2])

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)  # 교집합을 찾아줌
print(s1.intersection(s2))

print(s1 | s2)  # 합집합을 돌려줌

print(s1.difference(s2))    # 차집합을 돌려줌

# 추가 제거
s3 = set([1, 2, 3])
s3.add(4)
print(s3)

s3.remove(2)
print(s3)