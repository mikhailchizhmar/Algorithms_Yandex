set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
ans = []
for num in set1:
    if num in set2:
        ans.append(num)
print(*sorted(ans))
