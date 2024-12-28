n = int(input())
set_x = set()
set_y = set()
for i in range(n):
    x, y = map(int, input().split())
    set_x.add(x)
    set_y.add(y)
print(len(set_x))
