N, X = map(int, input().split())
arr = list(map(int, input().split()))
index = 0
res = []

current_sum = sum(arr[:X])
res = current_sum
cnt = 1

for i in range(X, N): # 2, 3, 4
    # 
    current_sum = current_sum - arr[i-X] + arr[i]

    if current_sum > res:
        res = current_sum 
        cnt = 1
    elif current_sum == res:
        cnt += 1

if res == 0:
    print("SAD")
else:
    print(res)
    print(cnt)



# 간동안의 방문자들을 구하는 시간복잡도를 낮출 방법
# O(1)만에 구하는 방법


# 5 2
# 1 4 2 5 1

# 1 4 -> 0, 1
# 4 2 -> 1, 2
# 2 5 -> 2, 3
# 5 1 -> 3, 4


# 7 5
# 1 1 1 1 1 5 1

# 1 1 1 1 1 -> 0 1 2 3 4
# 1 1 1 1 5 -> 1 2 3 4 5
# 1 1 1 5 1 -> 2 3 4 5 6

# 5 2
# 1 4 2 5 1
# [5, 6, 7, 6, 1, 0]

# 7 5
# 1 1 1 1 1 5 1
# [5, 9, 9, 8, 7, 6, 1, 0]