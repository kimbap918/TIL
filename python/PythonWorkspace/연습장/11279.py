import sys
input = sys.stdin.readline

heap = [0]
capacity = 0

# 값 삽입
def push(heap, n):
    global capacity
    # heap 의 자리가 부족할경우 배열을 2배로 늘림
    if len(heap)-1 == capacity:
        heap += [0]*len(heap)

    capacity += 1
    heap[capacity] = n

    tn = capacity
    while(tn > 1):
        if heap[tn] > heap[tn//2]:
            temp = heap[tn]
            heap[tn] = heap[tn//2]
            heap[tn//2] = temp
            tn//=2
        else:
            break
    return heap

# 값 빼내기
def pop(heap):
    global capacity
    if capacity == 0:
        return 0
    p = heap[1]
    heap[1] = heap[capacity]
    heap[capacity] = 0

    tn = 1
    while(capacity > tn*2):
        if heap[tn*2] == 0 and heap[tn*2+1] == 0:
            break
        if heap[tn] < max(heap[tn*2], heap[tn*2+1]):
            temp = heap[tn]
            if heap[tn*2] > heap[tn*2+1]:
                heap[tn] = heap[tn*2]
                heap[tn*2] = temp
                tn*=2
            else:
                heap[tn] = heap[tn*2+1]
                heap[tn*2+1] = temp
                tn = tn*2+1
        else:
            break
    capacity -= 1
    return p

for i in range(int(input())):
    x = int(input())
    if x: # true
        heap = push(heap, x)
    else: # false
        print(pop(heap))

# import sys
# import heapq as hq
# input = sys.stdin.readline

# heap = []
# for i in range(int(input())):
#     x = int(input())
#     if x:
#         hq.heappush(heap, (-x, x))
#     else:
#         if len(heap) >= 1:
#             print(hq.heappop(heap)[1])
#         else:
#             print(0)