# 2068
T = int(input())

for test_case in range(1, T + 1):
    a = map(int, input().split())
    b = list(a)
    max = 0
    for i in range(len(b)):
        if max < b[i]:
            max = b[i]
    print("#{0} {1}".format(test_case, max))