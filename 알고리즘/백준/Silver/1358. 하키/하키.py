import math
import sys

input = sys.stdin.readline
W, H, X, Y, P = map(int, input().split())
cnt = 0
# W * H 크기의 직사각형 (가로, 세로)
# 반지름(R)이 H/2, 중심이 (X, Y+R), (X+W, Y+R)인 두 원
for _ in range(P):
    x, y = map(int, input().split())
    # 1) 가운데 직사각형 부분에 선수가 있는 경우
    # 2) 왼쪽 반원에 있는 경우
    # 3) 오른쪽 반원에 있는 경우
    if(X <= x <= X+W) and (Y <= y <= Y+H): # 하키 선수의 좌표 x, y가 둘레 포함해서 직사각형 안에 있는 경우
        cnt += 1
        continue

    R = H/2
    d1 = math.sqrt((x-X)**2 + (y-(Y+R))**2) # 왼쪽반원
    d2 = math.sqrt((x-(X+W))**2 + (y-(Y+R))**2) # 오른쪽 반원
    if d1 <= R or d2 <= R:
        cnt += 1
print(cnt)