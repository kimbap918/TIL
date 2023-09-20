import sys
input = sys.stdin.readline
arr1 = []
arr2 = []
cnt = 0

N, M = map(int, input().split())

for i in range(N):
    board = list(map(int, input().split()))
    for j in range(N):
        # 개미인 경우
        if board[j] == 1:
            arr1.append([i, j])
        # 진드기인 경우
        elif board[j] == 2:
            arr2.append([i, j])

for x1, y1 in arr1:
    for x2, y2 in arr2:
        if abs(x1-x2) + abs(y1-y2) <= M:
            cnt += 1
            break

print(cnt)
