N, M = map(int, input().split())

castle = [list(map(str, input())) for _ in range(N)]
cnt1, cnt2 = 0, 0
for n in range(N):
    if "X" not in castle[n]:
        cnt1 += 1

for m in range(M):
    if "X" not in [castle[n][m] for n in range(N)]:
        cnt2 += 1

print(max(cnt1, cnt2))