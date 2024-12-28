N = int(input())
comp = list(map(int, input().split()))
error_flag = False
vasiliy = -1
rating = 1
champ_index = comp.index(max(comp))

for i in range(len(comp) - 1):
    if comp[i] % 10 == 5 and comp[i + 1] < comp[i] and champ_index < i:
        if comp[i] > vasiliy:
            vasiliy = comp[i]

for i in range(len(comp)):
    if comp[i] > vasiliy:
        rating += 1

if vasiliy != -1:
    print(rating)
else:
    print(0)

# slow implementation
# N = int(input())
# comp = list(map(int, input().split()))
# error_flag = False
# possible = []
# rating = []
# champ_index = comp.index(max(comp))
#
# for i in range(len(comp) - 1):
#     if comp[i] % 10 == 5 and comp[i + 1] < comp[i] and champ_index < i:
#         possible.append(comp[i])
#
# comp.sort(reverse=True)
# for i in range(len(comp)):
#     if comp[i] in possible:
#         rating.append(i)
#
# if possible:
#     print(min(rating) + 1)
# else:
#     print(0)
