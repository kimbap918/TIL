import sys
input = sys.stdin.readline

def DFS(arr, visited, start):
    visited.add(start)

    for i in arr[start]:
        if i not in visited:
            DFS(arr, visited, i)


N, M = map(int, input().split())
# 인접리스트
cows = [[] for _ in range(N+1)]
visited = set()

for _ in range(M):
    c1, c2 = map(int, input().split())
    cows[c1].append(c2)
    cows[c2].append(c1)

DFS(cows, visited, 1)

# 묶여있지 않은 소들의 리스트
cow_list = []
for i in range(2, N+1):
    if i not in visited:
        cow_list.append(i)

if cow_list:
    print(*cow_list, sep='\n')
else:
    print(0)
