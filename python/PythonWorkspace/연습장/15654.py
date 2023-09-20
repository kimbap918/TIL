import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * N
ans = []

def backtraking(depth, N, M):
    if depth == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            ans.append(arr[i])
            backtraking(depth+1, N, M)
            # 백트래킹
            ans.pop()
            visited[i] = False


backtraking(0, N, M)

