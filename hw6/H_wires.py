def max_n_of_segments(arr, length):
    n = 0
    for wire in arr:
        n += wire // length
    return n


# right binary search
def find_max_length(arr, k):
    # left, right = 0, max(arr)  # linear time
    left, right = 0, 10 ** 7
    while left < right:
        mid = (left + right + 1) // 2
        n_segments = max_n_of_segments(arr, mid)
        if n_segments >= k:
            left = mid
        else:
            right = mid - 1
    return left


assert find_max_length([802, 743, 457, 539], 11) == 200
assert find_max_length([3, 5], 10) == 0
assert find_max_length([500, 100], 3) == 166


def main():
    n, k = map(int, input().split())
    wires = [int(input()) for _ in range(n)]
    print(find_max_length(wires, k))


if __name__ == '__main__':
    main()
