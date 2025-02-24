N = int(input())
arr = []

def sum_digits(serial):
    total = 0
    for char in serial:
        if char.isdigit():
            total += int(char)
    return total

def compare(serial):
    return (len(serial), sum_digits(serial), serial)

for i in range(N):
    serial = input()
    arr.append(serial)

sorted_serial = sorted(arr, key=compare)

for i in sorted_serial:
    print(i)