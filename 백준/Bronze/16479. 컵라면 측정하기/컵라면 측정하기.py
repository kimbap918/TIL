k = float(input())
d1, d2 = map(float, input().split())
d1, d2 = min(d1, d2), max(d1, d2)
h = k**2 - ((d2-d1)/2)**2
print(h)