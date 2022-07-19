# 2070
T = int(input())
b = ""

for test_case in range(1, T + 1):
    N = map(int, input().split())
    a = list(N)
    if a[0] > a[1]:
        b = ">"
    elif a[0] < a[1]:
        b = "<"
    else:
        b = "="
    print("#{0} {1}".format(test_case, b))
    
