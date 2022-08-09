while True:
    cnt = 0
    S = input()
    if S == "#":
        break
    for i in S:
        if i in "aeiouAEIOU":
            cnt += 1
    print(cnt)