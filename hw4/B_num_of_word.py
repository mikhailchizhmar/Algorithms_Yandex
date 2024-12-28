with open("input.txt", "r") as inp:
    text = inp.read().split()
d = {}
for word in text:
    if word not in d.keys():
        d[word] = 0
    else:
        d[word] += 1

    print(d[word], end=" ")
