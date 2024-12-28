n, m = map(int, input().split())
set_n = set()
set_m = set()
for i in range(n):
    set_n.add(int(input()))
for i in range(m):
    set_m.add(int(input()))

same_count = 0
same_set = set()
for cube in set_n:
    if cube in set_m:
        same_count += 1
        same_set.add(cube)

for cube in same_set:
    set_n.remove(cube)
    set_m.remove(cube)

print(same_count)
print(*sorted(same_set))
print(len(set_n))
print(*sorted(set_n))
print(len(set_m))
print(*sorted(set_m))
