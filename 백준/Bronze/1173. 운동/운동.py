N, m, M, T, R = map(int, input().split())
cnt = t = 0
now = m
while cnt < N:
    if m+T > M:
        break
    if now + T <= M:
        now += T
        cnt += 1
    else:
        now = max(now-R, m)
    t += 1
print(t if cnt == N else -1)