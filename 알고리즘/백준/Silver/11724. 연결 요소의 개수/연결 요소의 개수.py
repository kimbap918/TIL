# visited[start] = False
# start를 한 횟수 2번이 연결요소의 개수
# 시작을 한 횟수 == 연결요소의 개수
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split()) # 6 5
adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0

def dfs(n): # dfs(1)
    visited[n] = True # visited[1]
    for i in adj_list[n]: #2,1,5,2,1,5,4,3,6,4
        if visited[i] == False: # if visited[2] == False:
            visited[i] = True # visited[2] = True
            dfs(i) # dfs(2) 1, 5, 2, 1, 5, 4 ... 순으로 쭉 순회


for _ in range(M):
    u, v = map(int, input().split()) # 1 2 / 2 5 / 5 1 / 3 4 / 4 6
    adj_list[u].append(v)
    adj_list[v].append(u)

for number in range(1, N + 1): # 1, 2, 3, 4, 5, 6
    if not visited[number]: # visited[1]
        visited[number] = True # visited[1] = True
        answer += 1 # answer = 1
        dfs(number) # dfs(1)

print(answer)