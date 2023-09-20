import sys
input = sys.stdin.readline

N, M, B = map(int,input().split())
block = []
for _ in range(N):
    block.append([ int(i) for i in input().rstrip().split()])
ans = int(1e9)
glevel = 0

# 땅의 높이 256
for i in range(257): 
    use = 0
    take  = 0
    for j in range(N):
        for k in range(M):
            if block[j][k] > i:
                take += block[j][k] - i
            else:
                use += i - block[j][k]

    if use > take + B:
        continue

    cnt = take * 2 + use

    if cnt <= ans:
        ans = cnt
        hight = i

print(ans, hight)
