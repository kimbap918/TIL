# N = int(input()) # 보드의 크기
# K = int(input()) # 사과의 개수
# dx = [0, 1, 0, -1] # 동, 남, 서 북
# dy = [1, 0, -1, 0]
# board = list([0] * (N+1) for _ in range(N+1))
# directions = []

# for _ in range(K):
#     row, col = map(int, input().split())
#     board[row][col] = 1
#     # 3 4
#     # 2 5
#     # 5 3

# L = int(input()) # 방향 변환 횟수
# for _ in range(L):
#     X, C = input().split() # X초가 끝난 뒤에 L(완쪽) D(오른쪽)으로 90도 회전
#     directions.append((int(X), C))

# def turn(dir, C):
#     # L이 왼쪽, 
#     # 동(0, 1) -> 북(-1, 0), 남(1, 0) -> 동(0, 1)
#     # 서(0, -1) -> 남(1, 0), 북(-1, 0) -> 서(0, -1)
#     if C == "L": 
#         dir = (dir - 1) % 4
#     else:
#         dir = (dir + 1) % 4
#     return dir

# def simulate():
#     x, y = 1, 1
#     board[x][y] = 2 # 뱀의 위치
#     direction = 0
#     time = 0
#     index = 0

#     q = [(x, y)]
#     while True:
#         nx = x + dx[direction]
#         ny = y + dy[direction]

#         if 1 <= nx and nx <= N and 1 <= ny and ny <= N and board[nx][ny] != 2:
#             if board[nx][ny] == 0:
#                 board[nx][ny] = 2
#                 q.append((nx,ny))
#                 px, py = q.pop(0)
#                 board[px][py] = 0

#             if board[nx][ny] == 1:
#                 board[nx][ny] = 2
#                 q.append((nx,ny))
#         else:
#             time += 1
#             break

#         x, y = nx, ny
#         time += 1
#         if index < L and time == directions[index][0]:
#             direction = turn(direction, directions[index][1])
#             index += 1
#     return time

# print(simulate())








# 3 D
# 15 L
# 17 D

# [[1, 0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 2, 0], 
#  [0, 0, 0, 2, 0, 0], 
#  [0, 0, 0, 0, 0, 0], 
#  [0, 0, 2, 0, 0, 0], 
#  [0, 0, 0, 0, 0, 0]]



N = int(input())  # 보드 크기
K = int(input())  # 사과 개수
dx = [0, 1, 0, -1]  # 동, 남, 서, 북
dy = [1, 0, -1, 0]
board = [[0] * (N + 1) for _ in range(N + 1)]
directions = []

# 사과 위치 입력
for _ in range(K):
    row, col = map(int, input().split())
    board[row][col] = 1

L = int(input())  # 방향 변환 개수
for _ in range(L):
    X, C = input().split()
    directions.append((int(X), C))

def turn(dir, C):
    """ 뱀의 방향을 회전 """
    if C == "L":
        dir = (dir - 1) % 4
    else:
        dir = (dir + 1) % 4
    return dir

def simulate():
    """ 게임 진행 함수 """
    x, y = 1, 1  # 뱀의 시작 위치
    board[x][y] = 2  # 뱀이 위치한 곳 표시
    direction = 0  # 현재 방향 (0: 동, 1: 남, 2: 서, 3: 북)
    time = 0  # 게임 시간
    index = 0  # 방향 변환 인덱스
    q = [(x, y)]  # 뱀의 위치를 저장하는 큐

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 벽에 부딪히거나 자기 자신과 부딪히면 게임 종료
        if 1 <= nx <= N and 1 <= ny <= N and board[nx][ny] != 2:
            # 사과가 없으면 꼬리 제거
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)  # 꼬리 제거
                board[px][py] = 0  # 꼬리 지운 자리 0으로 초기화

            # 사과가 있으면 그대로 유지 (꼬리 안 줄어듦)
            elif board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))

        else:
            time += 1  # 벽 또는 자기 자신 충돌 시 종료
            break

        x, y = nx, ny  # 뱀 머리 위치 갱신
        time += 1  # 시간 증가

        # 방향 변환
        if index < len(directions) and time == directions[index][0]:
            direction = turn(direction, directions[index][1])
            index += 1

    return time

# 결과 출력
print(simulate())
