from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
y, x = map(int, input().split())
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def BFS(y, x):
    move = 0
    eat = 0

    if move > 3:
        return 0

    if eat >= 2 and move <= 3:
        return 1

    Q = deque([[y, x]])

    while Q:
        col, row = Q.popleft()

        for i in range(4):
            ny = col + dy[i]
            nx = row + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5 and board[ny][nx] != -1 and not visited[ny][nx]:

                if board[ny][nx] == 1:
                    eat += 1
                    move += 1
                    board[ny][nx] = 0
                    visited[ny][nx] = True
                    Q.append([ny, nx])
                elif board[ny][nx] == 0:
                    move += 1
                    Q.append([ny, nx])
                    visited[ny][nx] = True

                print(move)
    print(board)


print(BFS(y, x))




# pprint(board)
# print(visited)
# print(y, x)
# print(board[y][x])