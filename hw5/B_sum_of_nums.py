def count_k_sum_segments(arr, k):
    prefix_sums = 0
    count = 0
    prefix_count = {0: 1}

    for num in arr:
        prefix_sums += num
        if prefix_sums - k in prefix_count:
            count += prefix_count[prefix_sums - k]

        prefix_count[prefix_sums] = prefix_count.get(prefix_sums, 0) + 1

    return count


def main():
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    print(count_k_sum_segments(lst, k))


assert count_k_sum_segments([17, 7, 10, 7, 10], 17) == 4
assert count_k_sum_segments([1, 2, 3, 4, 1], 10) == 2
assert count_k_sum_segments([1, 2, 3, 4], 10) == 1
assert count_k_sum_segments([12], 12) == 1
assert count_k_sum_segments([666], 12) == 0

if __name__ == "__main__":
    main()
