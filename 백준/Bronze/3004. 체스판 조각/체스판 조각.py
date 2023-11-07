N = int(input())
ans = 1
a = 1
for i in range(N):
    ans += a
    if i%2 == 0:
        a += 1
print(ans)