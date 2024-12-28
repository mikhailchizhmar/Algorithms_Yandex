str1 = input()
str2 = input()

set_b = set()
for i in range(len(str2) - 1):
    set_b.add(str2[i:i + 2])

res = 0
for i in range(len(str1) - 1):
    if str1[i:i + 2] in set_b:
        res += 1
print(res)

# str1 = input()
# str2 = input()
# gen = {}
# cnt = 0
#
# for i in range(len(str1) - 1):
#     if str1[i:i + 2] in gen.keys():
#         gen[str1[i:i + 2]] += 1
#     else:
#         gen[str1[i:i + 2]] = 1
#
# for i in range(len(str2) - 1):
#     if str2[i:i + 2] in gen.keys():
#         cnt += gen[str2[i:i + 2]]
# print(cnt)
