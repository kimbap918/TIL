
# ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ...
# ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ 
# ㅁ ㅁ ㅁ ㅁ ㅅ ㅁ ㅁ ㅁ
# ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ ㅁ

# S = 대각선 이동시 소요시간
# W = 가로, 세로 1칸 이동시 소요시간
X, Y, W, S = map(int, input().split())

method1 = (X+Y) * W # 가로/세로로만 이동 
method2 = min(X, Y) * S + abs(X-Y) * W # 대각선으로 최대한 이동 후에 남은 거리를 가로/세로로 이동

print(min(method1, method2))