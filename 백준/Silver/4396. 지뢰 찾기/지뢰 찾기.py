n = int(input())

mine_map = list(input() for _ in range(n))
mine_click = list(input() for _ in range(n))
mine_result = [['.'] * n for _ in range(n)]

# 열린 칸 주변에 지뢰가 몇개 있는지(열린칸에서 8방향을 탐색)
# ...
# .x.
# ...
dc = [-1, -1, -1, 0, 1, 1, 1, 0] # ex) -1,-1 = x보다 위,왼쪽 / -1,0 = x보다 위,중앙 
dr = [-1, 0, 1, 1, 1, 0, -1, -1] # -1,1 = x보다 위,오른쪽 / 0,1 = x보다 중앙,오른쪽


for c in range(n):
    for r in range(n):
        
        # 지뢰를 밟지 않았을 경우
        if mine_map[c][r] == "." and mine_click[c][r] == "x":
            # 클릭시 숫자를 뜨게하는 카운트
            cnt = 0
            # 클릭한 값(x)를 기준으로 8방위의 좌표를 확인 
            for k in range(8):
                nc = c + dc[k]
                nr = r + dr[k]
                # 좌표가 음수이거나(맵 밖을 벗어났거나), n보다 큰 경우 건너뜀
                if nc < 0 or nc >= n or nr < 0 or nr >= n:
                    continue
                # 좌표 안에 폭탄이 있을 경우
                if mine_map[nc][nr] == "*":
                    cnt += 1 # 숫자 카운트 증가(최대 8)
            # 클릭한 결과에 카운트를 저장한다 
            mine_result[c][r] = cnt

        # 지뢰를 밟았을 경우
        if mine_map[c][r] == "*" and mine_click[c][r] == "x":  
            for a in range(n):
                for b in range(n):
                    if mine_map[a][b] == "*":
                        mine_result[a][b] = "*"

#결과값 출력
for i in range(n):
    for j in range(n):
        print(mine_result[i][j], end='')
    print()
