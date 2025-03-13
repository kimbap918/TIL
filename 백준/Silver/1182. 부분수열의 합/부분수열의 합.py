def dfs(index, sum):
    global cnt 

    if sum == S and index >= 1:
        cnt += 1

    for i in range(index, N):
        sum += arr[i]
        dfs(i+1, sum)
        sum -= arr[i]

    return cnt

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

print(dfs(0, 0))

