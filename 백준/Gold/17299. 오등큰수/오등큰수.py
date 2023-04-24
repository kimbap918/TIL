import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A_cnt = Counter(A)
NGF = [-1] * N
stack = []

for i in range(N):
    while stack and stack[-1][0] < A_cnt[A[i]]:
        num, idx = stack.pop()
        NGF[idx] = A[i]
    stack.append([A_cnt[A[i]], i])

print(*NGF)

