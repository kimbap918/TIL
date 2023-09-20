N, M = map(int, input().split())
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
arr = []

def dfs(a):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, N+1):
        arr.append(i)
        dfs(i)
        arr.pop()
dfs(1)
