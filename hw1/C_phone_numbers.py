numbers = [''] * 4

for i in range(4):
    numbers[i] = input()
    numbers[i] = (numbers[i].replace('(', '').replace(')', '')
                  .replace('-', '').replace('+', ''))

    if len(numbers[i]) == 11 or len(numbers[i]) == 8:
        numbers[i] = numbers[i][1:]
    if len(numbers[i]) == 7:
        numbers[i] = '495' + numbers[i]

for i in range(1, 4):
    if numbers[i] == numbers[0]:
        print("YES")
    else:
        print("NO")
