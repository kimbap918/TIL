# 1, 5, 10, 20, 40
import sys
input = sys.stdin.readline
N = int(input())
coins = [1, 5, 10, 20, 40]
cnt = 0

while N != 0:
    if N >= coins[-1]:
        N -= coins[-1]
        cnt += 1
    else:
        coins.pop()

print(cnt)


coin = [40, 20, 10, 5, 1]
N = int(input())
count = 0
for i in coin:
    count += N // i
    N %= i
print(count)

# 55 -> 55-40=15 -> 15-10->5 -> 5-5=0 3 
# 30? -> 