def find_max(N):
    cnt = 0
    num_arr = []

    for num in range(1, N+1):
        arr = [N, num]

        while True:
            next_num = arr[-2] - arr[-1]
            if next_num < 0:
                break
            arr.append(next_num)

        if len(arr) > cnt:
            cnt = len(arr)
            num_arr = arr
    return cnt, num_arr

N = int(input())
max_length, max_nums = find_max(N)


print(max_length)
print(' '.join(map(str, max_nums)))