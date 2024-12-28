# https://contest.yandex.ru/contest/27794/problems/E/

from collections import Counter


def find_coords(colors, k):
    left = 0
    segment_colors = Counter()
    best_segment = [0, len(colors)]

    for right, color in enumerate(colors):
        segment_colors[color] += 1
        if len(segment_colors) == k:
            while segment_colors[colors[left]] > 1:
                segment_colors[colors[left]] -= 1
                left += 1

            if right - left < best_segment[1] - best_segment[0]:
                best_segment = (left, right)

    return best_segment[0] + 1, best_segment[1] + 1


def main():
    n, k = map(int, input().split())
    trees = list(map(int, input().split()))
    print(*find_coords(trees, k))


assert find_coords([1, 2, 1, 3, 2], 3) == (2, 4)
assert find_coords([2, 4, 2, 3, 3, 1], 4) == (2, 6)
assert find_coords([1], 1) == (1, 1)
assert find_coords([1, 2, 1, 1, 1, 1, 1, 1, 3, 2], 3) == (8, 10)
assert find_coords([1, 2, 3, 4, 5], 5) == (1, 5)
assert find_coords([5, 1, 1, 2, 2, 4, 4, 4, 3, 2, 1, 5], 5) == (8, 12)

if __name__ == "__main__":
    main()


# incorrect solution
# def find_coords(arr, k):
#     d = {}
#     left = right = 0
#     d[arr[left]] = 1
#
#     while len(d) != k:
#         right += 1
#         if right < len(arr):
#             if arr[left] == arr[right]:
#                 if arr[left] in d.keys():
#                     d[arr[left]] -= 1
#                     if d[arr[left]] == 0:
#                         d.pop(arr[left])
#                 left += 1
#             d[arr[right]] = d.get(arr[right], 0) + 1
#
#     if right - left + 1 < k:
#         return 1, len(arr)
#
#     return left + 1, right + 1
