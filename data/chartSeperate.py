import matplotlib.pyplot as plt

# figure 객체 생성
fig = plt.figure('Chart Name')  # 차트 이름 넣을 수 있음

# 차트 사이즈 지정
fig.set_size_inches(10, 6, forward = True)

# 서브 플롯 생성(2행 1열)
ax1 = fig.add_subplot(2, 1, 1)      # 2행 1열짜리로 분할하고, 그 중에 1번째다.
ax2 = fig.add_subplot(2, 1, 2)      # 2행 1열짜리로 분할하고, 그 중에 2번째다.

# x축 생성
x = range(1, 100)

# y축 생성
y = [i*i for i in x]

# y축 생성2
z = [i*i*2 for i in x]

# 라인 차트 1행 1열
ax1.plot(x, y, 'b', label = 'y = x^2')
ax1.plot(x, z, 'r', label = 'y = x^2*2')

# 범례 위치
plt.legend(loc = 'upper left')


# 차트 제목
plt.title('Formulas')

# 축 라벨
plt.xlabel('x value')
plt.ylabel('y value')

# 바 차트 1행 1열
ax2.bar(x, z)

plt.show()