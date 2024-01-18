n = int(input())
i = 1
while n != 1:
    if n % 2:
        n = 3*n + 1
    else:
        n = n//2
    i += 1
print(i)