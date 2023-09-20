import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def DFS(arr, row, col, apple, move):
    x, y = row, col
    # 이동이 3회 이하면서 사과를 2개이상 먹었을 경우
    if apple >= 2:
        return True

    if move == 3:
        return False

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < board_size and 0 <= ny < board_size and arr[nx][ny] != -1:
            eaten = 0

            # 사과가 있는 경우
            if arr[nx][ny] == 1:
                eaten = 1
                # 사과를 먹었으므로 빈 칸으로 변경
                arr[nx][ny] = 0

            arr[x][y] = -1 # 현재 위치를 장애물로 변경
            if DFS(arr, nx, ny, apple+eaten, move+1):
                return True    
            arr[x][y] = 0 # 백트래킹 : 원래대로 복구

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
