ex = input("input")
ex = list(ex)

tryLi=[]
idx = -1

for i in ex :
    try :
        int(i)  # detect number

        try :   # detect 10
            if len(tryLi[idx]) == 1 :
                tryLi[idx].append(i)
                continue
        except : pass

        tryLi.append([])
        idx += 1
        tryLi[idx].append(i)

    except ValueError :
        tryLi[idx].append(i)

# print(tryLi)

for n, myTry in enumerate(tryLi) :
    num = ''

    try :   # detect 10
        int(myTry[1])
        num = myTry.pop(0) + myTry.pop(0)
    except ValueError :
        num = myTry.pop(0)

    num = int(num)
    tryLi[n] = num

    if  myTry[0] == 'D' :
        tryLi[n] = tryLi[n] ** 2
    elif myTry[0] == 'T' :
        tryLi[n] = tryLi[n] ** 3

    try :
        if myTry[1] == '*' :
            tryLi[n] = tryLi[n] * 2
            if n != 0 :
                tryLi[n-1] = tryLi[n-1]*2
        elif myTry[1] == '#' :
            tryLi[n] = -tryLi[n]

    except IndexError :
        pass

print(tryLi)

result = 0
for i in tryLi :
    result = result + i
print(result)
