a, b, c = map(int, input().split())
cnt = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i, j, k)
            cnt += 1
print(cnt)

