with open("input.txt", "r") as inp:
    text = inp.read().split()

d = {}
for word in text:
    if word not in d.keys():
        d[word] = 0
    d[word] += 1

most_common_word = None
max_count = 0

for word, count in d.items():
    if count > max_count or (count == max_count and (most_common_word is None or word < most_common_word)):
        most_common_word = word
        max_count = count

print(most_common_word)


# solution with using min()
#
# from collections import Counter
#
# with open("input.txt", "r") as inp:
#     text = inp.read().split()
#
# word_count = Counter(text)
#
# # Нахождение слова с максимальной частотой
# # Если несколько слов имеют одинаковую частоту, выбирается лексикографически минимальное
# most_common_word = min(word_count, key=lambda x: (-word_count[x], x))
# print(most_common_word)
