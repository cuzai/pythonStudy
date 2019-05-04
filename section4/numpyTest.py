import pandas as pd
import numpy as np

#랜덤으로 DataFrame 생성
df = pd.DataFrame(np.random.randint(0, 100, size = (100, 4)), columns = list('ABCD'))   #colums = ['one', 'two', 'three', 'four']도 가능
print(df)

df = pd.DataFrame(np.random.randn(100, 4), columns = ['one', 'two', 'three', 'four'])
print(df)

df.to_csv('result_s2.csv', index = False, header = False)