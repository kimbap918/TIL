import sys
input = sys.stdin.readline

R,C,T = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(R)]
robot_top = 0
robot_bottom = 0

#상 우 하 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def spread():  # 1초마다 미세먼지가 퍼지는 동작
    
    change = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y] > 0: # 미세먼지가 있는 경우
                tmp = 0
                for i in range(4):  # 4방면으로 퍼짐
                    ax = x + dx[i]
                    ay = y + dy[i]
                    if 0 <= ax < R and 0 <= ay < C:  # board 에서 벗어나지 않는 범위일 경우만
                        if board[ax][ay] != -1:  # 공기청정기가 아닌 위치만 확산
                            change[ax][ay] += board[x][y]//5
                            tmp += board[x][y]//5
                board[x][y] -= tmp
    for x in range(R):
        for y in range(C):
            board[x][y] += change[x][y]

def rotation():
    def top_rotate(): # 위쪽 회전
        d = 1 # 오른쪽 방향으로 시작
        before = 0
        x, y = robot_top, 1 # 공기청정기 머리부분의 바로 오른쪽 칸부터 시작
        while True:
            ax = x + dx[d]
            ay = y + dy[d]
            if ax == R or ay == C or ax == -1 or ay == -1: # 현재 좌표가 꼭짓점인 경우
                d = (d-1)%4
                continue
            if x == robot_top and y == 0: # 한 바퀴 회전 완료해서 공기청정기 좌표로 다시 돌아온 경우
                break
            board[x][y], before  = before, board[x][y]
            x, y = ax, ay


    def bottom_rotate():  # 아래 회전
        d = 1 # 오른쪽 방향으로 시작
        before = 0
        x, y = robot_bottom, 1 # 공기청정기 아래부분의 바로 오른쪽 칸부터 시작
        while True:
            ax = x + dx[d]
            ay = y + dy[d]
            if ax == R or ay == C or ax == -1 or ay == -1: # 현재 좌표가 꼭짓점인 경우
                d = (d+1)%4
                continue
            if x == robot_bottom and y == 0: # 한 바퀴 회전 완료해서 공기청정기 좌표로 다시 돌아온 경우
                break
            board[x][y], before  = before, board[x][y]
            x, y = ax, ay
            
    top_rotate()
    bottom_rotate()


for i in range(R): # 공기청정기의 위치를 찾기 위함
    if board[i][0] == -1:
        robot_top = i
        robot_bottom = i+1
        break

for _ in range(T): # T만큼 수행
    spread() 
    rotation() 
    
answer = 2  #공기청정기 2칸 -1인 것 상쇄하기 위함
for i in range(R):
    answer += sum(board[i])
print(answer)