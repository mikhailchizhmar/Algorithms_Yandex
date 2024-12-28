a = int(input())
b = int(input())
c = int(input())
ansNO = "NO SOLUTION"
ansMANY = "MANY SOLUTIONS"

if c < 0:
    print(ansNO)
elif a == 0:
    if c * c - b == 0:
        print(ansMANY)
    else:
        print(ansNO)
else:
    if (c * c - b) % a == 0:
        print((c * c - b) // a)
    else:
        print(ansNO)
