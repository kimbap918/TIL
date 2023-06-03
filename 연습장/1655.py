import heapq
import sys
input = sys.stdin.readline

# 왼쪽 힙은 최대 힙으로 정렬하고, 오른쪽 힙은 최소 힙으로 정렬하면
# 왼쪽 힙의 첫번째 요소는 항상 중앙값이 된다.

min_heap = [] # 중간값 보다 작은 수
max_heap = [] # 중간값 보다 큰 수
ans = []
# 중간값은 leftheap의 root로 들어간다.

N = int(input())

for i in range(N):
    num = int(input())

    if len(min_heap) == len(max_heap):
        heapq.heappush(min_heap, -num)
    else:
        heapq.heappush(max_heap, num)
    # 힙의 가장 첫 번째 값, 즉 0번 인덱스 값은 해당 힙의 가장 우선순위가 높은 값
    # 왼쪽 힙 중 가장 우선순위가 높은 값 즉, 가장 큰 값이 오른쪽 힙의 가장 우선순위가 높은 값인 가장 작은 값보다 클 경우, 
    # 두 수를 바꿔주면 중간값을 기준으로 숫자들을 쭉 나눠놓을 수 있다
    if len(min_heap) >= 1 and len(max_heap) >= 1 and min_heap[0] * -1 > max_heap[0]:
        max_val = heapq.heappop(min_heap)
        min_val = heapq.heappop(max_heap)

        heapq.heappush(min_heap, min_val * -1)
        heapq.heappush(max_heap, max_val * -1)

    print(min_heap[0] * -1)


