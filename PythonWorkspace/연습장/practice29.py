import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
cnt = [0 for _ in range(N+1)] # 연결된 물탱크의 개수를 담아둔다.
cycle = []

for i in range(N):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    cnt[u] += 1
    cnt[v] += 1

flag = False
while True:
    if flag: # True 반환시 종료
        break
    else:
        flag = True
        for i in range(1, N+1):
            if cnt[i] == 1: # 물탱크의 개수가 하나라면?
                j = graph[i][0] # 물탱크의 값을 j에 저장
                graph[i] = 0
                graph[j].remove(i)
                cnt[i] -= 1
                cnt[j] -= 1
                flag = False
                break
    
for i in range(1, N+1):
    if cnt[i] > 0:
        cycle.append(i)

print(len(cycle))
print(*cycle)