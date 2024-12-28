def map_bomb(i, j):
    field[i][j] = "*"
    coords = []
    if i == 0:
        if n > 1:
            coords.append([i + 1, j])
        if j != 0:
            coords.append([i, j - 1])
            if n > 1:
                coords.append([i + 1, j - 1])
        if j != m - 1:
            coords.append([i, j + 1])
            if n > 1:
                coords.append([i + 1, j + 1])
    elif i == n - 1:
        coords.append([i - 1, j])
        if j != 0:
            coords.append([i - 1, j - 1])
            coords.append([i, j - 1])
        if j != m - 1:
            coords.append([i - 1, j + 1])
            coords.append([i, j + 1])
    elif j == 0:
        if m > 1:
            coords.append([i, j + 1])
        if i != 0:
            coords.append([i - 1, j])
            if m > 1:
                coords.append([i - 1, j + 1])
        if i != n - 1:
            coords.append([i + 1, j])
            if m > 1:
                coords.append([i + 1, j + 1])
    elif j == m - 1:
        coords.append([i, j - 1])
        if i != 0:
            coords.append([i - 1, j])
            coords.append([i - 1, j - 1])
        if i != n - 1:
            coords.append([i + 1, j])
            coords.append([i + 1, j - 1])
    else:
        coords.append([i - 1, j - 1])
        coords.append([i - 1, j])
        coords.append([i - 1, j + 1])
        coords.append([i, j - 1])
        coords.append([i, j + 1])
        coords.append([i + 1, j - 1])
        coords.append([i + 1, j])
        coords.append([i + 1, j + 1])

    for cell in coords:
        if field[cell[0]][cell[1]] != "*":
            field[cell[0]][cell[1]] = str(int(field[cell[0]][cell[1]]) + 1)


n, m, k = map(int, input().split())
bombs = []
field = []
for i in range(n):
    field.append([0] * m)
for i in range(k):
    bombs.append(list(map(int, input().split())))
    bombs[i][0] -= 1
    bombs[i][1] -= 1

for c in bombs:
    map_bomb(c[0], c[1])

for s in field:
    print(*s)
