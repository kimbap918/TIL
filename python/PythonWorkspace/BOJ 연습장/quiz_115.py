# from pprint import pprint

# N = int(input())
# N_list = [list(map(int, input().split())) for _ in range(N)]
# a = []

# for r in range(N):
#     for c in range(N):
#         a.append(N_list[r][c])

# sorted(a, reverse=True)
# print(a[N-1])

import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N): # N번동안 반복 
    nums = list(map(int, input().split()))

    if not heap:
        for num in nums:
            heapq.heappush(heap, num) # heap에 num값을 푸시
    else:
        for num in nums:
            # print(num)
            # print(heap)
            if heap[0] < num: # 힙 리스트의 첫번째 요소가 num보다 작을 경우
                heapq.heappush(heap, num) # num을 heap에 푸시
                # print(heap)
                heapq.heappop(heap) # heap의 제일 작은 요소를 팝
                # print(heap)
print(heap[0])