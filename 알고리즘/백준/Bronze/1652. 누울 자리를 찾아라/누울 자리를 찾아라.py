N = int(input())

room = [list(map(str, input())) for i in range(N)]
r_seat = 0
c_seat = 0
for r in range(N):
    cnt_r = 0
    cnt_c = 0
    for c in range(N):
        # 가로
        if room[r][c] == '.': # 빈자리일때 
            cnt_r += 1  # 카운트 1 증가
        else:
            cnt_r = 0 # 짐을 만나면? 초기화
        if cnt_r == 2:
            r_seat += 1

        # 세로
        if room[c][r] == '.':
            cnt_c += 1
        else:
            cnt_c = 0
        if cnt_c == 2:
            c_seat += 1
print(r_seat, c_seat)
    
  