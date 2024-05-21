import sys
input = sys.stdin.readline 

for _ in range(3):
    res = 0
    N = int(input())
    for i in range(N):
        num = int(input())
        res += num


    if res > 0:
        print("+")
    elif res < 0:
        print("-")
    else:
        print(0)
