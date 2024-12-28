# https://contest.yandex.ru/contest/27794/problems/I/

def robot(s, k):
    prev_len = 0
    ans = 0
    for i in range(k, len(s)):
        if s[i] == s[i - k]:
            prev_len += 1
            ans += prev_len
        else:
            prev_len = 0

    return ans


assert robot('zabacabab', 2) == 5
assert robot('abcabcac', 3) == 10
assert robot('abcabcabcbb', 3) == 22
assert robot('abc', 2) == 0


def main():
    k = int(input())
    s = input()
    print(robot(s, k))


if __name__ == "__main__":
    main()
