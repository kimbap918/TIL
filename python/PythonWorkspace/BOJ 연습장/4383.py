while True:
    try:
        jumper = list(map(int, input().split()))
        N = jumper[0]
        res = []
        # 1부터 n-1까지 모두 나와야 Jolly jumper
        for i in range(1, len(jumper)-1):
            res.append(abs(jumper[i] - jumper[i+1]))

        if sum(set(res)) == int((N*(N+1)/2)-N):
            print("Jolly")
        else:
            print("Not jolly")
    except:
        break
