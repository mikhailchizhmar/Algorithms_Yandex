buttons = set(input().split())
inp_set = set(input())
cnt = 0
for c in inp_set:
    if c not in buttons:
        cnt += 1

print(cnt)
