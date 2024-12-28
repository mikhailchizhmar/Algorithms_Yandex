lst = list(map(int, input().split()))
answer = "YES"
# если массив не пустой
if lst:
    prev = lst[0]
else:
    answer = "NO"

for i in range(1, len(lst)):
    if prev >= lst[i]:
        answer = "NO"
    prev = lst[i]
print(answer)
