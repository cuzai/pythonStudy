import sys
import os
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
print(sys.argv) # 현재 파일이 실행되고 있는 경로

# print(os.getcwd())  # 현재 위치(경로) 얻기
# print(os.path.dirname(os.getcwd())) # 한단계 위로 올릴 때

label = QLabel("PyQT First Test!")
label.show()

print("Before Loop")
app.exec_()
print("After Loop")




