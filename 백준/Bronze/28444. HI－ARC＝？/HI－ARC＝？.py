import sys
input = sys.stdin.readline

# 입력
h, i, a, r, c = map(int, input().split())

# 출력
print(h*i - a*r*c)