n = int(input())
turtles = set()
for i in range(n):
    turtles.add(tuple(map(int, input().split())))

set_before = set()
set_after = set()
for el in turtles:
    if el[0] + el[1] == n - 1 and el[0] >= 0 and el[1] >= 0:
        set_before.add(el[0])
        set_after.add(el[1])
print(min(len(set_before), len(set_after)))
