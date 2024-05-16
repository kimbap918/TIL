import sys

input = sys.stdin.readline

# 25 7 5
A, B, N = map(int, input().split())

for i in range(N):
    A = (A%B)*10
    ans = A//B
print(ans)


# N 번 시행

# 25 % 7 = 4 * 10 = 40
# 40 // 7 = 5

# 40 % 7 = 5 * 10 = 50
# 50 // 7 = 7

# 50 % 7 = 1 * 10 = 10
# 10 // 7 = 1

# 10 % 7 = 3 * 10 = 30
# 30 // 7 = 4

# 30 % 7 = 2 * 10 = 20
# 20 // 7 = 2

# 답 2