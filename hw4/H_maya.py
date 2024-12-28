from collections import Counter

# Чтение данных
g, len_s = map(int, input().split())
w = input().strip()
s = input().strip()

# Эталонный словарь частот для строки W
w_count = Counter(w)
current_count = Counter(s[:g])

matches = 0

# Проверка первого окна
if current_count == w_count:
    matches += 1

# Сдвиг окна по строке S
for i in range(g, len_s):
    # Удаляем старый символ из окна
    old_char = s[i - g]
    current_count[old_char] -= 1
    if current_count[old_char] == 0:
        del current_count[old_char]

    # Добавляем новый символ в окно
    new_char = s[i]
    current_count[new_char] += 1

    # Сравниваем словарь окна с эталоном
    if current_count == w_count:
        matches += 1

print(matches)


# slow implementation:
# g, len_s = map(int, input().split())
# w = ''.join(sorted(input()))
# s = input()
#
# d = {w: 0}
# for i in range(len_s - g + 1):
#     sub_s = ''.join(sorted(s[i:i + g]))
#     if sub_s in d:
#         d[w] += 1
#
# print(d[w])
