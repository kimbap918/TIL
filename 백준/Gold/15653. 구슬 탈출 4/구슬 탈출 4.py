import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def move(x, y, dir):
    cnt = 0

    while board[x + dx[dir]][y + dy[dir]] != "#" and board[x][y] != "O":
        x += dx[dir]
        y += dy[dir]
        cnt += 1

    return x, y, cnt


def BFS(x1, y1, x2, y2):
    Q = deque([[x1, y1, x2, y2, 1]])

    while Q:
        rx, ry, bx, by, cnt = Q.popleft()
        visited[rx][ry][bx][by] = True
        
        for i in range(4):
            rnx, rny, rcnt = move(rx, ry, i)
            bnx, bny, bcnt = move(bx, by, i)

            if board[bnx][bny] != "O":
                if board[rnx][rny] == "O":
                    print(cnt)
                    exit(0)
            
                if bnx == rnx and bny == rny:
                    if rcnt > bcnt:
                        rnx -= dx[i]
                        rny -= dy[i]
                    else:
                        bnx -= dx[i]
                        bny -= dy[i]

                if not visited[rnx][rny][bnx][bny]:
                    visited[rnx][rny][bnx][bny] = True
                    Q.append([rnx, rny, bnx, bny, cnt+1])
    print(-1)
    return

for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            rx, ry = i, j
        if board[i][j] == "B":
            bx, by = i, j

BFS(rx, ry, bx, by)