A, B = map(float, input().split())
M = (B-A)/400
res = 1 / (1 + 10**M)
print(res)