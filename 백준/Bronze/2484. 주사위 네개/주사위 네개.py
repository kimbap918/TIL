from collections import Counter

N = int(input())
play = []

for i in range(N):
    A, B, C, D = map(int, input().split())
    check = Counter((A, B, C, D))
    big = max(check.items(), key=lambda x: x[1])
    
    if big[1] == 4:
        res = 50000 + big[0] * 5000
        play.append(res)
    elif big[1] == 3:
        res = 10000 + big[0] * 1000
        play.append(res)
    elif big[1] == 2:
        if len(check) != 2:
            res = 1000 + big[0] * 100
            play.append(res)
        else:
            tmp = list(check.keys())
            res = 2000 + tmp[0] * 500 + tmp[1] * 500
            play.append(res)
    else:
        res = max(check) * 100
        play.append(res)

print(max(play))