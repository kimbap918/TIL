
# ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ...
# ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ 
# ㅁ ㅁ ㅁ ㅁ ㅅ ㅁ ㅁ ㅁ
# ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ

# S = 대각선 이동시 소요시간
# W = 가로, 세로 1칸 이동시 소요시간
X, Y, W, S = map(int, input().split())

method1 = (X+Y) * W # 가로/세로로만 이동 
method2 = min(X, Y) * S + abs(X-Y) * W # 대각선으로 최대한 이동 후에 남은 거리를 가로/세로로 이동

if S < 2*W: # 대각선이 가로/세로 이동 2번보다 빠른 경우
    if (X+Y) % 2 == 0: # 합이 짝수이면 대각선만으로 이동 가능
        method3 = max(X, Y) * S
    else: # 합이 홀수이면 대각선 + 직선 1번
        method3 = (max(X, Y)-1) * S + W
else:
    method3 = method1


print(min(method1, method2, method3))