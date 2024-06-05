import sys
input = sys.stdin.readline

# 입력
a, b = map(int, input().split())

# 이진수로 변환
bin_a = bin(a)
bin_b = bin(b)

# c
res = int(bin(a^b)[2:], 2)
print(res)