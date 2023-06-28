li = [input() for _ in range(6)]
cnt = li.count('W')
if cnt >= 5:
    print(1)
elif cnt >= 3:
    print(2)
elif cnt >= 1:
    print(3)
else:
    print(-1)