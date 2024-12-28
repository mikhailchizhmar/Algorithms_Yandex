a = int(input())
b = int(input())
n = int(input())
m = int(input())

min_a = n + (n - 1) * a
min_b = m + (m - 1) * b
max_a = n + (n + 1) * a
max_b = m + (m + 1) * b

if max(min_a, min_b) > min(max_a, max_b):
    print(-1)
else:
    t_min = max(min_a, min_b)
    t_max = min(max_a, max_b)
    print(t_min, t_max)