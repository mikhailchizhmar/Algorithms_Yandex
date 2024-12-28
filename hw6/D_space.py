# right binary search
def find_module_size(n, a, b, w, h):
    left, right = 0, max(w, h)
    while left < right:
        d = (left + right + 1) // 2
        max_n = max((w // (a + 2 * d)) * (h // (b + 2 * d)), (h // (a + 2 * d)) * (w // (b + 2 * d)))
        if max_n >= n:
            left = d
        else:
            right = d - 1
    return left


assert find_module_size(1, 1, 1, 1, 1) == 0
assert find_module_size(1, 1, 1, 3, 3) == 1
assert find_module_size(11, 3, 2, 21, 25) == 2
assert find_module_size(3, 1, 5, 4, 3) == 0
assert find_module_size(1, 2, 2, 10, 10) == 4
assert find_module_size(4, 2, 2, 30, 30) == 6
assert find_module_size(6, 2, 5, 20, 15) == 1
assert find_module_size(4, 3, 3, 20, 10) == 1
assert find_module_size(1, 10, 20, 10, 20) == 0


def main():
    n, a, b, w, h = map(int, input().split())
    print(find_module_size(n, a, b, w, h))


if __name__ == '__main__':
    main()
