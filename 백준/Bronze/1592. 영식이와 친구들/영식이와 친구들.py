N, M, L = map(int, input().split())
li = [0]*N
cnt = i = 0
while li[i] < M-1:
    li[i] += 1
    cnt += 1
    i = (i+L)%N if li[i]%2 == 1 else (i-L)%N
print(cnt)