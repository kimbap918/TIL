import sys
import heapq

input = sys.stdin.readline
N = int(input())
heap = []

for i in range(N): # N만큼 반복
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
        #print(heap)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
            #print(heap)