N, M = map(int, input().split())
li = list(map(int, input().split()))
res = 1
for n in li:
    res *= n
print(res%M)