N = input().split('-')
ans = 0

for i in N[0].split('+'):
    ans += int(i)

for j in range(1, len(N)):
    for k in N[j].split('+'):
        ans -= int(k)

print(ans)