X, Y = map(int, input().split())
li = [X/Y]
for _ in range(int(input())):
    X, Y = map(int, input().split())
    li.append(X/Y)
print("%.2f" % (min(li)*1000))