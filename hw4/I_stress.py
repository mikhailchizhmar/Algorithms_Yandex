def stress_test(sentence, words):
    def has_no_stress(word):
        return word == word_lower

    def has_more_than_one_stress(word):
        upper_count = 0
        for c in word:
            if c.isupper():
                upper_count += 1
                if upper_count > 1:
                    return True
        return False

    dictionary = {}
    for word in words:
        word_lower = word.lower()
        if word_lower not in dictionary:
            dictionary[word_lower] = set()
        dictionary[word_lower].add(word)

    errors = 0
    for word in sentence.split():
        word_lower = word.lower()
        incorrect_stressing = word_lower in dictionary and word not in dictionary[word_lower]
        if incorrect_stressing or has_no_stress(word) or has_more_than_one_stress(word):
            errors += 1

    return errors


def main():
    n = int(input())
    words = [input() for _ in range(n)]
    sentence = input()
    print(stress_test(sentence, words))


if __name__ == '__main__':
    main()

# incorrect solution
# n = int(input())
# d = {}
# for i in range(n):
#     d[input()] = 0
# sentence = input().split()
#
# n_errors = 0
# for word in sentence:
#     if word not in d:
#         cnt = 0
#         for letter in word:
#             if 65 <= ord(letter) <= 90:
#                 cnt += 1
#         if cnt != 1:
#             n_errors += 1
#
# print(n_errors)
