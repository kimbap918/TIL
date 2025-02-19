N = int(input())
X, S = map(int, input().split())
weaponInfo = [list(map(int, input().split())) for _ in range(N)]

result = False

for c, p in weaponInfo:
    if c <= X and p > S:
        result = True
        break

if result:
    print("YES")
else:
    print("NO")
