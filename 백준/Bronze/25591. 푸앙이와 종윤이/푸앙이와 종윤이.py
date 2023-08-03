import sys
input = sys.stdin.readline

# 입력
i, j = map(int, input().split())

# 계산
a = 100 - i
b = 100 - j
c = 100 - (a + b)
d = a * b

q = d // 100
r = d % 100

print(a, b, c, d, q, r)
print(c+q, r)