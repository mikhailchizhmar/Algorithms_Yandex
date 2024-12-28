def find_size(width, height, n):
    left, right = 0, max(width, height) * n
    while left < right:
        size = (left + right) // 2
        quantity = (size // width) * (size // height)
        if quantity < n:
            left = size + 1
        else:
            right = size
    return left


assert find_size(2, 3, 10) == 9
assert find_size(1, 1, 8) == 3
assert find_size(1, 1, 1) == 1
assert find_size(3, 4, 1) == 4


def main():
    width, height, n = map(int, input().split())
    print(find_size(width, height, n))


if __name__ == '__main__':
    main()
