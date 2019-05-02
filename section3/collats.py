def collatz(number) :
    if(number % 2 == 0) :
        return int(number / 2)
    else :
        return int(number * 3 + 1)

while True :
    number = input("Input number")
    try :
        number = int(number)
    except ValueError :
        if number == 'exit' :
            exit()
        print("'{}'{}".format(number, "is not a number"))
        continue
    break

while True :
    number = collatz(number)
    print(number)
    if number ==1 :
        break

print("finished")