n = int(input())
max_touches = list(map(int, input().split()))
d = {i + 1: max_touches[i] for i in range(n)}

k = int(input())
touches = list(map(int, input().split()))
for button in touches:
    d[button] -= 1

for key in d.keys():
    if d[key] < 0:
        print("YES")
    else:
        print("NO")
