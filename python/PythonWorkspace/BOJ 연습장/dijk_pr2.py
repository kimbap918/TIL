import sys
import heapq
input = sys.stdin.readline

N, M, C = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(N+1)]  # 인접 리스트로 초기화
distance = [INF] * (N+1)

for _ in range(M):
    # 출발지, 목적지, 비용
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(C)

# 도달할 수 있는 도시 수와 최대 거리 계산
cnt = 0
max_dist = 0
for i in range(1, N+1):
    # 자기 자신(C)은 제외하고, 도달 가능한 도시만 카운트
    if distance[i] != INF and i != C:
        cnt += 1
        max_dist = max(max_dist, distance[i])

print(cnt, max_dist)