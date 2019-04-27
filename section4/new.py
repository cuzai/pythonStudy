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