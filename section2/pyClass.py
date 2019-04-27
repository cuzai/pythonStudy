class UserInfo :
    def __init__(self, name, phone) :   #생성자 __init__
        self.name = name
        self.phone = phone

    def printInfo(self) :
        print("------------")
        print(self.name)
        print(self.phone)
        print("------------")

    def __del__(self) :
        print(self.name, "deleted")

user1 = UserInfo("park", "010-3005-9929")
user2 = UserInfo("lee", "010-9936-7926")

user1.printInfo()
user2.printInfo()

print(user1.__dict__)   #인스턴스의 네임스페이스 확인
print(user2.__dict__)
print(UserInfo.__dict__)