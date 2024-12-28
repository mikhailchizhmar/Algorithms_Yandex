N = int(input())
lst = list(map(int, input().split()))
x = int(input())
min_diff = float("inf")
ans = lst[0]

for num in lst:
    diff = abs(num - x)
    if diff < min_diff:
        min_diff = diff
        ans = num

print(ans)
