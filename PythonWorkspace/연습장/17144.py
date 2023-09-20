# 1. 미세먼가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
# (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
# 확산되는 양은 Ar,c/5이고 소수점은 버린다.
# (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)*(확산된 방향의 개수)

# -> 8 - (8/5)*(3)
# -> 8 - 3 = 5

# 2. 공기청정기가 작동된다.
# 공기청정기에서는 바람이 나온다.
# 위쪽 공기청정기의 바람은 반시계방향으로 순환, 아래쪽 공기청정기는 시계 방향으로 순환한다.
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
top, bottom = 0, 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def spread():  # 1초마다 미세먼지가 퍼지는 동작
    change = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if A[r][c] > 0: # 미세먼지가 있는 경우
                tmp = 0

                for i in range(4):  # 4방면으로 퍼짐
                    nr = r + dx[i]
                    nc = c + dy[i]
                    if 0 <= nr < R and 0 <= nc < C:  # board 에서 벗어나지 않는 범위일 경우만
                        if A[nr][nc] != -1:  # 공기청정기가 아닌 위치만 확산
                            change[nr][nc] += A[r][c]//5
                            tmp += A[r][c]//5
                A[r][c] -= tmp
                
    for r in range(R):
        for c in range(C):
            A[r][c] += change[r][c]

def rotation():

    def top_rotate(): # 위쪽 회전
        d = 1 # 오른쪽 방향으로 시작
        before = 0
        r, c = top, 1 # 공기청정기 머리부분의 바로 오른쪽 칸부터 시작
        while True:
            nr = r + dx[d]
            nc = c + dy[d]
            if nr == R or nc == C or nr == -1 or nc == -1: # 현재 좌표가 꼭짓점인 경우
                d = (d-1)%4
                continue
            if r == top and c == 0: # 한 바퀴 회전 완료해서 공기청정기 좌표로 다시 돌아온 경우
                break
            A[r][c], before  = before, A[r][c]
            r, c = nr, nc

    def bottom_rotate():  # 아래 회전
        d = 1 # 오른쪽 방향으로 시작
        before = 0
        r, c = bottom, 1 # 공기청정기 아래부분의 바로 오른쪽 칸부터 시작
        while True:
            nr = r + dx[d]
            nc = c + dy[d]
            if nr == R or nc == C or nr == -1 or nc == -1: # 현재 좌표가 꼭짓점인 경우
                d = (d+1)%4
                continue
            if r == bottom and c == 0: # 한 바퀴 회전 완료해서 공기청정기 좌표로 다시 돌아온 경우
                break
            A[r][c], before  = before, A[r][c]
            r, c = nr, nc

    top_rotate()
    bottom_rotate()

for i in range(R): # 공기청정기의 위치를 찾기 위함
    if A[i][0] == -1:
        top = i
        bottom = i+1
        break

for _ in range(T): # T만큼 수행
    spread() 
    rotation() 
    
ans = 2  #공기청정기 2칸 -1인 것 상쇄하기 위함
for i in range(R):
    ans += sum(A[i])
print(ans)
