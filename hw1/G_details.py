N, K, M = map(int, input().split())
amount = 0
N_left = 0

while (N >= K or N_left > 0) and K >= M:
    N += N_left
    N_left = 0
    if N >= K:
        N -= K
        amount += K // M
        N_left += K % M

print(amount)
