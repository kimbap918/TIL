import sys
input = sys.stdin.readline

# 입력
K, L = map(int, input().split())

# 인수판별
for i in range(2, L):
    if K % i == 0:
        print("BAD", i)
        break
else:
    print("GOOD")