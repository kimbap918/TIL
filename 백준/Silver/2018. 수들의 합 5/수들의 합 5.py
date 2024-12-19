def two(N):
    start, end = 1, 1
    cur_sum = 1
    cnt = 0

    if N == 1 or N == 2:
        return 1

    while start <= N // 2+1:
        if cur_sum < N:
            end += 1
            cur_sum += end
        elif cur_sum > N:
            cur_sum -= start
            start += 1
        else: # cur_sum == N
            cnt += 1
            cur_sum -= start
            start += 1
    return cnt + 1


N = int(input())
print(two(N))