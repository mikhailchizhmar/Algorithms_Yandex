def closest_clothes(arr_n, arr_m):
    n_index = m_index = 0
    best_n_index = best_m_index = 0

    while n_index < len(arr_n) and m_index < len(arr_m):
        if abs(arr_n[n_index] - arr_m[m_index]) < abs(arr_n[best_n_index] - arr_m[best_m_index]):
            best_n_index, best_m_index = n_index, m_index

        if n_index < len(arr_n) and m_index < len(arr_m) - 1 and arr_m[m_index] < arr_n[n_index]:
            m_index += 1
        else:
            n_index += 1

    return arr_n[best_n_index], arr_m[best_m_index]


assert closest_clothes([3, 4], [1, 2, 3]) == (3, 3)
assert closest_clothes([4, 5], [1, 2, 3]) == (4, 3)
assert closest_clothes([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == (1, 1)


def main():
    n = int(input())
    lst_n = list(map(int, input().split()))
    m = int(input())
    lst_m = list(map(int, input().split()))

    print(*closest_clothes(lst_n, lst_m))


if __name__ == "__main__":
    main()
