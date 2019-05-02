import numpy as np

li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

array = np.array(li)     # array() : 리스트를 행렬화한다. Dynamic typing : 리스트 내의 원소는 하나의 형으로 통일해야 함
print(array, '\n')
print(array + 1)

print(array.shape)      # 행렬이 몇 콤마 몇인지 알려줌(앞이 더 큰 차원)
print(array.ndim)        # 행렬이 몇차원인지
print(array.size)       # 행렬 내 원소들의 개수

# array 만드는 법 : np.array(리스트, dtype = int, str 등등)

np.empty([2, 2])    # 빈 array를 만든다.
np.zeros([2, 2])
np.ones([2, 2])

np.empty_like(li)   # 행렬의 틀만 따온 빈 행렬을 만들어준다.

np.identity(3, dtype = int)      # 해당 사이즈의 단위행렬을 만들어준다.

np.full((3, 3), 5)  # 5로 가득찬 3x3 행렬 만든다.

np.arange(1, 100, 2)    # 2의 등차를 갖고 1~100까지의 수를 만든다.

np.linspace(1, 100, num = 10)       # 1~100까지 중 10개를 뽑되, 얘들 서로서로의 차가 같다.

# axis = 0 은 열, 1은 행
np.average(li, axis = 1)        # average는 가중평균

# 슬라이싱
print(array[0:2, 0:3])  # 두개 행, 3개 열을 가져와라

# 인덱싱
print(array[1, 1])  # 2번째 행, 두번째 열의 값을 가져와라