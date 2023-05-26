from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
y, x = map(int, input().split())
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
move = 0
eat = 0

def BFS(y, x):
    global eat
    global move
    Q = deque([[y, x]])

    while Q:
        col, row = Q.popleft()
        visited[col][row] = True
        if board[col][row] == 1:
            eat += 1
        if move > 2 and eat < 2:
            return 0
        if eat >= 2:
            return 1

        for i in range(4):
            ny = col + dy[i]
            nx = row + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5 and board[ny][nx] != -1 and not visited[ny][nx]:
                if board[ny][nx] == 1:
                    move += 1
                    eat += 1
                    Q.append([ny, nx])
                    visited[ny][nx] = True
                    board[ny][nx] = 0
                    
                elif board[ny][nx] == 0:
                    move += 1
                    Q.append([ny, nx])
                    visited[ny][nx] = True




print(BFS(y, x))




# pprint(board)
# print(visited)
# print(y, x)
# print(board[y][x])