h, w = map(int, input().split())
a, b = max(h, w), min(h, w)
l1 = a/3 if a/3 <= b else b
l2 = b/2
print(max(l1, l2))