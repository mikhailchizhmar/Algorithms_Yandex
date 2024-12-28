k1, m, k2, p2, n2 = map(int, input().split())
n_rooms = (k2 - 1) // (n2 + m * (p2 - 1)) + 1  # number of rooms on a floor

floor = (k1 - 1) // n_rooms + 1
p1 = (floor - 1) // m + 1
n1 = floor - (p1 - 1) * m

if p2 > n2 or n2 > m:
    print(-1, -1)
elif m == 1:
    print(0, n1)
else:
    print(p1, n1)
