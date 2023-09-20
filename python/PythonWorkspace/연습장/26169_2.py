import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def DFS(arr, row, col, apple, move):
    x, y = row, col

    if apple >= 2:
        return True
    
    if move == 3:
        return False
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위를 벗어나는 경우
        if nx < 0 or ny < 0 or nx >= board_size or ny >= board_size:
            continue

        # 장애물이 있는 칸의 경우
        if arr[nx][ny] == -1:
            continue

        # 사과가 있는 경우
        if arr[nx][ny] == 1:
            # 빈 칸으로 변경
            arr[nx][ny] = 0

        arr[x][y] = -1

        if DFS(arr, nx, ny, apple+1, move+1):
            return True
        arr[x][y] = 0

        if arr[nx][ny] == 1:
            arr[nx][ny] = 1

    return False


board_size = 5
board = [list(map(int, input().split())) for _ in range(board_size)]
r, c = map(int, input().split())
move, apple = 0, 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

res = DFS(board, r, c, apple, move)

if res:
    print(1)
else:
    print(0)
