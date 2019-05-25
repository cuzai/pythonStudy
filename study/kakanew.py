import random

def Inarr() :
    myBin = []
    arr = []
    # inpur arr
    for i in range(n) :
        while True :
            num = random.randint(1, 50)
            binNum = bin(num)[2:]
            if len(binNum) <= n :   # is binary length > n
                break
        arr.append(num)
        myBin.append(binNum)
    return myBin

def draw(arr) :
    numLi = []  # list of binaries
    # print(len(numLi))
    for enum, ele in enumerate(arr) :
        # element to list
        numLi.append([])
        for num in ele :
            numLi[enum].append(num)

        # add zeros
        while True :
            if len(numLi[enum]) < n :
                numLi[enum].insert(0, "0")
            else :
                break
    # print(numLi)
    for binNum in numLi :
        for i in binNum :
            if i == "0" :
                print("ㅁ", end = "")
            else : print("#", end = "")
        print()

    print("-"*10)









n = int(input("input n : "))

arr1 = Inarr()
arr2 = Inarr()
print(arr1)

draw(arr1)
draw(arr2)


# print(arr1)
# print(arr2)

