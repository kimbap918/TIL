# heapq
import heapq
from collections import defaultdict

heap = list()

# heap list에 원소 추가 
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
# 최소값으로 기준이 잡혀있음
# [3]
# [1, 3]
# [1, 3, 2]
print(heap)
# heapq로 변환

# defaultdict
dic1 = defaultdict(list)
dic2 = dict()

arr = list(map(int, input().split()))
for i in arr:
    dic1[i].append(1)
    if i not in dic2.keys():
        dic2[i] = 1
    else:
        dic2[i] += 1
print(dic1)
print(dic2)

listA = [["A", 3], ["A", 2], ["B", 5], ["C", 4]]
listA.sort(key = lambda x : (-x[1], x[0]))

print(listA)