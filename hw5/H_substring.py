# https://contest.yandex.ru/contest/27794/problems/H/

from collections import defaultdict, Counter


# incorrect
def max_substring(string, k):
    left = 0
    min_len_substr = len(set(string)) * k
    letters_cnt = Counter()
    best_segment = [0, 0]

    for right, letter in enumerate(string):
        if letters_cnt[letter] < k:
            letters_cnt[letter] += 1

            if right - left > best_segment[1] - best_segment[0]:
                best_segment = [left, right]


# correct, O(n)
def max_substring_with_limited_repeats(s, k):
    left = 0
    counter = {}
    max_len = 0
    start_index = 0

    for right, char in enumerate(s):
        counter[char] = counter.get(char, 0) + 1

        # Если текущий символ превышает допустимое количество повторений
        while counter[char] > k:
            counter[s[left]] -= 1
            if counter[s[left]] == 0:
                del counter[s[left]]
            left += 1

        # Проверяем длину текущего окна
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            start_index = left

    return max_len, start_index + 1


assert max_substring_with_limited_repeats('abb', 1) == (2, 1)
assert max_substring_with_limited_repeats('ababa', 2) == (4, 1)
assert max_substring_with_limited_repeats('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 10) == (10, 1)
assert max_substring_with_limited_repeats('abbbbbaaaawwwww', 3) == (6, 4)
assert max_substring_with_limited_repeats('a', 10) == (1, 1)


def main():
    n, k = map(int, input().split())
    s = input().strip()
    print(max_substring_with_limited_repeats(s, k))


if __name__ == "__main__":
    main()
