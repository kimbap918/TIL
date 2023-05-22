import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(N)]

cnt = 0

for i in range(N):
    a = ''
    for j in range(M):
        if board[i][j] == '-':
            if board[i][j] != a:
                cnt += 1
        a = board[i][j]

for j in range(M):
    a = ''
    for i in range(N):
        if board[i][j] == '|':
            if board[i][j] != a:
                cnt += 1
        a = board[i][j]

print(cnt)

