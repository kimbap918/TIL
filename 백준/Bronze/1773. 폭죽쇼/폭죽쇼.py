N, C = map(int, input().split())
check = [False]*(C+1)
ans = 0

for _ in range(N):
    n = int(input())
    for i in range(n, C+1, n):
        if not check[i]:
            check[i] = True
            ans += 1
print(ans)