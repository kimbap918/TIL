A, B = map(int, input().split())
li = []
for i in range(-1000, 10001):
    if i*(2*A-i) == B:
        li = list(set([-i, -(2*A-i)]))
print(*sorted(li))