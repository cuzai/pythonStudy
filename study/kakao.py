import random

def Inarr() :
    arr = []
    while True :
        num = random.randint(1, 50)
        num = bin(num)[2:]

        while len(num) < n :
            num = "0" + num # add zeros

        if len(num) == n :
            arr.append(num)

        if len(arr) == n :
            return arr

n = int(input("input n : "))
arr1 = Inarr()
arr2 = Inarr()
newArr = []

for i in range(n) :
    myStr = ""
    for z in range(n) :
        if arr1[i][z] == "1" or arr2[i][z] == "1" :
            myStr = myStr + "|#|"
        else :
            myStr = myStr + "| |"
    newArr.append(myStr)
print(newArr)