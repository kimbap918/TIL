numbers = []
max = 0

for _ in range(int(input())):
    numbers.append(int(input()))

for i in numbers:
    if numbers.count(i) > max:
        max = numbers.count(i)

print(max)