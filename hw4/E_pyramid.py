n = int(input())
d = {}
for i in range(n):
    w, h = map(int, input().split())
    if w not in d.keys() or w in d.keys() and h > d[w]:
        d[w] = h

print(sum(d.values()))
