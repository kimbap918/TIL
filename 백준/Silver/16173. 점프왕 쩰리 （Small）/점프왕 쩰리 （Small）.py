import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def DFS(x, y):
    if 0 <= x < N and 0 <= y < N and visited[x][y] == False:
        visited[x][y] = True        

        DFS(x+board[x][y], y)
        DFS(x, y+board[x][y])
    else:
        return

    if board[x][y] == -1:
        visited[x][y] = True
        return



N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]



DFS(0, 0)
        
if visited[-1][-1] == True:
    print("HaruHaru")
else:
    print("Hing")