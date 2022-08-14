import sys

input = sys.stdin.readline

# 방향 및 x, y 계산을 위함
# 상, 하, 좌, 우
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# M = 맵의 크기, n = 로봇의 이동 횟수
M, n = map(int, input().split()) 
x, y = 0, 0 # 좌표
dir = 0 # 방향 
check = False

for _ in range(n):
    # 로봇의 커맨드 MOVE, TURN..  / 횟수 2, 3..
    com, num = map(str, input().rstrip().split()) # MOVE 10

    if com == "TURN": # 회전일 경우 
        if num == "1": # 1일 경우 (오른쪽 이동)
            dir -= 1 # 3
            if dir < 0:
                dir = 3 
        else: # 0일 경우 (왼쪽 이동) 
            dir += 1 # 1
            if dir > 3: 
                dir = 0 
    elif com == "MOVE":
        x += int(num) * dx[dir] 
        y += int(num) * dy[dir] 
    if x < 0 or x >= M or y < 0 or y >= M:
        print(-1)
        check = True
        break
if not check:
    print(x, y)