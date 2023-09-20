N = int(input())

score = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    sum = 0
    for j in range(3):
        a = score[i][j]
        check = 1
        for k in range(N):
            if i == k:
                continue
            if a == score[k][j]:
                check = 0
                break
        if check == 1:
            sum += a
    print(sum)

# print(score)