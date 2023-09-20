# 입력
a, b = map(int, input().split())

# 출력
if a >= b:
    print(b)
elif a < b and b != 0:
    print(a+1)