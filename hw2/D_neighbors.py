lst = list(map(int, input().split()))
cnt = 0
if len(lst) > 2:
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            cnt += 1

print(cnt)
