import sys
N = int(input())
RGB = []

for i in range(N):
    RGB.append(list(map(int, input().split())))
    # RGB = [[26, 40, 83]]

for i in range(1, len(RGB)):
    RGB[i][0] += min(RGB[i-1][1], RGB[i-1][2]) # [0][1], [0][2] 중 최소값 누적
    RGB[i][1] += min(RGB[i-1][0], RGB[i-1][2])
    RGB[i][2] += min(RGB[i-1][0], RGB[i-1][1])
print(min(RGB[N-1][0], RGB[N-1][1], RGB[N-1][2]))