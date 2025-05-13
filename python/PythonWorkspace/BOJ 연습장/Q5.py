# import itertools

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# res = list(itertools.combinations(arr, 2))
# cnt = len(res)

# for i in res:
#     A, B = i[0], i[1]
#     if A == B:
#         cnt -= 1


# print(cnt)


N, M = map(int, input().split())
data = list(map(int, input().split()))

arr = [0] * 11

for x in data:
    arr[x] += 1

res = 0
for i in range(1, M+1):
    N -= arr[i] # arr[i] 볼링공 개수
    res += arr[i] * N # (무게 i인 볼링공 수) × (무게 i보다 큰 볼링공 수)

    # 5 3
    # 1 3 2 3 2
    # [0, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0]
    # 5 -= 1 = 4
    # 1 * 4 = 4
    # 0 + 4 = 4

    # 4 -= 2 = 2
    # 2 * 2 = 4
    # 4 + 4 = 8
    
print(res)
print(arr)
