#kim 이라는 함수를 정의
def kim() :
    arms = 2
    legs = 2
    head = 1
    print("kim's " + "arms are" + str(arms) + ", legs are" + str(legs) + " and head is" + str(head))
kim()
#park의 상태도 나오게 해 보기

#여러명의 상태 나오게 하기
def person(name) :
    arms = 2
    legs = 2
    head = 1
    print(name + "'s " + "arms are" + str(arms) + ", legs are" + str(legs) + " and head is" + str(head))

#장애가 있는 사람 함수 만들기
def personWithOneArms(name) :
    sdf = 1
    legs = 2
    head = 1
    print(name + "'s " + "arms are" + str(sdf) + ", legs are" + str(legs) + " and head is" + str(head))

person("kim")
person("park")
personWithOneArms("lee")

class human :
    name = ""
    arms = 2
    legs = 2
    head = 2
    def call(self, name) :
        self.name = name
        print (name + "'s " + "arms are" + str(self.arms) + ", legs are" + str(self.legs) + " and head is" + str(self.head))

kim  = human()
kim.call("kim")

park = human()
park.call("park")

#무의미한 코드 줄이기(생성자)
class human :
    def __init__(self, erum):
        self.name = erum
        self.arms = 2
        self.legs = 2
        self.head = 1
        print (erum+ "'s " + "arms are" + str(self.arms) + ", legs are" + str(self.legs) + " and head is" + str(self.head))
human("kim")

class humanDisabled(human) :
    arms = 1
    def call(self) :
        print (self.name + "'s " + "arms are" + str(self.arms) + ", legs are" + str(self.legs) + " and head is" + str(self.head))
# 팔의 상태는 안나오게도 해 보기

choi = humanDisabled("choi")