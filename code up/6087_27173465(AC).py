a = int(input())
b = 0
while a > b:
    b += 1
    if b % 3 == 0:
        continue
    print(b, end=' ')

