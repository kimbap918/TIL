import sys
import math
from heapq import heappush, heappop
input = sys.stdin.readline
INF = math.inf

# 걸어서 갈 때와 순간이동으로 갈 때의 가중치가 다르므로 다익스트라 알고리즘을 사용
N, K = map(int, input().split())
MAX = 100001
dist = [INF] * MAX
heap = []

def dijkstra(n, k):
    if k <= n:
        print(n-k)
        return
    
    heappush(heap, [0, n])
    while heap:
        w, x = heappop(heap)
        for nx in (x+1, x-1, x*2):
            if 0 <= nx < MAX:
                # 순간 이동은 0초, 걸어서 갈땐 1초
                if nx == x*2 and dist[nx] == INF:
                    dist[nx] = w
                    heappush(heap, [w, nx])
                elif dist[nx] == INF:
                    dist[nx] = w + 1
                    heappush(heap, [w+1, nx])
    print(dist[k])

dijkstra(N, K)