import random
import time

a = 1

b = 1

c = 1


def printTrack(a, b, c, end):
    for i in range(1, end+1):
        line = ""
        if len(str(i)) == 1:
            line += "0" + str(i) + " "
        else:
            line += str(i) + " "
        print(line, end="")
    print("\n")
    printturtoise("A ", a, end)
    print("\n")
    printturtoise("B ", b, end)
    print("\n")
    printturtoise("C ", c, end)


def printturtoise(name, no, end):
    for i in range(1, end+1):
        if no == i:
            print(name, end=" ")
        else:
            print("-- ", end="")

    print()


def moveTortoise(t):
    x = random.randrange(1, 11)

    if (x == 1) and (t > 2):
        return t-2
    elif (x <= 3) and (x > 1) and (t > 1):
        return t-1
    elif (x <= 5) and (x > 3):
        return t
    elif (x <= 9) and (x > 5):
        if (t+1 >= end):
            return end
        return t+1
    elif (x == 10):
        if(t+2 >= end):
            return end
        return t+2
    else:
        return t


end = int(input("Please enter the length of the race track = "))
r = 0
h = True
while h == True:
    if r == 0:
        printTrack(1, 1, 1, end)
    time.sleep(2)
    a = moveTortoise(a)
    b = moveTortoise(b)
    c = moveTortoise(c)

    printTrack(a, b, c, end)

    r = r+1
    if a >= end:
        h = False
        break
    elif b >= end:
        h = False
        break
    elif c >= end:
        h = False
        break


if (a == end and b == end) or (a == end and c == end) or (b == end and c == end):
    print("It's a tie!!")
else:
    if a > b and a > c:
        print("A WON!")

    elif b > a and b > c:
        print("B WON!")
    elif c > a and c > b:
        print("C WON!")
