import sys
input = sys.stdin.readline
K = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
bigW = 0
bigH = 0
bigHidx = 0
bigWidx = 0

smallW = 0
smallH = 0

# 오 : 1, 왼 : 2, 아 : 3, 위 : 4

for idx, temp in enumerate(arr):
    if temp[0] == 1 or temp[0] == 2:
        if bigW < temp[1]:
            bigWidx = idx
            bigW = temp[1]

    elif temp[0] == 3 or temp[0] == 4:
        if bigH < temp[1]:
            bigHidx = idx
            bigH = temp[1]

smallW = abs(arr[(bigWidx - 1) % 6][1] - arr[(bigWidx + 1) % 6][1])
smallH = abs(arr[(bigHidx - 1) % 6][1] - arr[(bigHidx + 1) % 6][1])
print(abs(((bigW * bigH) - (smallW * smallH))) * K)
