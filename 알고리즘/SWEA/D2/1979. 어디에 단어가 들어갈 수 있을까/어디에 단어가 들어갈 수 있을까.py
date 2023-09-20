T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for r in range(N): # 가로
        cnt = 0
        cnt1 = 0
        for c in range(N): # 세로
        
            # 가로 확인하기
            if puzzle[r][c] == 1:
                cnt += 1
            if puzzle[r][c] == 0 or c == N-1:
                if cnt == K:
                    result += 1
                cnt = 0

            # 세로 확인하기
            if puzzle[c][r] == 1:
                cnt1 += 1
            if puzzle[c][r] == 0 or c == N-1:
                if cnt1 == K:
                    result += 1
                cnt1 = 0

    print("#{} {}".format(t, result))

