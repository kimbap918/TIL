a, b = map(int, input().split())
res = 1
for i in range(a, b+1):
    res *= sum([j for j in range(1, i+1)])
print(res%14579)