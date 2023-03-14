n, h, v = map(int, input().split())
res = max(h, n-h) * max(v, n-v)
print(res*4)