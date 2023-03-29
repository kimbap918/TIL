import sys

input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

res = []

def paperchk(x, y, N):
    check = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if check != paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        paperchk(x+k*N//3, y+l*N//3, N//3)
                return

    if check == -1:
        res.append(-1)
    elif check == 0:
        res.append(0)
    else:
        res.append(1)


paperchk(0, 0, N)
print(res.count(-1))
print(res.count(0))
print(res.count(1))
