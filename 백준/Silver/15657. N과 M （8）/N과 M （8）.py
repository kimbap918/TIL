N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = []

def dfs(start, depth):
    if depth == M:
        print(' '.join(map(str, res)))
        return

    for i in range(start, N): # 0부터 숫자개수까지
        res.append(arr[i])
        dfs(i, depth+1)
        res.pop()


dfs(0, 0)

