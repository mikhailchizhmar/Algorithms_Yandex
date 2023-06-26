numbers = ['', '', '', '']
numbers[0] = input()
numbers[1] = input()
numbers[2] = input()
numbers[3] = input()

for i in range(4):
    numbers[i] = numbers[i].replace('(', '')
    numbers[i] = numbers[i].replace(')', '')
    numbers[i] = numbers[i].replace('-', '')
    numbers[i] = numbers[i].replace('+', '')

    if len(numbers[i]) == 11 or len(numbers[i]) == 8:
        numbers[i] = numbers[i][1:]
    if len(numbers[i]) == 7:
        numbers[i] = '495' + numbers[i]

for i in range(1, 4):
    if numbers[0] == numbers[i]:
        print("YES")
    else:
        print("NO")
