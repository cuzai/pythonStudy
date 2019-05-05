import matplotlib.pyplot as plt #차트 만드는 라이브러리

# 리스트 범위(x축)
x = list(range(0, 256))
# print(x)

# 리스트 범위(y축)
y = [i*i for i in x]
# for i in x :
#     y.append(i*i)
print(y)

# 차트 설정
plt.plot(x, y, 'r--') # r, b 등으로 색깔 지정 가능, 선의 종류도 선택 가능 b--, bo(선 굵게) 등

# 차트 실행
plt.show()