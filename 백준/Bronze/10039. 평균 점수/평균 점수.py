total = 0

for i in range(5):
    tmp = int(input())

    if tmp < 40:
        tmp = 40

    total += tmp

print(total // 5)