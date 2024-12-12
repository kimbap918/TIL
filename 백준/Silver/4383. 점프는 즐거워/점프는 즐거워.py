while True:
    try:
        # 입력받고 분리
        jumper = list(map(int, input().split()))
        N = jumper[0]
        sequence = jumper[1:]

        # 길이가 1인 경우 무조건 Jolly
        if N == 1:
            print("Jolly")
            continue

        # 절댓값 차이를 집합으로 저장
        differences = set(abs(sequence[i] - sequence[i + 1]) for i in range(N - 1))

        # 1부터 N-1까지 차이를 모두 포함하는지 확인
        if differences == set(range(1, N)):
            print("Jolly")
        else:
            print("Not jolly")
    except EOFError:
        break
