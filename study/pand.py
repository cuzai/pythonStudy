import pandas

raw_data = {'first_name' : ['park', 'kim'], 'last_name' : ['sung', 'ho']}
df = pandas.DataFrame(raw_data, index = ['a', 'b'])
# print(df.T)    # 행 열 바꾸기

# print(df.first_name[df.first_name=='park'])



#loc : 인덱스 값 그 자체, iloc : 실제 순서, 무조건 숫자 값
print(df.loc['a'])

# print(df)