def prefix_sums(arr):
    ascent_sums = [0] * len(arr)
    descent_sums = [0] * len(arr)
    for i in range(1, len(arr)):
        diff = arr[i][1] - arr[i - 1][1]
        if diff >= 0:
            ascent_sums[i] = ascent_sums[i - 1] + diff
            descent_sums[i] = descent_sums[i - 1]
        else:
            descent_sums[i] = descent_sums[i - 1] - diff
            ascent_sums[i] = ascent_sums[i - 1]

    return ascent_sums, descent_sums


def rsq(ascent_sums, descent_sums, left, right):
    if left < right:
        return ascent_sums[right - 1] - ascent_sums[left - 1]
    elif left > right:
        return descent_sums[left - 1] - descent_sums[right - 1]
    else:
        return 0


def main():
    n = int(input())
    coords = []
    for _ in range(n):
        x, y = map(int, input().split())
        coords.append((x, y))

    m = int(input())
    routes = []
    for _ in range(m):
        s, f = map(int, input().split())
        routes.append((s, f))

    asc, desc = prefix_sums(coords)
    for r in routes:
        print(rsq(asc, desc, r[0], r[1]))


# def tests():
#     a1, d1 = prefix_sums([(2, 1), (4, 5), (7, 4), (8, 2), (9, 6), (11, 3), (15, 3)])
#     assert rsq(a1, d1, 2, 6) == 4
#
#     a2, d2 = prefix_sums([(1, 1), (3, 2), (5, 6), (7, 2), (10, 4), (11, 1)])
#     assert rsq(a2, d2, 5, 6) == 0
#     assert rsq(a2, d2, 1, 4) == 5
#     assert rsq(a2, d2, 4, 2) == 4


if __name__ == "__main__":
    main()
