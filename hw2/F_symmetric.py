def search_mid(list_a: list[int]) -> tuple[int, list[int]]:
    mid = len(list_a) - 1
    for i in range(len(list_a)):
        if list_a[i] == list_a[mid] and i != mid and is_symmetric(list_a[i + 1:mid]):
            break

    return i, list_a[i - 1::-1]


def is_symmetric(list_a: list[int]) -> bool:
    is_sym = True
    for i in range((len(list_a) + 1) // 2):
        right = len(list_a) - i - 1
        if list_a[i] != list_a[right]:
            is_sym = False
    return is_sym


N = int(input())
lst = list(map(int, input().split()))
count = 0
if is_symmetric(lst):
    print(0)
else:
    answer = search_mid(lst)
    print(answer[0])
    print(*answer[1])
