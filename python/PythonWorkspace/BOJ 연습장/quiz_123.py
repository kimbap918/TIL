from pprint import pprint

R, C = map(int, input().split()) # 열과 행
building = "#" # 빌딩
car = "X" # 차
void = "." # 빈 공간
break_count_list = [0] * 5 # 부순횟수를 저장할 리스트 

# 델타 탐색 우, 하, 우하
dr = [1, 0, 1] 
dc = [0, 1, 1]

map_list = [list(map(str, input())) for _ in range(R)]
# pprint(map_list)


for r in range(R):
    for c in range(C):
        break_count = 0

        if map_list[r][c] == building:
            continue
        
        if map_list[r][c] == car:
            break_count += 1    


        for d in range(3):
            next_dr = r + dr[d]
            next_dc = c + dc[d]

            if not (-1 < next_dr < R and -1 < next_dc < C):
                break

            if map_list[next_dr][next_dc] == building:
                break

            if map_list[next_dr][next_dc] == car:
                break_count += 1

        else:
            break_count_list[break_count] += 1

for count in break_count_list:
    print(count)