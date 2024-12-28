# right binary search
def find_max_width(n, m, t):
    left, right = 0, (min(n, m) - 1) // 2
    while left < right:
        mid = (left + right + 1) // 2
        n_tiles = n * m - (n - 2 * mid) * (m - 2 * mid)
        # this also works:
        # n_tiles = mid * (2 * n + 2 * m - 4 * mid)
        if n_tiles <= t:
            left = mid
        else:
            right = mid - 1
    return left


assert find_max_width(6, 7, 38) == 2
assert find_max_width(5, 5, 50) == 2
assert find_max_width(5, 5, 24) == 2
assert find_max_width(5, 5, 23) == 1
assert find_max_width(4, 10, 40) == 1
assert find_max_width(4, 10, 22) == 0


def main():
    n = int(input())
    m = int(input())
    t = int(input())
    print(find_max_width(n, m, t))


if __name__ == '__main__':
    main()
