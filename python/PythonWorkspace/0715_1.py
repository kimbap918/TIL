import random

n = int(input('얼마쓸래?'))
for i in range(n):
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    print(numbers)