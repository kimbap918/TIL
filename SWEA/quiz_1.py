# 2029
T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, sys.stdin.readline().split())
    print('#{0} {1} {2}'.format(test_case, a//b, a%b))

