import sys
graph = []
blank = []

input = sys.stdin.readline

# 1. 먼저 문제에서 빈 칸은 0으로 주어지기 때문에 graph의 0인칸의 위치정보(x, y)를 blank 리스트에 넣어준다.
# 2. 첫 번째 빈칸에 1~9까지의 수 중 넣을 수 있는 수를 넣는다. 넣을 수 있는 수는 빈칸의 행,열,3x3정사각형에 없는 수임을 확인하자. 확인이 되면 그 빈칸에는 그 수를 넣어준다.
# 3. 그 다음 빈칸에 대해서도 같은 방법을 수행한다.
# 4. 마지막 빈칸까지 채우면 스도쿠를 완성하므로 맵을 출력한다.

for i in range(9): # graph에 스도쿠의 입력값을 넣어준다.
    graph.append(list(map(int, input().rstrip().split())))

    # 0 3 5 4 6 9 2 7 8
    # 7 8 2 1 0 5 6 0 9
    # 0 6 0 2 7 8 1 3 5
    # 3 2 1 0 4 6 8 9 7
    # 8 0 4 9 1 3 5 0 6
    # 5 9 6 8 2 0 4 1 3
    # 9 1 7 6 5 2 0 8 0
    # 6 0 3 7 0 1 9 5 2
    # 2 5 8 3 9 4 7 6 0

for i in range(9): # 스도쿠의 값 중 빈칸인 0 값을 찾아서 위치값을 blank에 넣어준다.
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

def checkRow(x, a): # 열에서 1~9중 겹치는 숫자가 있는지 확인, 겹치는 숫자가 있다면 False를 반환
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y, a): # 행에서 1~9중 겹치는 숫자가 있는지 확인, 겹치는 숫자가 있다면 False를 반환
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a): # 3*3 정사각형 안에서 1~9의 수 중 겹치는 수가 있는지를 확인, 있다면 False를 반환
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank): # 인덱스가 blank위치정보의 길이와 같아지면 종료, graph의 값들을 전부 출력함
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        # print(idx)
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i): # 열, 행, 정사각형이 모두 참 값이면 
            graph[x][y] = i # 그래프의 해당 값을 i로 변경
            dfs(idx+1) # idx 1 증가
            graph[x][y] = 0 # 초기화

dfs(0)