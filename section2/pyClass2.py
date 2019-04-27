class SelfTest :
    def function1() :
        print("function1 called!")

    def function2(self) :
        print("function2 called!")

    i = 1

f = SelfTest()

#f.function1() #self를 통해서 인스턴스의 주소값을 넘겨주는데, function1을 주소값을 받을 매개변수(self)를 정의해주지 않아서 호출이 안됨
SelfTest.function1() #인스턴스 생성 없이 직접 접근 하면 호출 가능
f.function2()

SelfTest.i = 2  #클래스 자체의 변수를 바꿔버림

print(SelfTest.i)
print(f.i)  #원본이 바뀌니 인스턴스의 값도 바뀜