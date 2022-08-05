# 1. 현재 박스 아래에 박스가 없어야 한다.
# 2. 박스는 바닥을 벗어나면 안된다. -> 리스트의 범위를 벗어나면 안된다.
# 3. 박스이동 -> 현재 위치는 0 저장, 아래 위치는 1 저장

T = int(input())

for _ in range(T):
    N, M = map(int, input().split()) # N 행 M 열
    box_list = [list(map(int, input().split())) for _ in range(N)] 
    box = 1
    empty = 0
    move = 0

    # 2중 반복문
    # 열부터 순환
    for x in range(M): # 열(row) 개수
        # 행순회, 단 아래에서 위로 탐색을 한다.
        for y in range(N-1,-1,-1): # 4 3 2 1 0
            
            # 만약에 현재 탐색하고 있는 좌표에 박스가 있으면
            if box_list[y][x] == box:
                while True:
                    # 조건1. 현재 박스 아래에 박스가 없어야 한다.
                    if y+1 == N:
                        break
                    # 조건2. 박스가 바닥을 벗어나면 안된다.
                    if box_list[y+1][x] == box:
                        break
                
                    box_list[y][x] = empty
                    box_list[y+1][x] = box
                    y += 1
                    move += 1

    print(move)