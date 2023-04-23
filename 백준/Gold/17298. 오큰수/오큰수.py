import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split())) # 3 5 2 7
NGE = [-1] * N
stack = [] # 0 1 2 3

# 오른쪽에 있으면서 Aj보다 큰 수 중에서 가자 왼쪽에 있는 수
# 마지막은 오른쪽이 없으므로 무조건 -1이 나와야함
for i in range(N):
    while stack and stack[-1][0] < arr[i]:
        # arr값과 인덱스를 꺼낸다
        num, idx = stack.pop()
        NGE[idx] = arr[i]
    stack.append([arr[i], i])

print(*NGE)
