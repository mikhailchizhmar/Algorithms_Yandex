def max_product(lst):
    max1 = max2 = max3 = float("-inf")
    min1 = min2 = float("inf")

    for n in lst:
        if n > max1:
            max3, max2, max1 = max2, max1, n
        elif n > max2:
            max3, max2 = max2, n
        elif n > max3:
            max3 = n

        if n < min1:
            min2, min1 = min1, n
        elif n < min2:
            min2 = n

    if max1 * max2 * max3 >= min1 * min2 * max1:
        return max3, max2, max1
    else:
        return min1, min2, max1


# assert max_product([4, 3, 5, 2, 5]) == (4, 5, 5)
# assert max_product([-4, 3, -5, 2, 5]) == (-5, -4, 5)
# assert max_product([4, 3, -5, 2, 5]) == (3, 4, 5)

arr = list(map(int, input().split()))
print(*max_product(arr))
