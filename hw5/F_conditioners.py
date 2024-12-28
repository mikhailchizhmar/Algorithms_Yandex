# https://contest.yandex.ru/contest/27794/problems/F/

def easy_solution(classes, price_list):
    d = {k: float("inf") for k in classes}

    for k in d.keys():
        for b, c in price_list:
            if b >= k and c <= d[k]:
                d[k] = c

    return sum(d[a] for a in classes)


def linear(required_powers, conditioners):
    max_power = max(max(required_powers), max(cond[0] for cond in conditioners))
    prices = [-1] + [float("inf")] * max_power
    for power, price in conditioners:
        while price < prices[power]:
            prices[power] = price
            power -= 1

    return sum(prices[required_power] for required_power in required_powers)


def main():
    n = int(input())
    min_p = tuple(map(int, input().split()))
    m = int(input())
    variants = [tuple(map(int, input().split())) for _ in range(m)]
    print(linear(min_p, variants))


assert linear([1, 2, 3], [(1, 10), (1, 5), (10, 7), (2, 3)]) == 13
assert linear([800], [(800, 1000)]) == 1000
assert linear([8000], [(8000, 1000)]) == 1000

if __name__ == "__main__":
    main()
