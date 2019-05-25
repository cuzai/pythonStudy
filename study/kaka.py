import random

def Inarr() :
    arr = []
    # get binary list
    for i in range(n) :
        while True :
            num = random.randint(1, 50)
            binNum = bin(num)[2:]   # to binary
            if len(binNum) <= n :   # is binary length > n
                break

        arr.append(binNum)
    # print(arr)

    # to n size binary List
    for i, ele in enumerate(arr) :
        li = []
        # binary to list of numbers
        for e in ele :
            li.append(e)

        # add zeros
        while True :
            if len(li) < n :
                li.insert(0, "0")
            else : break
        arr[i] = li
    print(arr)
    return arr


def draw(arr) :
    for ele in arr :
        for e in ele :

            if e == "0" :
                print("| |", end = "")
            else : print("|#|", end = "")
        print()
    print("-"*10)


# compare
def comp(arr1, arr2) :
    li = []
    for i in range(n) :
        li.append([])
        for e in range(n) :
            # print(arr1[i][e])
            # print(arr2[i][e])
            if arr1[i][e] == "1" or arr2[i][e] == "1" :
                print("|#|", end = "")
            else : print("| |", end = "")

        print()


n = int(input("input n : "))

arr1 = Inarr()
arr2 = Inarr()

draw(arr1)
draw(arr2)

print("compounded map")
comp(arr1, arr2)


