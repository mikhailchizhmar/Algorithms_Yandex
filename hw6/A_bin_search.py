def binary_search(arr, k):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        if k > arr[m]:
            l = m + 1
        elif k < arr[m]:
            r = m - 1
        else:
            return True
    return False


def left_binary_search(arr, k):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        if k > arr[m]:
            l = m + 1
        elif k < arr[m]:
            r = m
        else:
            return True
    return False


def main():
    n, k = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    for el in arr2:
        if binary_search(arr1, el):
            print("YES")
        else:
            print("NO")


assert binary_search([1, 2, 3, 4, 5], 1) is True
assert binary_search([1, 2, 3, 4, 5], 2) is True
assert binary_search([1, 2, 3, 4, 5], 3) is True
assert binary_search([1, 2, 3, 4, 5], 4) is True
assert binary_search([1, 2, 3, 4, 5], 5) is True
assert binary_search([1, 2], 1) is True
assert binary_search([1, 2], 2) is True
assert binary_search([1, 2], 8) is False


if __name__ == "__main__":
    main()
