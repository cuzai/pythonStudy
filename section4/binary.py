# · 텍스트 데이터
#   - 장점 : 에디터 편집 가능, 가독성 좋음
#   - 단점 : 크기가 큼
#
# · 바이너리 데이터
#   - 장점 : 크기가 작음. 동영상, 이미지 등
#   - 단점 : 에디터 편집 불가.

import pickle   # 객체, 텍스트의 직렬화, 역직렬화

# 파일 이름과 데이터
bfilename = 'C:/Users/cuzai/Desktop/Web_Crawling/pythonStudy/section4/test.bin'
tfilename = 'C:/Users/cuzai/Desktop/Web_Crawling/pythonStudy/section4/test.txt'

data1 = 77
data2 ="Hello World"
data3 = ['car', 'apple', 'house']

# 바이너리 쓰기
with open(bfilename, 'wb') as f :
    pickle.dump(data1, f)   #dumps는 객체를 바이너리화 할 때, dump는 그냥 텍스트를 바이너리화(직렬화) 할 때
    pickle.dump(data2, f)
    pickle.dump(data3, f)

# 텍스트 쓰기

with open(tfilename, 'wt') as f :
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3))  # 리스트 그 자체를 바로 write 할 수는 없음. 그래서 파이썬 writelines 메소드를 통해
                                    # 리스트를 순회하며 쓸 수 있도록 해 주고, 파이썬 자체 함수인 join을 통해 ??해 준다.
                                    #좀 더 찾아볼 것

# 바이너리 읽기
with open(bfilename, 'rb') as f :
    b = pickle.load(f)
    print(type(b), 'binary read1 : ', b)
    b = pickle.load(f)
    print(type(b), 'binary read2 : ', b)
    b = pickle.load(f)
    print(type(b), 'binary read3 : ', b)



# 텍스트 읽기
with open(tfilename, 'rt') as f :
    for i, line in enumerate(f, 1) :
        print(type(line), 'text read', str(i) + " " +line, end = "")
