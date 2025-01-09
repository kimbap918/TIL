import sys

n = int(sys.stdin.readline())

target_number = -1

for _ in range(n):
    number = int(sys.stdin.readline())

    if target_number < 0:
        target_number = number
        continue
    
    if number % target_number == 0:
        print(number)
        target_number = -1