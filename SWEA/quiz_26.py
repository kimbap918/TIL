N = int(input())
for i in range(1, N+1):
    a = str(i)
    cnt = 0
    for clap in a:
        if (clap == "3") or (clap == "6") or (clap == "9"):
            cnt += 1
    if cnt == 0:
        print(i, end=' ')
    else:
        print(cnt*'-', end=' ')
