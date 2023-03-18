N, K = map(int, input().split())
cnt = 0
ans = []

while N != cnt:
    cnt += 1
    if N % cnt == 0:
        ans.append(cnt)
if len(ans) < K:
    print(0)
else:
    print(ans[K-1])


