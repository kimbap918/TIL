import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 세로의 길이, 가로의 길이 입력
N, M = map(int, input().split())
# 모래사장의 상태
S = [list(map(int, input().split())) for _ in range(N)]
# 모래사장의 방문 여부
visited = [[False for _ in range(M)] for _ in range(N)]
# 모래사장을 바로 갱신하지 않기 위해 가라앉을 칸을 기록
update = [[False for _ in range(M)] for _ in range(N)]
# print(visited)
# print(update)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(i, j):
    y, x = i, j
    for k in range(4):
        # 꺼낸 y, x에 4방위를 더한 값 저장 
        ny, nx = y + dy[k], x + dx[k]
        # 해당 범위를 벗어나면 건너뜀
        if ny < 0 or nx < 0 or ny >= N or nx >= M:
            continue
        # 방문한곳이거나 해당 칸이 모래로 채워져 있으면 건너뜀
        if visited[ny][nx] or not S[ny][nx]:
            continue
        # 방문한 곳을 모래로 처리
        visited[ny][nx] = True
        DFS(ny, nx)

day = 0
# 모래사장의 상태를 업데이트하고, 물에 의해 가라않게 되는 날짜를 계산
while True:
    island = 0
    for i in range(N):
        for j in range(M):
            # 방문한곳이거나 해당 칸이 모래로 채워져 있으면 건너뜀
            if visited[i][j] or not S[i][j]:
                continue
            # 방문처리 후 섬의 개수 증가
            visited[i][j] = True
            island += 1
            DFS(i, j)
    
    # 섬의 개수가 2개 이상이면 날짜를 출력하고 반복탈출
    if island > 1:
        print(day)
        exit(0)
    # 섬의 개수가 없으면 전부 가라앉은 것이므로 -1 출력 후 반복탈출
    if island == 0:
        print(-1)
        exit(0)
    
    for i in range(N):
        for j in range(M):
            for k in range(4):
                ny, nx = i + dy[k], j + dx[k]
                # 범위를 벗어나면 건너뜀
                if ny < 0 or nx < 0 or ny >= N or nx >= M:
                    continue
                # 현재 칸의 이웃 칸들 중 모래로 차 있는곳이 있으면 
                # 현재칸을 update리스트에 True로 변경
                if not S[ny][nx]:
                    update[i][j] = True
                    
    for i in range(N):
        for j in range(M):
            # 모래로 차 있는곳을 가라앉힘
            if update[i][j]:
                S[i][j] = 0
    
    for i in range(N):
        for j in range(M):
            update[i][j] = visited[i][j] = False
    day += 1