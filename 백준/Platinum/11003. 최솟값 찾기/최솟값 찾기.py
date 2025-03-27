# N, L
# 12 3 
import sys
from collections import deque
input = sys.stdin.readline 

N, L = map(int, input().split())
A = list(map(int, input().split()))
# D0 = A0-L+1 
# D0 = 1-3+1 = -1
# D1 = 
# Di = Ai-L+1

#i - L + 1이 0 이하인 경우는 범위를 벗어나는 값이므로 무시해야 함
dq = deque()
res = []


for i in range(N):
    # A[i-L+1:i+1]
    # []
    # []
    # [1, 5, 2]
    # [5, 2, 3]
    # [2, 3, 6]
    # [3, 6, 2]
    # [6, 2, 3]
    # [2, 3, 7]
    # [3, 7, 3]
    # [7, 3, 5]
    # [3, 5, 2]
    # [5, 2, 6]

    # A[max(0, i-L+1):i+1]
    # [1]
    # [1, 5]
    # [1, 5, 2]
    # [5, 2, 3]
    # [2, 3, 6]
    # [3, 6, 2]
    # [6, 2, 3]
    # [2, 3, 7]
    # [3, 7, 3]
    # [7, 3, 5]
    # [3, 5, 2]
    # [5, 2, 6]
    # 맨 앞 원소가 범위를 벗어나면 제거
    if dq and dq[0][1] < i-L+1:
        dq.popleft()

    # 새 원소가 덱의 맨 뒷 부분보다 작으면 
    while dq and dq[-1][0] > A[i]: 
        # 기존 큰 값 제거
        dq.pop()

    # 새 원소
    dq.append((A[i], i))


    res.append(dq[0][0])

print(' '.join(map(str, res)))

    # 음수를 제외한 A[i-L+1]부터, A[i+1]범위 까지 값 중 최소값
    # print(min(A[max(0, i - L + 1):i + 1]))
    # 1 1 1 2 2 2 2 2 3 3 2 2
