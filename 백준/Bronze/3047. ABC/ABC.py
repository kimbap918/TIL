numbers = list(map(int, input().split()))
order = input()
numbers = sorted(numbers)

for i in order:
    if i == 'A':
        print(numbers[0], end =' ')
    elif i == 'B':
        print(numbers[1], end =' ')
    elif i == 'C':
        print(numbers[2], end =' ')