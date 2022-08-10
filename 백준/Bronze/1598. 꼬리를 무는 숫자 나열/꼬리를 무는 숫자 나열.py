# 칸마다 4씩 차이가 발생
N, M = map(int, input().split())
N-=1
M-=1
# 11//4 = 2 33//4 = 8  == 6
# 11%4 = 3 33%4 = 1 == 4 == 2
res = abs(N//4-M//4) + abs(N%4-M%4)
print(res)