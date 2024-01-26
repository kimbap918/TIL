import sys

h, m, s = map(int, sys.stdin.readline().split())
for _ in range(int(sys.stdin.readline())):
    li = list(map(int, sys.stdin.readline().split()))
    if len(li) == 1 and li[0] == 3:
        print(h, m, s)
    else:
        t = h*3600 + m*60 + s
        t += (li[1] if li[0] == 1 else -li[1])
        if t < 0:
            t += 86400
        t = t%86400
        h, m, s = t//3600, (t%3600)//60, t%60