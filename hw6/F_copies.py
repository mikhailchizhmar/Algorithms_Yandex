# left binary search
def find_min_number_of_5(N, x, y):
    left, right = 1, N * max(x, y)
    while left < right:
        time = (left + right) // 2
        N_curr = (time - min(x, y)) // x + (time - min(x, y)) // y + 1
        if N_curr < N:
            left = time + 1
        else:
            right = time
    return left


# N = 5
# x = 2
# y = 3

#                |           | - (time - min(x, y))

# x:         |- -|- -|- -|- -|
# y:             |- - -|- - -|
# seconds:    1 2 3 4 5 6 7 8 9 10 11 ...


assert find_min_number_of_5(4, 1, 1) == 3
assert find_min_number_of_5(5, 1, 2) == 4
assert find_min_number_of_5(1, 1, 1) == 1
assert find_min_number_of_5(3, 1, 10) == 3
assert find_min_number_of_5(5, 2, 3) == 8


def main():
    N, x, y = map(int, input().split())
    print(find_min_number_of_5(N, x, y))


if __name__ == '__main__':
    main()
