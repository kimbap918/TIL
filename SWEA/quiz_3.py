
# 2071
T = int(input())
b = 0
for test_case in range(1, T + 1):
    N = map(int, input().split())
    a = list(N)
    for i in range(len(a)):
        b += a[i]
    print("#"+str(test_case)+" "+format(b/len(a), ".0f"))
    a = []
    b = 0
