lst = list(map(int, input().split()))

max1 = max2 = float("-inf")
min1 = min2 = float("inf")

for n in lst:
    if n > max1:
        max2, max1 = max1, n
    elif n > max2:
        max2 = n

    if n < min1:
        min2, min1 = min1, n
    elif n < min2:
        min2 = n

if max1 * max2 >= min1 * min2:
    print(max2, max1)
else:
    print(min1, min2)

# Решение валится на 22 тесте: lst = [-100, 100]
# lst = list(map(int, input().split()))
#
# max1 = lst[0]
# min1 = lst[0]
# i_max1 = 0
# i_min1 = 0
# max2 = lst[0]
# min2 = lst[0]
#
# for i in range(len(lst)):
#     if lst[i] > max1:
#         max1 = lst[i]
#         i_max1 = i
#     elif lst[i] < min1:
#         min1 = lst[i]
#         i_min1 = i
#
# for i in range(len(lst)):
#     if i != i_min1 and i != i_max1:
#         if lst[i] > max2:
#             max2 = lst[i]
#         elif lst[i] < min2:
#             min2 = lst[i]
#
# if max1 * max2 >= min1 * min2:
#     print(max2, max1)
# else:
#     print(min1, min2)
