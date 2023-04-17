import sys
import heapq as hq
input = sys.stdin.readline

heap = []
for i in range(int(input())):
    x = int(input())
    if x:
        hq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap)[1])
        else:
            print(0)