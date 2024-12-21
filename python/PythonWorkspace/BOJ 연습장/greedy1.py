# N 배열의 크기 N
# M 번 더해서
# K 번을 초과하지 않게


# N = 5
# M = 8
# K = 3
# 2 4 5 4 6

# 6 6 6 5 6 6 6 5
# 18 + 5 + 18 + 5 = 46

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
# print(N, M, K)
# print(arr)

sort_arr = sorted(list((set(arr))))
max_num = sort_arr[-1]
nd_num = sort_arr[-2]

res = 0
chk = 0
cnt = 0

while cnt != M: 
    res += max_num
    chk += 1
    cnt += 1

    # print(res)
    if chk == K:
        res += nd_num
        chk = 0
        cnt += 1
        # print(res)


print(res)
