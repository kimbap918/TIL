N, M = map(int, input().split())
arr = sorted(map(int, input().split()))  # 중복 제거 X, 정렬만 수행
visited = [False] * N
res = []


def dfs(depth):
    if depth == M:
        print(' '.join(map(str, res)))
        return

    prev = -1

    for i in range(N): # 0부터 숫자개수까지
        if not visited[i] and prev != arr[i]:
            visited[i] = True
            res.append(arr[i])
            prev = arr[i]
            dfs(depth+1)
            visited[i] = False
            res.pop()


dfs(0)

# [1, 7, 9]
# 1, 1 x
# 1, 7
# 1, 9
# 7, 1
# 7, 7 x
# 7, 9
# 9, 1
# 9, 7
# 9, 9 