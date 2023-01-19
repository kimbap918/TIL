s, m = map(int, input().split())
if  s+m < 0 or s-m < 0 or (s + m) % 2:
    print(-1)
else:
    a = (s + m) // 2
    b = s - a
    print(max(a, b), min(a, b))