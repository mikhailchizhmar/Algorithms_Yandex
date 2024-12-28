def find_pairs(arr, r):
    cnt_pairs = 0
    right = 0
    for left in range(len(arr)):
        while right < len(arr) and arr[right] - arr[left] <= r:
            right += 1
        cnt_pairs += len(arr) - right

    return cnt_pairs


def main():
    n, r = map(int, input().split())
    lst = list(map(int, input().split()))

    print(find_pairs(lst, r))


if __name__ == "__main__":
    main()
