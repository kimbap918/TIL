# 쿼드트리
import sys

input = sys.stdin.readline

N = int(input())
video = [ list(map(int, input().rstrip())) for i in range(N)]

def quardtree(x, y, N):
    dot = video[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            # 0과 1이 섞여있을경우
            if dot != video[i][j]:
                dot = -1
                break
    if dot == -1:
        print("(", end='')
        N = N // 2
        quardtree(x, y, N)
        quardtree(x, y+N, N)
        quardtree(x+N, y, N)
        quardtree(x+N, y+N, N)
        print(")", end='')
    elif dot == 1: # 영상이 전부 1일 경우
        print(1, end='')
    else: # 영상이 전부 0인 경우
        print(0, end='')
quardtree(0, 0, N)

