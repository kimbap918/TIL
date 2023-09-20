import sys
input = sys.stdin.readline

# 4
# 2 3 3 3 
# 3
# 1 4 10

# 1. 추를 더한다.
# 2. 추를 뺀다.
# 3. 추를 사용하지 않는다.

N = int(input())
weight = list(map(int, input().split()))
n = int(input())
marbles = list(map(int, input().split()))

dp = [0]
for chu in weight:
    tmp = []
    for i in dp:
        tmp.append(i+chu)
        tmp.append(abs(i-chu))
    dp = list(set(dp+tmp))

for marble in marbles:
    if marble in dp:
        print("Y", end=' ')
    else:
        print("N", end=' ')