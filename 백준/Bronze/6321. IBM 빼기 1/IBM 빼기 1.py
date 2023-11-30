import sys
input = sys.stdin.readline

n = int(input())

for x in range(1, n + 1):
    data = input().rstrip()
    result = ''
    for i in range(len(data)):
        value = ord(data[i]) + 1
        if value > 90:
            value = 65
        result += chr(value)

    print('String #%d' % x)
    print(result)
    print()