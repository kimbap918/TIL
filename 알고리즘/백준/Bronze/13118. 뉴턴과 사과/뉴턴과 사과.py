li = list(map(int, input().split()))
x, y, r = map(int, input().split())
print(li.index(x)+1 if x in li else 0)