import sys
input = sys.stdin.readline

N = int(input())
S = [[] for _ in range(N + 1)]
for i in range(1, N+1):
    S[i] = input().rstrip()
ans1, ans2 = 9**9, 0

print(S)
def DFS(h, n, score):
    score += ord(S[h][n]) - ord('A') + 1
    print(S[h][n])
    if h < N:
        DFS(h + 1, n * 2, score)
        DFS(h + 1, n * 2 + 1, score)
    else:
        global ans1, ans2
        ans1 = min(ans1, score)
        ans2 = max(ans2, score)
    
DFS(1, 0, 0)
# print(ans1, ans2, sep='\n')