# left binary search
def find_min_number_of_5(a, b, c):
    if a + b + c == 0:
        return 1
    left, right = 0, 2 * (a + b + c)
    while left < right:
        n_of_5 = (left + right) // 2
        numerator = a * 2 + b * 3 + c * 4 + n_of_5 * 5
        denominator = a + b + c + n_of_5
        if numerator < 3.5 * denominator:
            left = n_of_5 + 1
        else:
            right = n_of_5
    return left


# falls on 33rd test
def find_min_number_of_5_incorrect(a, b, c):
    if a + b + c == 0:
        return 1
    left, right = 0, 2 * (a + b + c)
    while left < right:
        n_of_5 = (left + right) // 2
        grade = (a * 2 + b * 3 + c * 4 + n_of_5 * 5) / (a + b + c + n_of_5)
        if round(grade) < 4:
            left = n_of_5 + 1
        else:
            right = n_of_5
    return left


assert find_min_number_of_5(2, 0, 0) == 2
assert find_min_number_of_5(0, 3, 0) == 1
assert find_min_number_of_5(2, 3, 0) == 3
assert find_min_number_of_5(0, 0, 1) == 0
assert find_min_number_of_5(0, 0, 0) == 1
assert find_min_number_of_5(1, 2, 10) == 0


def main():
        a = int(input())
        b = int(input())
        c = int(input())
        print(find_min_number_of_5(a, b, c))


if __name__ == '__main__':
    main()
