P, K = map(int, input().split())
cnt = 1
for i in range(K, P):
    K += 1
    cnt += 1
    if P == K:
        print(cnt)