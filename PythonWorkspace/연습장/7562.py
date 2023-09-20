import sys
from collections import deque
input = sys.stdin.readline

# 나이트의 이동 경로 8가지
dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def BFS(x1, y1, x2, y2):
    Q = deque()
    Q.append([x1, y1])
    # 방문처리
    board[x1][y1] = 1
    
    while Q:
        a, b = Q.popleft()
        if a == x2 and b == y2:
            print(board[x2][y2] -1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            # 범위 내의 위치에서 이동횟수 기록
            if 0 <= x < I and 0 <= y < I and board[x][y] == 0:
                Q.append([x, y])
                board[x][y] = board[a][b]+1
            


T = int(input())
for _ in range(T):
    # 체스판 한 변의 길이
    I = int(input())
    board = [[0] * I for _ in range(I)]
    # pprint(board)
    # 나이트가 현재 있는 칸
    X1, Y1 = map(int, input().split())
    # 나이트가 이동하려는 칸
    X2, Y2 = map(int, input().split())
    BFS(X1, Y1, X2, Y2)