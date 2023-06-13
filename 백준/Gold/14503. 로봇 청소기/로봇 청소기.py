from pprint import pprint
N, M = map(int, input().split())
# d = 0 북, 1 동 2 남 3 서
r, c, d = map(int, input().split())
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# d = (d+3) % 4  왼쪽으로 회전
# 3, 2, 1, 0 서 남 동 북
# [r - dx[dir]][c - dy[dir]] 후진

room = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
room[r][c] = 2
cnt = 1

# 왼쪽으로 회전시킨다.
def turn(d):
    d = (d+3) % 4
    return d

# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
#   1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
#   2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
# 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
#   1. 반시계 방향으로 90도 회전한다.
#   2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
#   3. 1번으로 돌아간다.

def robot(x, y, dir):
    global cnt
    if room[x][y] == 0:
        room[x][y] = 2
        cnt += 1

    for _ in range(4):
        nd = turn(dir)
        nx = x + dx[nd]
        ny = y + dy[nd]

        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            if not visited[nx][ny]:
                robot(nx, ny, nd)
                return
        dir = nd

    nd = (dir+2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if room[nx][ny] == 1:
        return
    robot(nx, ny, dir)

robot(r, c, d)
print(cnt)