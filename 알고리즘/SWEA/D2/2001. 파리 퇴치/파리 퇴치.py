T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    fly = 0

    for r in range(N-M+1): # N에서 파리채의 범위를 이동하면서 탐색
        for c in range(N-M+1): # 0 1, 0 2, 0 3, 1, 0, 1, 1, 1, 2 ... 3 3
            sum_result = 0
            for mr in range(M): # 파리채의 범위
                for mc in range(M): # MxM의 범위를 탐색하면서 값을 누적
                    sum_result += N_list[r+mr][c+mc]
            if sum_result > fly: # 가장 큰 누적값을 fly에 저장
                fly = sum_result


    print("#{} {}".format(t, fly))
