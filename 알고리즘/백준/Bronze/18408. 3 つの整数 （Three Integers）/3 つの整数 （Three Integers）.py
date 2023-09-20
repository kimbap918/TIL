A, B, C = map(int, input().split())
li = [A, B, C]
print(1 if li.count(1) > li.count(2) else 2)