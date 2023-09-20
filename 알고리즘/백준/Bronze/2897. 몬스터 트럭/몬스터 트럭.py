# https://www.acmicpc.net/problem/2897 

# 우 우하 하
# x+1 ,(y+1,x+1), y+1
dr = [0, 1, 1]
dc = [1, 1, 0]
BUILDING = "#"
CAR = "X"
VOID = "."

# 숫자가 공백으로 나뉘어져있는 입력
R, C = list(map(int, input().split()))

list_ = []

# R 줄 만큼의 리스트를 입력
for _ in range(R):
    # 숫자 X 문자 O
    # 공백 X
    temp_list = list(input())
    list_.append(temp_list)

# 부순 횟수를 저장할 리스트
# 0개 1개 2개 3개 4개 부순횟수를 저장
break_count_list = [0] * 5

# 이중 반복문
for r in range(R):
    for c in range(C):
        # 차를 부순 횟수는 탐색을 할 때마다 초기화(0)
        break_count = 0
        
        # 조건 1. 기준 좌표가 빌딩(#)이면 안된다.
        if list_[r][c] == BUILDING:
            # 이 다음 반복문의 코드들을 무시하고, 다음 값을 탐색
            continue

        # 성립이 안되는 조건들은 continue로 지나가고,
        # 조건이 성립될 때만 정상적인 코드를 실행한다.

        # 조건 2. 기준 좌표가 차라면 부순 횟수 + 1
        if list_[r][c] == CAR:
            break_count += 1

        """
        델타탐색을 하는 로직
        """
        for d in range(3):
            next_r = r + dr[d]
            next_c = c + dc[d]

            # 조건 1. 범위를 벗어나면 안된다.
            if not (-1 < next_r < R and -1 < next_c < C):
                break

            # 조건 2. 탐색 좌표에 빌딩이 있으면 안된다.
            if list_[next_r][next_c] == BUILDING:
                break

            # 조건 3. 탐색 좌표에 차가 있으면 부순 횟수를 + 1
            if list_[next_r][next_c] == CAR:
                break_count += 1

        # break를 만나지 않고 for문이 끝났다면
        # 혜빈이가 정상적으로 주차를 했다는 소리
        else:
            break_count_list[break_count] += 1

# print(break_count_list)
# 정답 출력
for count in break_count_list:
    print(count)
