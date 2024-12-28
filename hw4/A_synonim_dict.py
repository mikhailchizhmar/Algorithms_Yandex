n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = value
word = input()

for k, v in d.items():
    if k == word:
        print(v)
        break
    elif v == word:
        print(k)
        break
