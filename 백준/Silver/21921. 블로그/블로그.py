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

